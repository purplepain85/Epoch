"""
Epoch System v1
Self-evaluating chain with deterministic guidance.
"""
import argparse, hashlib, json, os, secrets, sys, time
from pathlib import Path

ROOT = Path(os.environ.get("EPOCH_DATA_ROOT", str(Path.home() / "epoch" / "data")))
ROOT.mkdir(parents=True, exist_ok=True)

BACKUP_DIR = ROOT.parent / "backups"
BACKUP_DIR.mkdir(parents=True, exist_ok=True)


def backup_chain(tag="auto"):
    """Snapshot all epoch data to backups/<timestamp>_<tag>/ before any destructive op."""
    import shutil as _sh
    from datetime import datetime as _dt
    stamp = _dt.now().strftime("%Y%m%d_%H%M%S")
    dst = BACKUP_DIR / f"{stamp}_{tag}"
    if ROOT.exists():
        _sh.copytree(ROOT, dst)
    return dst



# ---------- helpers ----------

def now():
    return time.time()


def sha256_hex(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode()).hexdigest()


def jdump(obj):
    return json.dumps(obj, indent=2, sort_keys=True)


def load(path):
    return json.loads(Path(path).read_text())


def save(path, obj):
    Path(path).write_text(jdump(obj))


def origin_path(epoch):
    return ROOT / epoch / "origin.json"


def block_path(epoch, seq):
    return ROOT / epoch / f"block_{seq:06d}.json"


# ---------- origin ----------

def new_origin(goal, parent_epoch=None, reason=None):
    epoch = secrets.token_hex(32)
    origin = {
        "epoch": epoch,
        "goal": goal,
        "namespace": goal,
        "timestamp": now(),
        "parent_epoch": parent_epoch,
        "fork_reason": reason,
        "created_at": now(),
    }
    (ROOT / epoch).mkdir(parents=True, exist_ok=True)
    save(origin_path(epoch), origin)
    return origin


# ---------- block ----------

def add_block(epoch, state, projection, next_action=None):
    origin = load(origin_path(epoch))
    existing = sorted(int(p.stem.split("_")[1]) for p in (ROOT / epoch).glob("block_*.json"))
    seq = existing[-1] + 1 if existing else 1

    if existing:
        prev = load(block_path(epoch, existing[-1]))
        prev_elapsed = prev["elapsed"]
    else:
        prev = None
        prev_elapsed = 0.0

    t = now()
    elapsed = t - origin["timestamp"]

    # math check
    if elapsed <= prev_elapsed:
        return {
            "ok": False,
            "reason": "elapsed not increasing",
            "action": "prompt_freeze",
            "epoch": epoch,
            "seq": seq,
        }

    divergence = None
    last_action_result = None
    if prev is not None and "projection" in prev:
        divergence = compute_divergence(prev["projection"], state)
    if prev is not None and prev.get("next_action"):
        proj_action = prev["next_action"]
        actual_action = (state.get("action_taken") if isinstance(state, dict) else None)
        last_action_result = {
            "projected": proj_action,
            "actual": actual_action,
            "matched": (proj_action == actual_action),
        }

    block = {
        "epoch": epoch,
        "seq": seq,
        "elapsed": elapsed,
        "timestamp": t,
        "state": state,
        "projection": projection,
        "next_action": next_action,
        "last_action_result": last_action_result,
        "divergence": divergence,
        "prev_seq": existing[-1] if existing else None,
    }
    save(block_path(epoch, seq), block)
    return {"ok": True, "block": block}


def compute_divergence(projection, state):
    """Very simple scalar divergence: count of differing keys + numeric delta."""
    diffs = {}
    keys = set(projection.keys()) | set(state.keys())
    for k in keys:
        p = projection.get(k)
        s = state.get(k)
        if isinstance(p, (int, float)) and isinstance(s, (int, float)):
            diffs[k] = s - p
        elif p != s:
            diffs[k] = {"projected": p, "actual": s}
    return diffs


# ---------- verify ----------

def verify(epoch):
    origin = load(origin_path(epoch))
    blocks = sorted((ROOT / epoch).glob("block_*.json"))
    prev_elapsed = 0.0
    prev_seq = None
    for p in blocks:
        b = load(p)
        if b["epoch"] != epoch:
            return {"ok": False, "reason": f"wrong epoch in {p.name}", "seq": b["seq"]}
        if prev_seq is not None and b["seq"] != prev_seq + 1:
            return {"ok": False, "reason": f"seq gap at {b['seq']}", "seq": b["seq"]}
        if b["elapsed"] <= prev_elapsed:
            return {"ok": False, "reason": f"elapsed not increasing at seq {b['seq']}", "seq": b["seq"]}
        prev_elapsed = b["elapsed"]
        prev_seq = b["seq"]
    missing_next = [b["seq"] for b in [load(p2) for p2 in blocks] if not b.get("next_action")]
    return {"ok": True, "blocks": len(blocks), "epoch": epoch, "missing_next_action": missing_next}


# ---------- fork ----------

def fork(epoch, seq, new_goal, reason):
    """Fork from block `seq` of `epoch`. Creates new origin referencing parent."""
    origin = load(origin_path(epoch))
    fork_origin = new_origin(
        goal=new_goal,
        parent_epoch=epoch,
        reason=reason,
    )
    fork_origin["forked_from_seq"] = seq
    save(origin_path(fork_origin["epoch"]), fork_origin)
    return fork_origin


# ---------- freeze ----------

def freeze_path(epoch, seq):
    return ROOT / epoch / f"frozen_{seq:06d}.json"


def freeze(epoch, seq, reason):
    save(freeze_path(epoch, seq), {"epoch": epoch, "seq": seq, "reason": reason, "at": now()})


def thaw(epoch, seq):
    p = freeze_path(epoch, seq)
    if p.exists():
        p.unlink()


def is_frozen(epoch, seq):
    return freeze_path(epoch, seq).exists()


# ---------- seal ----------

def seal(epoch):
    blocks = sorted((ROOT / epoch).glob("block_*.json"))
    payload = load(origin_path(epoch))
    for p in blocks:
        payload[p.name] = load(p)
    seal_value = sha256_hex(jdump(payload))
    (ROOT / epoch / "seal.json").write_text(jdump({"epoch": epoch, "seal": seal_value, "at": now()}))
    return seal_value


# ---------- cli ----------



def cmd_bots(args):
    """Dispatch to botctl as a subcommand: epoch.py bots <subcommand> [args...]"""
    import subprocess, sys as _sys
    botctl = Path.home() / "epoch" / "botctl"
    if not botctl.exists():
        print("botctl not found at", botctl); return 1
    r = subprocess.run([_sys.executable, str(botctl), *args.botargs])
    return r.returncode




def cmd_bots(args):
    import subprocess, sys as _sys
    botctl = Path.home() / 'epoch' / 'botctl'
    if not botctl.exists():
        print('botctl not found at', botctl); return 1
    r = subprocess.run([_sys.executable, str(botctl), *args.botargs])
    return r.returncode

def cmd_new(args):
    origin = new_origin(args.goal)
    print(jdump(origin))


def cmd_add(args):
    state = load(args.state)
    projection = load(args.projection)
    # pick most recent epoch if not given
    epoch = args.epoch or max([p.name for p in ROOT.iterdir() if p.is_dir()])
    result = add_block(epoch, state, projection, next_action=getattr(args, "next", None))
    print(jdump(result))


def cmd_show(args):
    p = block_path(args.epoch, args.seq)
    print(jdump(load(p)))


def cmd_verify(args):
    result = verify(args.epoch)
    print("PASS" if result["ok"] else "FAIL")
    print(jdump(result))
    return 0 if result["ok"] else 1


def cmd_fork(args):
    result = fork(args.epoch, args.seq, args.goal, args.reason)
    print(jdump(result))


def cmd_freeze(args):
    freeze(args.epoch, args.seq, args.reason)
    print("frozen")


def cmd_thaw(args):
    thaw(args.epoch, args.seq)
    print("thawed")




def cmd_summary(args):
    import json as _j
    epoch = args.epoch
    blocks = sorted((ROOT / epoch).glob('block_*.json'))
    if not blocks:
        print('no blocks')
        return
    print(f"{'seq':>3}  {'elapsed':>10}  {'matched':>7}  next_action")
    print('-' * 80)
    for p in blocks:
        b = _j.loads(p.read_text())
        mar = b.get('last_action_result') or {}
        matched = mar.get('matched')
        mstr = {True: 'yes', False: 'no', None: '-'}.get(matched, str(matched))
        na = (b.get('next_action') or '')[:60]
        print(f"{b['seq']:>3}  {b['elapsed']:>10.1f}  {mstr:>7}  {na}")




def cmd_scope(args):
    import subprocess, sys as _sys
    parser = Path.home() / 'epoch' / 'scope_parser.py'
    if not parser.exists():
        print('scope_parser.py not found'); return 1
    r = subprocess.run([_sys.executable, str(parser), args.slug])
    return r.returncode


def cmd_seal(args):
    print(seal(args.epoch))


def main():
    p = argparse.ArgumentParser(prog="epoch")
    sub = p.add_subparsers(dest="cmd", required=True)

    n = sub.add_parser("new"); n.add_argument("goal"); n.set_defaults(fn=cmd_new)
    bs = sub.add_parser("bots")
    bs.add_argument("botargs", nargs="+", help="subcommand for botctl, e.g. list, status <name>, start <name>")
    bs.set_defaults(fn=cmd_bots)
    b = sub.add_parser("backup"); b.add_argument("--tag", default="manual"); b.set_defaults(fn=lambda a: print(backup_chain(a.tag)))
    a = sub.add_parser("add"); a.add_argument("state"); a.add_argument("projection"); a.add_argument("--epoch"); a.add_argument("--next"); a.set_defaults(fn=cmd_add)
    s = sub.add_parser("show"); s.add_argument("epoch"); s.add_argument("seq", type=int); s.set_defaults(fn=cmd_show)
    v = sub.add_parser("verify"); v.add_argument("epoch"); v.set_defaults(fn=cmd_verify)
    sc = sub.add_parser("scope"); sc.add_argument("slug"); sc.set_defaults(fn=cmd_scope)
    sm = sub.add_parser("summary"); sm.add_argument("epoch"); sm.set_defaults(fn=cmd_summary)
    f = sub.add_parser("fork"); f.add_argument("epoch"); f.add_argument("seq", type=int); f.add_argument("goal"); f.add_argument("reason"); f.set_defaults(fn=cmd_fork)
    fr = sub.add_parser("freeze"); fr.add_argument("epoch"); fr.add_argument("seq", type=int); fr.add_argument("reason"); fr.set_defaults(fn=cmd_freeze)
    th = sub.add_parser("thaw"); th.add_argument("epoch"); th.add_argument("seq", type=int); th.set_defaults(fn=cmd_thaw)
    sl = sub.add_parser("seal"); sl.add_argument("epoch"); sl.set_defaults(fn=cmd_seal)

    args = p.parse_args()
    rc = args.fn(args)
    sys.exit(rc or 0)


if __name__ == "__main__":
    main()

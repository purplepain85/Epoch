import hashlib, json, os, subprocess, sys, time
from pathlib import Path

SIGNAL = Path.home() / "epoch" / "signal"
TIMEOUT = 300
POLL = 15
LOG = Path.home() / "epoch" / "watch_state.log"


def log(msg):
    line = f"[{time.strftime('%H:%M:%S')}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def signal_age():
    if not SIGNAL.exists():
        return None
    return time.time() - SIGNAL.stat().st_mtime


def tree_hash(path):
    h = hashlib.sha256()
    for f in sorted(path.rglob("*")):
        if not f.is_file():
            continue
        if ".git" in f.parts or "test_tmp" in f.parts or "backups" in f.parts:
            continue
        try:
            h.update(str(f.relative_to(path)).encode())
            h.update(f.read_bytes())
            h.update(str(f.stat().st_mtime).encode())
        except Exception:
            pass
    return h.hexdigest()


def write_block(epoch, state, projection):
    tmp_state = Path.home() / "epoch" / "ws_state.json"
    tmp_proj = Path.home() / "epoch" / "ws_proj.json"
    tmp_state.write_text(json.dumps(state))
    tmp_proj.write_text(json.dumps(projection))
    r = subprocess.run(
        [sys.executable, str(Path.home() / "epoch" / "epoch.py"),
         "add", str(tmp_state), str(tmp_proj), "--epoch", epoch],
        capture_output=True, text=True,
    )
    return r.stdout + r.stderr


def main():
    if len(sys.argv) < 3:
        print("usage: watch_state.py <epoch> <dir>")
        return 1
    epoch = sys.argv[1]
    watch_dir = Path(sys.argv[2])

    state = "INACTIVE"
    last_hash = tree_hash(watch_dir)
    log(f"start epoch={epoch[:12]} dir={watch_dir} state={state}")
    log(f"baseline hash={last_hash[:12]}")

    while True:
        try:
            age = signal_age()
            new_state = "ACTIVE" if age is not None and age < TIMEOUT else "INACTIVE"
            if new_state != state:
                log(f"state transition: {state} -> {new_state} (signal age={age})")
                state = new_state

            if state == "ACTIVE":
                current = tree_hash(watch_dir)
                if current != last_hash:
                    state_obj = {
                        "action_taken": "detected file change while active",
                        "dir": str(watch_dir),
                        "hash": current[:16],
                        "trigger": "watchdog_active",
                        "signal_age_s": round(age, 1) if age is not None else None,
                    }
                    result = write_block(epoch, state_obj, {})
                    log("change detected -> block written")
                    log(result[-300:])
                    last_hash = current

            time.sleep(POLL)
        except KeyboardInterrupt:
            log("stopped")
            return 0
        except Exception as e:
            log(f"error: {type(e).__name__}: {e}")
            time.sleep(POLL)


if __name__ == "__main__":
    sys.exit(main())

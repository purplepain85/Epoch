import json, os, shutil, subprocess, sys, time
from pathlib import Path

ROOT = Path.home() / "epoch"
EP = ROOT / "epoch.py"
TMP = ROOT / "test_tmp"
if TMP.exists():
    shutil.rmtree(TMP)
TMP.mkdir(parents=True)

# redirect the epoch system's data dir to test_tmp via env var
ENV = {**os.environ, "EPOCH_DATA_ROOT": str(TMP)}

def run(*args):
    r = subprocess.run([sys.executable, str(EP), *args], capture_output=True, text=True, env=ENV)
    return r.returncode, r.stdout, r.stderr

# 1. create origin
rc, out, err = run("new", "test goal")
assert rc == 0, err
origin = json.loads(out)
epoch = origin["epoch"]
assert len(epoch) == 64
print("[1] origin ok")

# 2. add block 1
(TMP / "s1.json").write_text(json.dumps({"step": 1, "value": 100}))
(TMP / "p1.json").write_text(json.dumps({"step": 2, "value": 110}))
time.sleep(0.1)
rc, out, err = run("add", str(TMP / "s1.json"), str(TMP / "p1.json"), "--epoch", epoch, "--next", "step two")
assert rc == 0, err
b1 = json.loads(out)
assert b1["ok"], b1
assert b1["block"]["seq"] == 1
assert b1["block"]["epoch"] == epoch
assert b1["block"]["next_action"] == "step two"
print("[2] block 1 ok, next_action stored")

# 3. add block 2 — should check block 1's next_action
(TMP / "s2.json").write_text(json.dumps({"step": 2, "value": 105, "action_taken": "step two"}))
(TMP / "p2.json").write_text(json.dumps({"step": 3, "value": 120}))
time.sleep(0.1)
rc, out, err = run("add", str(TMP / "s2.json"), str(TMP / "p2.json"), "--epoch", epoch, "--next", "step three")
b2 = json.loads(out)
assert b2["ok"], b2
assert b2["block"]["seq"] == 2
assert b2["block"]["divergence"] is not None
assert b2["block"]["divergence"]["value"] == 105 - 110
assert b2["block"]["last_action_result"]["matched"] is True
print("[3] block 2 ok, divergence + action match")

# 4. verify
rc, out, err = run("verify", epoch)
assert "PASS" in out, out
print("[4] verify ok")

# 5. show
rc, out, err = run("show", epoch, "1")
assert rc == 0
shown = json.loads(out)
assert shown["seq"] == 1
print("[5] show ok")

# 6. fork
rc, out, err = run("fork", epoch, "1", "new goal", "direction change")
assert rc == 0, err
child = json.loads(out)
assert child["parent_epoch"] == epoch
assert child["epoch"] != epoch
assert child["goal"] == "new goal"
assert child["forked_from_seq"] == 1
print("[6] fork ok")

# 7. seal
rc, out, err = run("seal", epoch)
assert rc == 0
assert len(out.strip()) == 64
print("[7] seal ok")

# 8. intrusion: block with wrong epoch
fake_epoch = "0" * 64
(TMP / fake_epoch).mkdir(exist_ok=True)
(TMP / fake_epoch / "origin.json").write_text(json.dumps({
    "epoch": fake_epoch, "goal": "x", "namespace": "x", "timestamp": time.time(),
    "parent_epoch": None, "fork_reason": None, "created_at": time.time()
}))
(TMP / fake_epoch / "block_000001.json").write_text(json.dumps({
    "epoch": epoch, "seq": 1, "elapsed": 5.0, "timestamp": time.time(),
    "state": {}, "projection": {}, "divergence": None, "prev_seq": None,
}))
rc, out, err = run("verify", fake_epoch)
assert "FAIL" in out, out
assert "wrong epoch" in out
print("[8] intrusion detection ok")

print()
print("ALL TESTS PASS")
print("test data lives in:", TMP)
print("real data untouched:", ROOT / "data")

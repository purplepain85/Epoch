# Epoch System — Design

## Purpose
An external memory for work that can't be trusted to remember itself.
Each block is a self-contained position on a chain: past, present, projected future.

## Origin
- Random 32-byte epoch, generated once
- Timestamp in seconds (float)
- Fields: goal, namespace, epoch, timestamp, parent_epoch, fork_reason
- Block 0

## Block fields
- `epoch` — origin epoch (shared across all blocks in the chain)
- `seq` — integer, strictly increasing, no gaps within a branch
- `elapsed` — seconds since origin (float, high precision)
- `timestamp` — absolute seconds
- `state` — dict, project state at this block
- `projection` — dict, what the next block's state should be (the vision)
- `next_action` — string, the single concrete step to move toward the goal
- `last_action_result` — dict, compares previous block's `next_action` to what actually happened
- `divergence` — dict, computed from prev.projection vs this.state

## Sequence rules
- Each new block's elapsed must be strictly greater than the previous
- Math check: `this.elapsed - prev.elapsed` must be positive
- If math fails → reject block, prompt "freeze sequence? y/n"
- If seq out of order → reject block, prompt "freeze sequence? y/n"
- Freeze locks the specific sequence, doesn't kill the chain

## Projection vs next_action
- `projection` is the vision — what the whole should look like at the next block
- `next_action` is the step — the single thing to do right now to get there
- The next block compares its state to the previous block's `projection` (→ divergence)
- The next block compares what was actually done to the previous block's `next_action` (→ last_action_result.matched)
- Drift is visible on both axes: vision drift (did the state move toward the projection?) and step drift (did you take the action you said you would?)

## Uniqueness
- `(epoch, seq)` pair globally unique
- A block without the correct epoch is an intrusion, not a block

## Deletion
- Any block can be removed
- Remaining blocks keep original seq numbers
- The gap is detectable
- Chain continues from last valid block
- Epoch unchanged

## Regression = Fork
- Going back to an earlier point starts a new branch
- Original branch intact
- New branch has its own seq namespace
- New branch shares the epoch with the origin

## Fork = New Origin
- New epoch generated
- Elapsed starts at 0
- Namespace updated to reflect the new goal
- References parent origin
- Documents reason
- Old chain intact

## Intrusion
- Wrong epoch → rejected
- Bad math → rejected, prompt freeze
- Duplicate seq → rejected, prompt freeze
- Freeze is temporary, sequence-specific
- Nothing happens automatically; user acknowledges

## Seal
- When goal reached, chain seals
- Seal = hash(origin + all blocks)
- Any change after seal invalidates the seal

## Commands
- `epoch.py new "goal"` → creates origin
- `epoch.py add <state> <projection> --next "action"` → creates block
- `epoch.py show <seq>` → prints block
- `epoch.py verify` → PASS/FAIL with reason
- `epoch.py fork <seq> "new goal" "reason"` → creates new origin
- `epoch.py freeze <seq> "reason"` → freezes
- `epoch.py thaw <seq>` → unfreezes
- `epoch.py seal` → seals chain

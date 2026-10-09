# epoch

A local, self-hosted log for long-running work. Each block carries its state, its projection for the next block, and the action to take. Divergence is computed at each block. Forks are explicit. The chain is sealed with a hash of origin + all blocks.

## Why

Long projects lose their thread. Decisions get reversed without acknowledgment. Drift becomes the new plan without anyone saying so. epoch makes the drift visible — each block records what was projected and what actually happened.

## Install

Requires Python 3.9+.

    git clone <this-repo> ~/epoch
    cd ~/epoch
    python epoch.py --help

## Usage

    # Start a chain
    python epoch.py new "your goal"

    # Add a block
    python epoch.py add state.json projection.json --next "next action" --epoch <hash>

    # Verify the chain
    python epoch.py verify <hash>

    # See all blocks
    python epoch.py summary <hash>

    # Fork (goal changes)
    python epoch.py fork <hash> <seq> "new goal" "reason"

    # Seal
    python epoch.py seal <hash>

## Bot tracker

    python epoch.py bots list
    python epoch.py bots add <name> <script> [args...]
    python epoch.py bots start <name>
    python epoch.py bots tail <name>

## Watchdog

Polls a directory and writes a block when it changes, while active. Active state is triggered by a signal file, refreshed on every shell prompt.

    python epoch.py watch --epoch <hash> --dir <path> --interval 60

## Design

See DESIGN.md.

## License

MIT

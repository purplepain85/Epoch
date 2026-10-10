# Architecture

The hub is a modular system. Each module is independent. Each module has
a defined interface — what it needs from others, what it provides. Any
module can be replaced without breaking the rest.

## Status

| # | Module | Status | Depends on |
|---|--------|--------|------------|
| 01 | Overview | draft | — |
| 02 | Hub | draft | 01 |
| 03 | Pipeline | draft | 02 |
| 04 | Spin Filter | draft | 03 |
| 05 | Outputs | draft | 03 |
| 06 | Media | draft | 03 |
| 07 | Interactions | draft | 05, 06 |
| 08 | Event Log | draft | 02 |
| 09 | Revenue | draft | 02, 08 |
| 10 | Operator | draft | 02, 09 |

## Module interface

Each module file begins with a header:

    Depends on: [module files this one requires]
    Provides:   [what this module defines that others use]
    Version:    0.1
    Status:     draft | review | final

## Ordering

Modules are numbered for reading order, not build order. Build order is
bottom-up: Event Log first, then Hub, then Pipeline, then everything else.

## Building

Every module ships as its own file. `git commit` after each. Any module
can be swapped, replaced, or removed by editing its file and updating
the status table above.

## Versioning

Every module carries a version number. Breaking changes to a module bump
its major. Additive changes bump the minor. Fixes bump the patch.

## Reference

The runtime that runs this — the epoch chain — lives at the repository
root. The design of the chain itself is in `../../DESIGN.md`.

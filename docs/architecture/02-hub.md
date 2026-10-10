# 02 — Hub

Depends on: 01-overview
Provides:   the runtime, storage, and rule enforcement for every market
Version:    0.1
Status:     draft

---

## What it is

The hub is the system. It runs once. It serves every market. Operators
don't run their own hub — they plug into this one.

The hub does not produce content. It runs the pipeline that produces
content. It does not take sides. It enforces the rules.

## What the hub owns

- The pipeline runtime
- The rules engine
- The event log
- The template engine
- The graphic generator
- The affiliate redirector
- The settlement accounting
- The operator dashboard and auth
- The plugin registry

## What the hub does not own

- The audience. That belongs to the operator.
- The local social accounts. Those belong to the operator.
- The podcast relationships. Those belong to the operator.
- The voice. That belongs to the operator.

## The core loop

For every incoming source article or event, the hub:

1. Receives input (paste, feed, or search result)
2. Assigns it to a market
3. Runs it through the spin filter
4. Rewrites for each output platform
5. Generates the graphic
6. Runs the rules check
7. Publishes (or queues for the operator)
8. Records every step to the event log

Every step is recorded before the next step runs. If a step fails, the
chain stops there and the failure is logged.

## Markets

Each market is a namespace in the hub. The market record holds:

- Team identity (city, colors, logo references)
- Voice settings (spin filter)
- Output channel config (Reddit, FB, X, TikTok accounts)
- Podcast list (subscribed feeds, revenue terms)
- Operator identity (who runs it, when they took over)
- Event log (append-only chain, one per market)
- Revenue state (accumulated, attributed, settled)

One hub. As many markets as there are teams with an operator.

## Rules engine

The rules engine runs before every publish. It checks:

- Attribution format is present
- Full team name is not in the branding
- Colors and logos match the market's assigned palette
- No blacklisted terms in the output
- Source credit is to the correct outlet

If a check fails, the content does not publish. It goes back to the
operator with the reason.

## Multi-tenant isolation

Each market's data is namespaced. No market can read another market's
event log, revenue state, or operator dashboard. The hub serves all of
them from one system but each sees only their own.

## Runtime requirements

- One process, long-running. Not serverless — this thing is stateful.
- A database for the event log and market records. SQLite is fine at
  first. Postgres when the volume grows.
- A file store for generated graphics and rant downloads.
- A queue for pipeline jobs so publish does not block the request.
- An API for the operator dashboard.
- An API for plugins, read-only by default.

## What the hub is not

- Not a per-operator installation. Operators don't run their own.
- Not a source of truth about facts. Facts come from credited outlets.
- Not the operator. Decisions about the local market are the operator's.
- Not a broadcaster. Posts go out from the operator's accounts, under
  the operator's identity.

## Failure modes

- **Pipeline down.** Markets stop producing. Operator is notified.
- **Rules engine down.** Nothing publishes. Safer than a bad post.
- **Event log corruption.** Detectable via chain verify. The last valid
  block is the recovery point.
- **Operator unreachable.** Markets run in auto mode until they respond.
- **Plugin failure.** That plugin disables. Market continues on the core.

# 08 — Event Log

Depends on: 02-hub
Provides:   the append-only chain that records every action in every market
Version:    0.1
Status:     draft

---

## What the event log is

Every market has a chain. Every action in that market — every article
produced, every comment posted, every affiliate click, every podcast
episode indexed, every moderation action — is written to the chain as
a block.

The chain is append-only. Nothing is edited. Nothing is deleted. Every
block references the one before it.

## Why it matters

The event log is the market's memory. It answers questions that no
other system can:

- What did this market produce last October?
- How did engagement change when the operator adjusted the spin filter?
- What was the affiliate conversion rate during the playoff run?
- Which podcast integration drove the most comments?
- When was this user banned, and why?

None of those questions can be answered without a record.

## What a block contains

Every block has:

- **Epoch.** The market's origin identifier. Every block in a market
  shares the same epoch.
- **Sequence.** The block's position in the chain. Strictly increasing.
- **Timestamp.** The absolute time.
- **Elapsed.** Time since the market's origin.
- **Type.** The kind of event (article, comment, podcast, click, etc.).
- **Payload.** The event-specific data.
- **Previous hash.** The hash of the block before this one.
- **Hash.** The hash of this block.

## Event types

### Pipeline events

- `article.intake` — a source article entered the pipeline
- `article.scored` — relevance scoring completed
- `article.spun` — spin filter applied
- `article.rehashed` — rehash produced
- `article.formatted` — output formats generated
- `article.graphic` — graphic generated
- `article.checked` — rules engine result
- `article.published` — published to a platform

### Interaction events

- `comment.created`
- `comment.edited`
- `comment.deleted`
- `comment.flagged`
- `reshare.endorsed`
- `rant.published`
- `rant.downloaded`

### Media events

- `podcast.subscribed`
- `podcast.episode.indexed`
- `podcast.thread.opened`
- `podcast.thread.closed`
- `podcast.delisted`

### Revenue events

- `affiliate.click`
- `affiliate.conversion`
- `ad.impression`
- `ad.revenue`
- `podcast.share`

### Operator events

- `operator.login`
- `operator.config.changed`
- `operator.spin.filter.adjusted`
- `operator.moderated`
- `operator.article.overrode`

### System events

- `pipeline.run.started`
- `pipeline.run.completed`
- `pipeline.run.failed`
- `chain.verify.passed`
- `chain.verify.failed`

## How blocks are written

Every event goes through the same routine:

1. Load the previous block's hash
2. Build the new block with all fields
3. Hash the new block
4. Write the block to the chain file (append-only)
5. Return the hash to the caller

If any step fails, the event is not written and the caller is notified.
A failed write is preferable to a corrupted chain.

## Storage

Phase 1: one JSON file per market, one JSON object per line (JSONL
format). Simple, greppable, portable.

Phase 2: SQLite database per market. Same block structure, indexed by
sequence and by type.

Phase 3: Postgres with partitioning per market. Same structure at scale.

The format does not change. Only the storage does.

## Verification

Any block in the chain can be verified:

1. Load the block
2. Load the previous block
3. Confirm the previous hash matches
4. Recompute the block's hash
5. Confirm the hash matches

If any step fails, the chain is broken. Verification can be run for a
single block, a range, or the whole chain.

Verification is exposed as a hub function so operators can check their
own chains.

## Sealing

At year-end, the chain is sealed. A seal is a hash of:

- The market's origin
- Every block in the chain
- The final block's hash

The seal is written to a separate file. It's the fingerprint of the
year. If any block changes, the seal no longer matches.

## Forking

If the operator changes the market's fundamental scope — new team, new
colors, new identity — the chain forks. The new chain has a new epoch
and a reference to the parent chain.

Old chains stay intact. Lineage is traceable.

## What the chain is not

- Not public by default. Each market's chain belongs to that market.
- Not aggregated across markets. The hub can compute aggregate stats
  but does not expose one market's chain to another.
- Not editable. Ever.
- Not a source of truth about the world. It's a source of truth about
  what the market did.

## What the chain enables

- **Audits.** Every affiliate conversion is provable.
- **Transfer.** A new operator inherits the full history.
- **Pricing.** The buyout price for any clause can be justified against
  what the chain shows.
- **Insight.** The operator can see exactly what worked and what
  didn't.
- **Trust.** Nobody has to take anyone else's word for anything.

## A note on performance

Append-only writes are fast. Reading the chain is fast. Verification
is the expensive operation, and it's only needed occasionally.

For 32 markets with typical volume, total chain size per market stays
in the low tens of megabytes per year. Nothing that needs special
infrastructure.

## The chain is the market

The pipeline produces content. The interaction layer produces community.
The revenue layer produces money.

The chain produces the record of all three. It is what makes everything
else provable. Without it, the market is just a set of files and
accounts. With it, the market is a fact.

# 03 — Pipeline

Depends on: 02-hub
Provides:   the production system that turns sources into outputs
Version:    0.1
Status:     draft

---

## What the pipeline is

The pipeline takes raw input — a news article, a podcast episode, a
game result — and produces formatted output for every market's channels.
It runs continuously. It runs in two modes. It logs every step.

## Two modes

### Auto mode

The pipeline searches for news on its own. It finds stories, scores them
for relevance, applies the market's spin filter, produces output, and
queues for publish.

The operator does not have to do anything. The market keeps producing
even when the operator is asleep, at work, or on vacation.

### Manual mode

The operator pastes a source article, writes a prompt, or sets the day's
tone. The pipeline takes the input and produces from it.

Manual mode is for the operator who wants to steer. It overrides the
auto mode's defaults for that piece.

Both modes feed the same output layer. Both are logged the same way.

## Input sources

In Phase 1 (manual), the input is whatever the operator pastes.

In Phase 2 (auto), the pipeline searches:

- Credited news outlets (ESPN, NFL.com, The Athletic, local beat writers)
- Team subreddits
- Team podcasts via RSS
- Public social accounts of beat reporters
- Official team releases

Every source is recorded. Every article names where its facts came from.

## The pipeline stages

### Stage 1 — Intake

A source article or event enters the pipeline. It's tagged with:

- Source (outlet, URL, timestamp)
- Market (which team it belongs to)
- Type (news, analysis, podcast, injury report, game result)
- Category (trade, draft, injury, coaching, stats)

The intake stage is the only stage where human input can be required.
Everything after is automatic.

### Stage 2 — Relevance scoring

The pipeline scores the input for relevance to the market:

- Team relevance: 0–100
- Timeliness: 0–100
- Engagement likelihood: 0–100
- Duplicate check: new / seen / related

Score below threshold = not produced. Score above = goes to the next
stage.

### Stage 3 — Spin filter

The market's spin filter is applied. This sets:

- Voice (hype, analytical, skeptical, humorous)
- Length (short, medium, long)
- Angle (from the fanbase perspective, from the coach's perspective)
- Emphasis (which elements of the story to lead with)

Same story, different spin, per market. What runs on Minnesota's market
is not the same piece that runs on Detroit's, even if the source is the
same article.

### Stage 4 — Rehash

The pipeline rewrites the source article in the market's voice. This is
not a copy. It's a rehash — same facts, different structure, different
opening, different closing. Attribution to the source outlet remains.

The rehash is the primary content piece for the market.

### Stage 5 — Format for outputs

The rehash is then formatted for each platform:

- Reddit: long-form markdown with headers, source link at the end
- Facebook: text post, graphic attached, link in first comment
- X: thread of 3–5 posts, hook first, link last
- TikTok: 30–60 second script, hook in first 3 seconds, one key moment

Each format has its own rules. Each is produced from the same source.

### Stage 6 — Graphic generation

For each piece, a graphic is generated:

- Team colors as background
- Title and subtitle
- Date or key stat
- Network mark (Gridiron Central)
- No full team name

The graphic is generated once and reused across platforms.

### Stage 7 — Rules check

Before anything publishes, the rules engine runs:

- Attribution format present
- Full team name not in the branding
- Colors and logos match the market's palette
- No blacklisted terms
- Source credit correct

Fail = not published. The piece goes back to the operator with the
reason.

### Stage 8 — Publish

The piece is published to each platform. In Phase 1, publishing is manual
— the operator copies and pastes. In Phase 2, it's automatic via each
platform's API.

Every publish is logged with: platform, account, URL, timestamp.

### Stage 9 — Event log

Every stage above writes a block to the market's event log. The chain
records:

- What the input was
- What the relevance score was
- What the spin filter produced
- What the rehash said
- What formats were generated
- What the graphic was
- What the rules check said
- When it published
- Where it published

Nothing is edited. The log is append-only.

## Failure handling

If any stage fails:

- The chain stops
- The failure is logged
- The operator is notified
- The piece does not publish

A failed pipeline run is preferable to a bad publish. The system errs on
the side of not publishing.

## Cadence

The pipeline runs at a configurable cadence per market:

- **In-season weekly:** 3–10 articles per day
- **In-season gameday:** 10–20 articles per day
- **Off-season:** 1–3 articles per day
- **Special events (draft, free agency):** continuous

The operator sets the cadence. The pipeline meets it.

## Pipeline throughput

One pipeline instance can serve many markets. The same process handles
all 32 markets in parallel:

- Sources are shared (same outlet feeds, same reporter accounts)
- Relevance scoring runs per market
- Spin filters are per market
- Outputs are per market
- The event log is per market

The pipeline does not need one instance per market. It needs one
instance, many threads.

## What the pipeline never does

- Publish without a rules check
- Skip the event log
- Copy the source verbatim
- Attribute to anyone other than the original outlet
- Publish to a platform the market has not configured

The pipeline is the input. The market is the output. The rules engine is
the gate. The event log is the record.

## What runs it

Phase 1: a Python process running on a server, with manual triggers and
scheduled runs.

Phase 2: a queue-based system that runs continuously, with worker
processes per market and retry logic for failures.

Phase 3: distributed across multiple servers, with one process per
market, all reporting to a central event log.

The interface between phases stays the same. Only the volume changes.

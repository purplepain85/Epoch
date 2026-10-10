# 04 — Spin Filter

Depends on: 03-pipeline
Provides:   the per-market voice specification
Version:    0.1
Status:     draft

---

## What the spin filter is

Every market has a voice. The spin filter is where that voice is
specified. It controls how the pipeline rewrites any given source
article into the market's version of the story.

Same source article. Different spin. Different market.

## Why it matters

The same trade rumor runs in 32 markets. The Minnesota version sounds
like a Minnesota fan wrote it. The Detroit version sounds like a Detroit
fan wrote it. The Dallas version sounds like a Dallas fan wrote it. None
of them sound like a wire service.

If the spin filter fails, all 32 markets sound the same. That kills the
product. The voice is the product.

## What the filter controls

### Voice

The general tone of the market. Options:

- **Hype.** Optimistic, celebratory, convinced the team is on the rise.
- **Analytical.** Data-driven, measured, interested in the why.
- **Skeptical.** Critical, quick to question, hard to impress.
- **Humorous.** Self-deprecating, jokey, doesn't take itself seriously.
- **Old school.** Traditional, values fundamentals, allergic to hype.
- **New school.** Modern, stats-forward, embraces analytics.

A market is usually a mix. Dallas might be 60% hype, 30% analytical,
10% old school. Minnesota might be 40% analytical, 40% humorous, 20%
skeptical. The mix is the voice.

### Length

How long the articles run, on average:

- **Short:** 200–400 words. Quick hits, comments, reactions.
- **Medium:** 400–800 words. Standard articles.
- **Long:** 800–1,500 words. Deep dives, features, analysis.

### Angle

Whose perspective the article takes:

- **Fan perspective:** "Here's what this means for us."
- **Analyst perspective:** "Here's what this means objectively."
- **Insider perspective:** "Here's what the front office is thinking."
- **Historical perspective:** "Here's how this compares to past seasons."

### Emphasis

What the article leads with:

- **The moment:** the play, the trade, the injury.
- **The context:** what led to this moment.
- **The consequence:** what happens next.
- **The reaction:** what the fanbase is saying.

### Vocabulary

Words and phrases the market uses. Some markets call the team "we."
Others say "the team." Some markets use specific slang. The filter
captures these.

### Taboo list

Words and phrases the market avoids. Slurs, trademarks that aren't
allowed, phrases that alienate the audience. The filter enforces the
list.

### Cadence of voice

Does the voice stay constant, or shift by context? Some markets are
serious about game coverage and funny about off-season news. The filter
allows for that.

## How the filter is set

### Initial setup

At onboarding, the operator configures the spin filter. The hub offers
defaults based on the market's team and audience. The operator adjusts.

### Adjustable over time

The filter can be changed anytime. Changes are logged as events. The
old filter stays in the record.

### Per-article overrides

For any specific article, the operator can override the filter with a
manual prompt. "Spin this one skeptical" or "keep this one neutral."

The override applies to that article only. The market's default filter
stays in place.

## The spin filter as a prompt

Under the hood, the spin filter is a system prompt for the AI that does
the rehash. It looks something like:

    You are writing for the [market] Gridiron Central market.
    Your voice is: [voice mix, percentages].
    Your average article length is: [length].
    Your angle is: [angle].
    Lead with: [emphasis].
    Use these words: [vocabulary].
    Never use these words: [taboo list].
    Attribution to the source outlet is required.
    The full team name must appear only in attribution.

Then the source article is appended, and the AI produces the rehash.

## What the filter does not control

- The facts. Facts come from the source.
- The attribution. It's always to the source outlet.
- The brand rules. Those run after the filter, not through it.
- The output format. That's stage 5 of the pipeline.

The filter controls voice only. Everything else is handled separately.

## Reading the filter

Every market's filter can be read by:

- The operator (in their dashboard)
- The hub (for consistency checking)
- Future operators (when a market is transferred)

The filter is part of the market's record. It's not private. It's not
editable without logging.

## The filter's effect on outcomes

Different filters produce different engagement:

- Hype voices tend to get more shares, fewer deep comments.
- Analytical voices tend to get fewer shares, more comments.
- Humorous voices tend to get the most re-shares.
- Skeptical voices tend to get the most argument.

The pipeline measures the correlation between voice settings and
engagement, per market. Over time, the operator can see which settings
produce which outcomes and adjust.

The measurement is not automatic adjustment. The operator decides. The
data is there to inform the decision.

## Default filters by team type

The hub ships with default filters based on team archetypes:

- **Blue blood program** (Dallas, Pittsburgh, Green Bay): hype + old
  school + long articles
- **Rebuilding team** (Chicago, Carolina): analytical + skeptical +
  medium articles
- **Contender** (Kansas City, Buffalo, San Francisco): hype +
  analytical + medium articles
- **Chaotic franchise** (Cleveland, Washington): humorous + skeptical +
  short articles

These are starting points. Every market adjusts.

## Why this matters

The spin filter is what makes the network defensible. Anyone can build
a pipeline. Anyone can hook up affiliate links. Anyone can post to four
platforms.

What they can't easily copy is the accumulated per-market voice
specification — 32 filters, each tuned to one specific fanbase, each
producing a distinct voice. That's a library, and the library is the
asset.

## What the filter is not

- Not an AI model. It's the prompt that runs against a model.
- Not a hardcoded script. It's configurable per market, per article.
- Not fixed. It changes as the market changes.
- Not public. Each market's filter belongs to that market.

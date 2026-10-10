# 05 — Outputs

Depends on: 03-pipeline
Provides:   the per-platform formatting rules for published content
Version:    0.1
Status:     draft

---

## What "outputs" means

Every market produces content for four platforms. The same source article
becomes a Reddit post, a Facebook post, an X thread, and a TikTok script.
Each platform has its own shape, its own constraints, its own audience.

This module defines those shapes.

## The four platforms

1. **Reddit** — long-form text, high signal, deep comment threads
2. **Facebook** — text post plus graphic, mixed audience, wide reach
3. **X** — threads, fast-moving, high re-share rate
4. **TikTok** — video scripts, short-form, algorithm-driven reach

Each is a distinct format. None is a copy of the others.

## Reddit

### Shape

- **Title:** 60–80 characters, fact-forward, no clickbait
- **Body:** 400–1,500 words, markdown headers, source link at end
- **Sub:** the team's subreddit, or a dedicated Gridiron Central sub
- **Tags:** appropriate flair for the sub's rules

### Formatting

- Use `##` for section headers
- Use `>` for quotes
- Use `**bold**` sparingly
- Link to source outlet in the final line
- No external affiliate links in the body — those go in a pinned comment

### Attribution

- Source outlet named in the final paragraph
- Link to the original article

### Posting cadence

- 3–10 posts per day during the season
- 1–3 posts per day off-season

### Affiliate handling

- Affiliate links in a pinned comment, added by the operator after publish
- Never in the body

## Facebook

### Shape

- **Post text:** 150–500 words, conversational, warm, more personal than Reddit
- **Graphic:** 1080×1080 or 1200×630, in market colors
- **Link:** first comment, not in the post itself

### Formatting

- Plain text, no markdown
- Emoji used sparingly, only where it fits the voice
- Paragraph breaks for readability
- No headers

### Attribution

- Source outlet mentioned at the end
- Link to original in first comment

### Posting cadence

- 3–8 posts per day during the season
- 1–2 posts per day off-season

### Affiliate handling

- Affiliate links in a second comment
- Or as a separate post, distinctly separate from editorial content

## X (Twitter)

### Shape

- **Thread:** 3–5 posts, each under 280 characters
- **Post 1:** the hook — the strongest fact or angle
- **Post 2–4:** development — what it means, who said what
- **Post 5:** conclusion plus link

### Formatting

- Each post stands alone but threads together
- Numbers or emoji to number posts (1/, 2/, 3/)
- No hashtags beyond one or two if the market uses them
- Link in the final post only

### Attribution

- Source outlet mentioned in the last post
- No link in the first post (algorithm penalizes external links early)

### Posting cadence

- 5–15 threads per day during the season
- 2–5 threads per day off-season

### Affiliate handling

- Rare on X
- Only if the market specifically runs affiliate content on X
- Never in the main thread

## TikTok

### Shape

- **Script:** 30–60 seconds of spoken or on-screen text
- **Hook:** first 3 seconds — the strongest fact or question
- **Body:** the development
- **Ending:** the market's sign-off and a call to comment

### Formatting

- Vertical video, 1080×1920
- Text-on-screen or voiceover
- Music bed from TikTok's commercial library (licensed)
- Captions required

### Attribution

- Source outlet named on-screen during the relevant segment
- Link in bio (TikTok doesn't allow clickable captions)

### Posting cadence

- 1–3 videos per day during the season
- 3–7 per week off-season

### Affiliate handling

- TikTok has its own affiliate program, plus a bio link
- Best done as separate creator content, not integrated into editorial

## Platform-specific rules

### No cross-posting the same text

Each platform gets its own version. Same source, same facts, different
shape. Reddit isn't X. Facebook isn't TikTok.

### No platform-exclusive content

Every story runs on every platform. Some markets may emphasize one
platform over another, but no story is exclusive to a single channel.

### No platform bypass of the rules engine

Every output goes through the same rules check. No platform publishes
without it.

### No direct copy from the source

Every output is a rehash. Never the original text.

## Graphic generation

Every market produces graphics in its colors. The rule:

- **Background:** team primary color
- **Text:** team secondary color, or white for contrast
- **Accent bar:** team secondary color
- **Bottom strip:** thin line in team secondary color
- **Network mark:** small "GC" or "Gridiron Central" at bottom

### What the graphic does not contain

- The team's official logo (unless under a licensing agreement)
- The full team name (Minnesota Vikings, Detroit Lions, etc.)
- NFL marks
- Player likenesses (unless properly licensed)

### What the graphic does contain

- The article's title
- A subtitle or key stat
- The date
- The market's colors
- The market's brand mark (the one we design)

## Video / TikTok production

TikTok scripts are produced by the pipeline, but recording is done by the
operator or by the hub using text-to-speech. Three options:

1. **Operator records.** Best quality. Requires the operator to spend time.
2. **Text-to-speech.** Automatic. Quality varies.
3. **Third-party host.** Paid actor or voice model. Best quality, cost.

The operator chooses per market. The pipeline produces the script either
way.

## The market's sign-off

Every market has a sign-off. It can be:

- A word (like "Skol" for Minnesota)
- A phrase (like "Roll Tide" for Alabama sports)
- A short line specific to the market's voice

The sign-off appears at the end of every post on every platform. It's the
market's signature.

## Outputs are configurable

The shapes above are defaults. Each market can adjust:

- Which platforms they publish to
- The cadence per platform
- The length and tone per platform
- The graphic style

What's not adjustable:

- The rules engine
- The attribution requirement
- The event log
- The rule against copying the source

## The output pipeline in one line

Same source. Four platforms. Four shapes. One voice. Every time.

## What's next

The outputs are where the audience lives. But the product isn't the
output. The product is what the audience does with it. That's module 07.

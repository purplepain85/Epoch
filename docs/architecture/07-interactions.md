# 07 — Interactions

Depends on: 05-outputs, 06-media
Provides:   the comment, re-share, and rant layers that make the
            market a community instead of a feed
Version:    0.1
Status:     draft

---

## The thesis of this module

The article is the prompt. The interaction is the product.

Every feature in this module exists to turn a passive reader into an
active participant. That is what turns a feed into a community and what
makes a market worth subscribing to.

## Three interaction types

1. Comments — public, threaded, moderated
2. Re-shares — endorsements, not just shares
3. Rants — long-form, downloadable, tied to the source piece

Each is logged as an event. Each contributes to the market's engagement
score.

## Comments

### Where they live

Every article, every podcast card, every video card, every game thread
gets a comment section. Automatic. No configuration required.

### Structure

Threaded. Top-level comments, replies under them, replies to replies.
Collapsed after a certain depth. Standard community behavior.

### Sorting

Default: newest first for game threads, top-rated for articles. The
operator can set per market.

### Moderation

The operator moderates. The hub provides tools:

- Flag for review
- Hide
- Delete
- Ban user (with reason logged)
- Approve flagged comment

Every moderation action is logged as an event.

### Rules

Per-market, set by the operator. Common rules across all markets:

- No slurs
- No personal attacks on players or their families
- No doxxing
- No spam
- No illegal content

### Comment identity

Users post under a handle tied to their market account. Not required to
be their real name. Not shared across markets.

## Re-shares

### What re-share means

A user reads an article and wants to say "I agree with this" or "this
is worth reading." Instead of a generic share button, the market
provides a re-share with endorsement.

The re-share carries:

- The article link
- The user's endorsement
- The user's handle
- The market's tag

### Why this matters

A normal share is a broadcast. A re-share is a broadcast with a signal.
The hub reads the signal:

- Which articles get endorsed most
- Which voices trigger endorsements
- Which topics generate agreement versus argument

### Where re-shares go

- The user's own feed
- Facebook, X, Reddit via the user's own accounts
- Back to the hub as an event

Each re-share is logged. The article's total endorsements show on the
card.

### Anti-abuse

- One endorsement per user per article
- Rate limited to prevent spam
- Endorsements from new accounts flagged for review

## Rants

### What a rant is

A reader who disagrees, or who has something long to say, can write a
rant tied to any article. The rant is:

- Written in a simple editor on the article page
- 200-2,000 words
- Saved as a downloadable file (PDF or Markdown)
- Linked back to the original article
- Signed with the user's handle

### Why rants matter

Rants are the release valve. Fans get angry about a team, a call, a
trade. If the market does not give them a place to say it, they go
somewhere else. If it does, they stay.

Rants also produce content for the market. A great rant might get
re-shared a hundred times. That is free distribution.

### Rant features

- Edit before publish
- Attach to article
- Download
- Share
- Replies
- Rant of the week

### Anti-abuse

- Rate limited
- Reviewed before display (configurable)
- Slur and threat filter applied automatically

## Game threads

### What a game thread is

During a game, the market opens a live thread. Every fan in the market
is watching the same game and reacting together.

### Structure

- The thread opens 30 minutes before kickoff
- Updates with scoring, injuries, and key plays
- Comment feed is live, newest first
- Comments are fast, short, and often funny

### Why game threads matter

Game threads are the highest-engagement feature in any sports community.
They are why people come back. A good game thread makes the market feel
like the best place to be watching the game even when the game is
terrible.

### After the game

The thread stays open. It becomes the post-game thread. Reactions,
analysis, anger, celebration — all in the same place.

The hub captures the flow of the thread for engagement metrics.

## Podcast threads

### Pre-cast and post-cast

Each podcast episode gets two threads:

- Pre-cast thread: opens when the episode is scheduled
- Post-cast thread: opens when the episode publishes

Both are comment sections. Both are logged. Both contribute to the
market's engagement score.

### Which one wins

Per market per podcast, the hub measures which thread drives more
engagement. The operator can weight the feed toward whichever works.

### Why both

Different audiences want different things. Some fans want to talk before
listening. Some want to react after. Both can exist without either
suffering.

## What engagement data feeds

Every interaction is a data point:

- Comments per article
- Re-shares per article
- Rants per article
- Game thread volume
- Podcast thread volume
- Endorsement rate per market
- Rant rate per market
- Comment velocity
- Moderation rate

The operator sees the data. The pipeline uses it to improve the spin
filter. The hub uses it to detect markets that are thriving or failing.

## What interactions are not

- Not a social network
- Not anonymous
- Not monetized directly
- Not portable

## What a successful market looks like

- Every article gets 20+ comments within the first hour
- Game threads hit 500+ comments during a close game
- Rants appear at least weekly
- Re-share rate is 5%+ of readers
- Comment velocity peaks during games and podcast drops
- Moderation rate stays under 1 flag per 100 comments

If those numbers hold, the market is working.

## The interaction is the product

The article gets them to the page. The comments keep them there. The
rants bring them back. The game threads bring them every Sunday.

That is the whole point. Not the aggregation. Not the affiliate links.
Not the podcast cards.

The community.

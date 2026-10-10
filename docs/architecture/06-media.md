# 06 — Media

Depends on: 03-pipeline
Provides:   how external media is surfaced, indexed, and monetized
Version:    0.1
Status:     draft

---

## What "media" means

The hub does not produce audio or video. It surfaces media that already
exists — podcasts, YouTube channels, Twitter spaces, team content — and
integrates it into the market feed alongside the articles.

The market becomes the place where a fan can find the article AND the
podcast about the article, on the same card, at the same time.

## What gets integrated

- **Podcasts.** Team-focused shows, both fan-run and professional.
- **YouTube channels.** Team-focused video creators.
- **Twitter/X Spaces.** Live audio events, recorded and archived.
- **Streamer content.** Twitch streams by fan creators covering the team.
- **Official team content.** Press conferences, highlights, official
  interviews — linked and credited, not reproduced.

The default is podcasts. Other media types are added per market as the
operator chooses.

## Podcast integration

### Discovery

The operator finds the team-friendly podcasts in their city. Team-friendly
means:

- Positive or neutral toward the team
- Not controversy-driven
- Not anti-fan or anti-player
- Not a "hot take" show that generates drama

The operator knows the shows. The hub does not discover them. The
operator picks.

### Subscription

For each podcast, the operator enters the RSS feed URL. The hub:

- Pulls the feed
- Indexes episodes
- Tags episodes by topic, player, game, and event
- Displays the episode in the market feed

### Episode flow

When a new episode drops:

1. The hub detects it within minutes
2. The episode is indexed and tagged
3. A card appears in the market feed
4. A pre-cast thread opens (if configured)
5. The episode publishes to listeners
6. A post-cast thread opens

The pre-cast and post-cast threads run in parallel by default. The
operator can weight one over the other per market.

## The comment threads

Each podcast episode gets two threads:

### Pre-cast thread

Opens when the episode is scheduled or when the feed notices an upcoming
release. Purpose:

- "What do you want them to cover?"
- "Predictions before the episode drops."
- "Any questions for the hosts?"

The audience talks before they listen. The podcast hosts can see the
thread and address the audience's questions on air.

### Post-cast thread

Opens when the episode publishes. Purpose:

- "What did you think?"
- "Timestamp your favorite moment."
- "Quote the best line."

The audience talks after they listen. The thread stays open as long as
the operator wants — 24 hours, a week, or indefinitely.

### Which thread wins

The hub measures engagement per thread type per market per podcast. Over
time, per market, the operator sees which is working and can weight
accordingly.

## Revenue from media

The operator earns from media integrations in three ways:

### 1. Referral clicks

Every podcast card links to the podcast platform through the hub's
redirector. Clicks are tracked. If the platform pays for referrals
(Spotify, Apple, YouTube), the operator earns.

### 2. Live-time share

During the first hour after an episode drops — the window when the
market is most active — a percentage of the market's activity is
attributed to that podcast. The podcast receives a share, the operator
receives a share.

### 3. Engagement share

If an episode generates high comment volume or a viral thread, the
podcast gets a bigger cut. The operator also gets a bigger cut.

The specific percentages are negotiated per podcast within a standard
range.

## Compensation to the podcast

The podcast does not pay to be listed. The podcast is not paid upfront.
The podcast receives a share of the market activity its episodes
generate.

### What the podcast receives

- **Referral traffic.** New listeners from the market.
- **Live-time share.** A percentage of market activity during the
  episode drop window.
- **Engagement share.** A percentage of market activity on the episode's
  comment threads, scaled by engagement.
- **Promotion.** The market promotes the podcast in its own feed, on
  other platforms, and in cross-market content.
- **Metrics.** The podcast gets a dashboard showing how their episodes
  performed in this market — listenership driven, comments, shares.

### What the podcast does not receive

- Payment upfront.
- Editorial control over the market.
- Data about the market's other podcasts or revenue.

## Team-friendly filter

Not every podcast qualifies. The operator applies the team-friendly
filter. Criteria:

- No player bashing beyond normal critical coverage
- No coaching rumors without credible sourcing
- No personal attacks on team employees
- No leaks of private team information
- No controversy-driven episodes

If a podcast stops meeting the criteria, the operator can delist it.
Delisting is logged. The podcast can be re-listed if it returns to form.

## Other media types

### YouTube channels

Same pattern as podcasts. The operator finds the channel. The hub pulls
the RSS feed. Videos are indexed and tagged. The card appears in the
market feed with a thumbnail and title.

### Twitter/X Spaces

Live audio events. The hub surfaces upcoming Spaces, indexes recorded
Spaces, and links to replays. Twitter/X does not expose Spaces via a
public RSS feed, so indexing is done via a scraper or the platform's API
where available.

### Streamer content

Twitch streams. The hub surfaces live streams of team-focused creators
when they are online. Links to the stream. Replays are indexed after the
stream ends.

### Official team content

Press conferences, official interviews, highlights. Linked and credited.
The market does not reproduce the content, it links to it.

## What media integration is not

- Not content production. The hub does not produce podcasts or videos.
- Not exclusive. Podcasts can be listed on other aggregators.
- Not editorial control. The podcast owns its content.
- Not paid placement. The podcast doesn't pay to be listed.

## Failure modes

- **Podcast feed breaks.** The card stops updating. Operator is notified.
- **Podcast goes dark.** The card stays but does not update. Operator can
  delist.
- **Episode is controversial.** Operator can suppress the card in the
  market feed while keeping the podcast listed.
- **Podcast requests removal.** Removed immediately. Logged.

## What media integration does for the market

- **Adds volume.** More content per day without producing more.
- **Adds depth.** The article covers the news. The podcast discusses it.
- **Adds audience.** The podcast's listeners become market readers.
- **Adds revenue.** Referral, live-time, and engagement shares.
- **Adds stickiness.** Readers come back for the podcast threads, not
  just the articles.

## Scaling media

One market might integrate 3–10 podcasts. Across 32 markets, that's
100–300 podcasts. Each podcast brings its own audience. The network
becomes a distribution platform for team-focused audio.

At that scale, the hub can:

- Broker national podcast ad deals
- Cross-promote podcasts across markets
- Offer bundled sponsorships
- Provide shared production tools

These are Phase 3 capabilities. Phase 1 is one market, a few podcasts,
running well.

## What media integration requires from the operator

- Finding the podcasts. The hub doesn't discover them.
- Qualifying them. Team-friendly filter is applied.
- Adding them. RSS feed and revenue terms.
- Managing them. Delist if they fail the filter.
- Moderating their threads. Same as the market's other threads.

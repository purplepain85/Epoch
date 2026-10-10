# 09 — Revenue

Depends on: 02-hub, 08-event-log
Provides:   where money flows, how it's tracked, how the hub is paid
Version:    0.1
Status:     draft

---

## Overview

Money moves through the hub in four directions:

1. From advertisers, to the operator
2. From affiliate networks, to the operator (via the hub)
3. From the operator, to the hub (license and routing fee)
4. From the hub, to the operator (help-back, when applicable)

The hub sits in the middle of exactly one of those flows: affiliate
routing. Everything else moves directly between the operator and their
counterparties.

## The four revenue streams per market

### 1. Affiliate revenue

The operator's market generates affiliate traffic through the hub's
redirector. The network pays the hub. The hub passes the operator's
share through and keeps a routing fee.

Tracking:
- Every click is a `affiliate.click` event
- Every conversion is an `affiliate.conversion` event
- Every payout is a `affiliate.payout` event

Revenue flows:
- Network -> hub (full conversion amount)
- Hub -> operator (conversion amount minus routing fee)
- Hub keeps routing fee

### 2. Ad revenue

The operator runs their own ad accounts — AdSense, Mediavine, Raptive,
or direct advertisers. Revenue lands in the operator's accounts. The
hub does not participate.

Tracking:
- Impressions are logged as `ad.impression` events (aggregated, not
  individual)
- Revenue is logged as `ad.revenue` events (monthly totals, not
  per-impression)

Revenue flows:
- Advertiser -> ad network -> operator
- Hub does not touch this money

### 3. Podcast revenue

Each podcast listed in a market generates revenue through the market's
attribution. The podcast receives a share. The operator receives a
share. The hub receives nothing from this flow.

Tracking:
- Referral clicks: `podcast.click`
- Conversion attribution: `podcast.conversion`
- Podcast share: `podcast.share.paid`
- Operator share: `podcast.share.received`

Revenue flows:
- Marketplace pays operator for podcast-generated traffic
- Operator pays podcast their share (monthly settlement)
- Hub does not touch this money

### 4. Sponsored content

Occasionally, a local advertiser pays the operator directly for a
sponsored post or segment. The operator keeps 100%.

Tracking:
- Sponsored content is logged as `sponsored.published` event
- Payment is logged as `sponsored.paid` event

Revenue flows:
- Advertiser -> operator
- Hub does not touch this money

## What the hub takes

The hub is paid two ways:

### License fee

A flat monthly fee per market. Covers:

- Hosting
- Pipeline runtime
- Event log storage
- Dashboard access
- Support

Range: **$100–$300/month** per market, negotiated at onboarding.

The license fee is billed monthly. The operator pays it directly. It
does not depend on market performance.

### Affiliate routing fee

A percentage of affiliate revenue that routes through the hub. The
hub holds the network relationship. When a conversion happens, the
network pays the hub. The hub keeps a routing fee and passes the rest
through.

Range: **5–15% of routed affiliate revenue.**

The percentage is negotiated at onboarding and stays fixed unless the
operator requests a renegotiation.

## What the hub does not take

- No cut of ad revenue
- No cut of podcast revenue
- No cut of sponsored content
- No cut of affiliate revenue that does not route through the hub
- No upfront fee
- No equity stake

## The operator's economics

For a mid-sized market in-season:

| Source | Monthly | To operator | To hub |
|--------|---------|-------------|--------|
| Affiliate (routed) | $3,000 | $2,700 | $300 |
| Ad revenue | $2,000 | $2,000 | $0 |
| Podcast shares | $800 | $800 | $0 |
| Sponsored content | $500 | $500 | $0 |
| **Totals** | **$6,300** | **$6,000** | **$300** |

Plus the license fee, paid monthly by the operator: $200.

Net to the hub from this market: **$500/month**, or **$6,000/year**.

Across 32 markets at similar volumes: **$192,000/year** to the hub.

## The year-end summary

Even though the hub takes no year-end cut, the hub produces a year-end
summary for each market. It contains:

- Total articles published
- Total comments, re-shares, rants
- Total affiliate clicks and conversions
- Total affiliate revenue, split by operator and hub
- Total ad revenue (from operator's own reporting)
- Total podcast activity
- Total engagement score
- Total moderation actions
- Chain verification result
- Year seal hash

The summary is generated from the event log. It's the market's annual
report.

## Payment mechanics

### License fee

- Billed monthly on the same day
- Paid via card, crypto, or bank transfer
- Automated. No invoice needed after setup.

### Affiliate routing fee

- Networks pay the hub on their standard schedule (NET-30 or NET-60)
- Hub pays the operator within 5 days of receiving payment
- Fee is deducted at payment time
- Every payout is logged as an event

### Help-back

If the market underperformed per the criteria defined at onboarding, the
hub may:

- Waive one or more months of license fee
- Return a portion of the routing fees collected that year
- Extend the buyout window by one year

Help-back is discretionary. It is decided by the hub and communicated to
the operator in writing.

## Tax and compliance

- The operator is responsible for their own taxes on their revenue.
- The hub is responsible for its own taxes on its revenue.
- The hub issues appropriate tax documents for its license and routing
  fees.
- Compliance with sports betting affiliate rules is the operator's
  responsibility in their jurisdiction, though the hub provides
  templates and disclosure requirements.

## Disputes

If the operator disputes the hub's accounting:

- Both sides have access to the event log
- The log is append-only, verifiable, and shared
- Any discrepancy can be traced block by block
- Arbitration terms are defined in the operator agreement

The event log makes most disputes resolvable without escalation. The
math is verifiable.

## What this model is not

- Not a franchise fee (no upfront).
- Not a subscription to a service (a low monthly license is not a
  subscription in the SaaS sense — it's access to infrastructure).
- Not a revenue share on the operator's whole business.
- Not a mandatory spend on any specific affiliate program.

## Why this model is fair

The hub is paid for what it actually provides: a platform, a pipeline,
and affiliate routing. It does not claim a share of the operator's
business, relationships, or reputation.

The operator keeps every dollar they would have earned without the hub,
minus a small routing fee on traffic the hub processed.

Nobody pays upfront. Nobody takes a cut they didn't earn. Both sides
win when the market wins.

## Summary

- Operator keeps: ad revenue, podcast shares, sponsored content,
  affiliate revenue minus routing fee
- Hub keeps: license fee, routing fee
- Nobody pays upfront
- Help-back available for bad years
- Everything auditable via the event log

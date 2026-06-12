# Sources — Cold Outreach Pipeline for B2B SaaS

**Last updated:** June 12, 2026

## Selection criteria

I didn't want 10 people saying the same thing. A cold outreach *pipeline* has distinct stages — targeting, copy, deliverability, follow-up, and measurement — so I selected experts to cover each layer:

- **Practitioners over commentators.** Everyone here runs campaigns, an agency, a tool, or a sales team today. No pure "thought leadership" accounts.
- **Coverage of the full pipeline**, not just copywriting (the most over-represented angle online).
- **Cross-validation.** Several of these experts cite or build on each other's frameworks (e.g., Jason Bay's REPLY Method and Will Allred's Above the Line framework are referenced across the space), which signals they're the primary sources, not aggregators.
- **Format mix** so the repo can demonstrate both API-based collection (YouTube transcripts) and manual curation (LinkedIn posts, newsletters).

## The experts

### 1. Eric Nowoslawski — Outbound systems & AI-powered GTM
- **Role:** Founder, Growth Engine X (outbound agency; clients include Notion, Intercom, Clay)
- **LinkedIn:** https://www.linkedin.com/in/outboundphd/ · **YouTube:** Clay/outbound build tutorials
- **Why:** The reference point for modern, AI-assisted outbound at scale. Posts daily on LinkedIn about cold outbound architecture, runs campaigns at massive volume, and publishes detailed system breakdowns. If a playbook gets built from this research, his content is the backbone of the "systems" chapter.
- **Angle covered:** campaign architecture, data enrichment, AI personalization at scale.

### 2. Jason Bay — Outbound strategy & rep training
- **Role:** CEO, Outbound Squad
- **LinkedIn:** https://www.linkedin.com/in/jasondbay/ · **Site/Podcast:** https://outboundsquad.com
- **Why:** 15+ years selling and training SDR/AE teams at companies like Gong, Zoom, and Rippling. Creator of the REPLY Method for cold email. His content bridges strategy and what reps actually say.
- **Angle covered:** messaging frameworks, call+email orchestration, team-level outbound.

### 3. Armand Farrokh & Nick Cegelski — Tactical sales (podcast)
- **Role:** Hosts, 30 Minutes to President's Club
- **Site:** https://www.30mpc.com · **YouTube:** full episodes with transcripts available
- **Why:** The most-cited tactical sales podcast in B2B. Long-form interviews with top performers produce high-signal transcripts — ideal for the API-collection part of this project.
- **Angle covered:** tactical execution across the whole pipeline, multiple practitioner voices per episode.

### 4. Josh Braun — Cold email copy & buyer psychology
- **Role:** Founder, Sales DNA
- **LinkedIn:** https://www.linkedin.com/in/josh-braun/
- **Why:** The strongest voice on low-pressure, curiosity-driven cold messaging. Creator of the 5-T framework (Trigger, Think, Tell, Third-party, Talk). His post archive is essentially a copywriting course.
- **Angle covered:** first-touch copy, psychology of why prospects ignore or reply.

### 5. Will Allred — Data-driven email copy
- **Role:** Co-founder, Lavender (lavender.ai) — LinkedIn Top Sales Voice
- **LinkedIn:** https://www.linkedin.com/in/williamallred/ · **Site:** https://www.lavender.ai
- **Why:** His advice is grounded in aggregate data from millions of analyzed sales emails, not anecdotes. Creator of the Above the Line framework. The empirical counterweight to pure-craft copywriting advice.
- **Angle covered:** what actually correlates with replies (length, structure, mobile optimization).

### 6. Jed Mahrle — Prospecting systems for individual reps
- **Role:** Founder, Practical Prospecting (newsletter, 30,000+ sales subscribers) — ex-PandaDoc outbound
- **LinkedIn:** https://www.linkedin.com/in/outboundsales/ · **Newsletter:** https://jed.substack.com · **Podcast:** Practical Prospecting
- **Why:** Publishes weekly, hyper-tactical plays (e.g., finding competitors' customers for hyper-relevant outreach). His newsletter archive is a goldmine for the /other folder.
- **Angle covered:** repeatable weekly prospecting workflows, list-building tactics.

### 7. Jeremy Chatelaine — Deliverability & infrastructure
- **Role:** Founder, QuickMail — co-host, Cold Outreach Podcast
- **Site:** https://quickmail.com (blog + podcast)
- **Why:** Over a decade focused on the least glamorous, most decisive layer of the pipeline: actually landing in the inbox. Publishes teardowns and deliverability frameworks based on real sending volume.
- **Angle covered:** domain setup, warm-up, inbox placement, sending infrastructure.

### 8. Patrick Dang — Outbound fundamentals (YouTube-first)
- **Role:** International sales trainer, ex-Oracle — has trained 100,000+ students across 150+ countries
- **YouTube:** https://www.youtube.com/channel/UCLOzkJ9W9fntCGyYfUwMPew · **LinkedIn:** https://www.linkedin.com/in/patrickdangofficial/
- **Why:** The strongest structured, beginner-to-advanced video curriculum on cold outreach. Dense video catalog = ideal source for transcript collection via API.
- **Angle covered:** fundamentals, list building, follow-up sequences, copy breakdowns.

### 9. Jay Feldman ("LeadGen Jay") — Cold email at scale with AI (YouTube-first)
- **Role:** Founder, Otter PR (Inc. 5000) — YouTube channel with 80K+ subscribers focused on cold email systems
- **Site:** https://leadgenjay.com · **YouTube:** "Lead Gen Jay" channel
- **Why:** Publishes frequent, current videos on high-volume AI-assisted cold email — the practitioner's view of the same systems Nowoslawski architects. Scaled his own agency with the exact strategies he teaches, and his recent upload cadence makes him a strong source for *2026-current* tactics. Note: his content frequently promotes his own courses and services, so I filter for tactical substance and cross-check claims against the other sources in this list.
- **Angle covered:** tooling walkthroughs, volume strategies, AI personalization in practice.

### 10. Becc Holland — Personalization at scale
- **Role:** Founder & CEO, Flip the Script
- **LinkedIn:** https://www.linkedin.com/in/beccholland-flipthescript/ · **Company:** https://www.linkedin.com/company/flip-the-script
- **Why:** Built her reputation on solving the core tension of outbound: personalization vs. volume. Her frameworks for relevance (not just personalization) round out the targeting/messaging layer.
- **Angle covered:** prospect research, relevance frameworks, multichannel touches.

## Collection methodology

- **YouTube transcripts:** collected programmatically with a Python script (`/scripts/get_transcripts.py`) using the `youtube-transcript-api` library. One markdown file per video with metadata (author, title, date, URL).
- **LinkedIn posts:** collected **manually** (copy + link + date, organized per author). I deliberately chose not to scrape LinkedIn: it violates LinkedIn's Terms of Service and risks account restriction. Manual curation also forces a quality filter — only high-signal posts make it into the repo.
- **Newsletters & podcasts:** public archive posts and episode transcripts saved to `/research/other/` with source links.

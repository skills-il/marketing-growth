---
name: israeli-product-launch
description: Plan and execute product launches targeting the Israeli tech market, including media outreach, VC demo day preparation, and community engagement. Use when user asks about launching a product in Israel, pitching Israeli media, Hebrew press releases, or asks about "hashkaa", "hasakat mutzar", "Geektime", "Calcalist", Israeli tech PR, or startup launch strategy. Covers Israeli tech media outlets, holiday timing, 8200 alumni networks, and early-adopter communities. Do NOT use for general global product launches, non-Israeli markets, or paid advertising campaigns.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex. Network access helpful for media research.
---


# Israeli Product Launch

## Instructions

### Step 0: Clear the Israeli Compliance Gate Before Anything Ships
Every later step in this skill creates a legal obligation: Step 6 builds a contact list, Step 5 and Step 7 write public claims, and the landing page they all point at is a service under Israeli law. Close these before the first message goes out. This is an orientation checklist, not legal advice, and none of it substitutes for an Israeli lawyer on a launch with real exposure.

1. **Consent before any bulk send.** Israel's anti-spam rules ("Chok HaSpam", Section 30A of the Communications (Telecommunications and Broadcasts) Law) make commercial messaging opt-in: you need prior consent, the message must identify itself as advertising and identify the sender, and it must carry an opt-out in the same channel it arrived on. The law's listed media are fax, SMS, email and automated dialling systems. **That list is not a safe harbour for newer messaging apps.** A bulk WhatsApp or Telegram broadcast to a launch list is the single biggest send in this whole playbook, and the safe working assumption is that the same gate applies to it: consent, self-identification, and an opt-out in that same app. Do not reason from the enumerated media that a WhatsApp blast falls outside the rules. A court may award up to NIS 1,000 per advertisement sent without prior consent, with no need to prove damage, and the awards accumulate across a list. The statute does carry a narrower route for someone who already transacted or negotiated with you and was told they may refuse, but the conditions on it are specific: do not assume it covers a signup list, and have a lawyer confirm it before relying on it. A one-to-one pitch to a named journalist about a news story is a different thing from a broadcast to a prospect list; do not let the second hide behind the first.
2. **Never harvest a list from a group.** Lifting emails or phone numbers out of a Facebook, WhatsApp or Telegram group into a marketing list has no consent behind it and also breaks the platform's own terms. This is the single most likely way a founder following a community-outreach playbook ends up with a claim. The platform side bites faster than the legal side: WhatsApp's business messaging rules prohibit unsolicited promotional messaging, and mass-adding numbers to a group or broadcast list can get the number banned outright, which takes the founder's support channel down in the middle of the launch.
3. **Privacy notice live before the first signup.** A waitlist, a beta form or a launch mailing list is a personal-data database under the Protection of Privacy Law as amended by Amendment 13 (in force August 2025), which expanded the Privacy Protection Authority's enforcement powers. Publish a Hebrew privacy notice, capture marketing consent separately from the terms checkbox, and have a deletion path.
4. **Accessibility on the page you are driving traffic to.** An Israeli public-facing website is treated as a service under the Equal Rights for Persons with Disabilities service-accessibility regulations, which carry a conformance duty and a published accessibility statement. The applicable standard version, the size thresholds and the exemptions change, so look them up against the Commission for Equal Rights of Persons with Disabilities rather than quoting a number from memory. What is not in doubt is that accessibility demand letters arrive at newly launched Israeli sites, so do not launch a Hebrew landing page that has never been checked.
5. **Prices as Israeli consumers must see them.** Consumer-facing prices are shown in NIS as the final price including VAT (18% since 1 January 2025). "Early-bird pricing in NIS" in Step 6 means VAT-inclusive.
6. **Substantiate every claim in the copy.** The Consumer Protection Law's prohibition on misleading a consumer reaches advertising and pre-contract statements. Every number in the Hebrew release, the LinkedIn post and the landing page should trace to something internal you could show. Superlatives ("the first in Israel", "cuts costs by half") are where launch copy actually gets a company in trouble.

### Step 1: Assess Launch Timing Around Israeli Calendar
Israeli holidays and cultural rhythms heavily impact launch success:

| Period | Hebrew | Recommendation |
|--------|--------|----------------|
| Rosh Hashana - Yom Kippur (Sep-Oct) | ראש השנה - יום כיפור | AVOID: Country shuts down 2-3 weeks |
| Sukkot (Oct) | סוכות | AVOID: Extended holiday, low attention |
| Post-holidays (Nov) | אחרי החגים | BEST: Fresh energy, budget planning season |
| Hanukkah (Dec) | חנוכה | OK: Light holiday, consumer spending up |
| Passover (Mar-Apr) | פסח | AVOID: Week-long break, pre-holiday rush |
| Yom HaShoah (Apr-May) | יום השואה | HARD NO: national mourning day |
| Yom HaZikaron (Apr-May) | יום הזיכרון | HARD NO: national mourning day, ends at nightfall |
| Independence Day (Apr-May) | יום העצמאות | OK once Yom HaZikaron has ended, not before |
| Summer (Jul-Aug) | קיץ | MIXED: Many on vacation, but tech stays active |
| Q1 (Jan-Feb) | רבעון 1 | GOOD: New year budgets, fresh start |

Guidelines:
1. Check the Hebrew calendar for exact holiday dates (they shift yearly)
2. Plan launch 2-3 weeks after major holiday clusters
3. Israeli work week starts Sunday (yom rishon) -- launch Sunday or Monday
4. Avoid Friday afternoon (erev Shabbat) for any announcements
5. Post-Rosh Hashana (November) is the prime Israeli launch window
6. **Yom HaShoah and Yom HaZikaron are no-announce days, not merely low-attention days.** Broadcast moves to mourning programming and Israeli brands suspend campaigns; a launch post on either day reads as a serious misjudgement rather than bad timing. Yom HaZikaron runs into Yom HaAtzmaut at nightfall, so an "Independence Day" slot must be dated from that transition, not from the calendar day.
7. **Check the security calendar, not just the religious one.** Since late 2023, large-scale reserve-duty (miluim) call-ups and security escalations have rivaled the holiday calendar as a launch-timing risk: they pull founders, engineers, and journalists away for weeks, and Home Front Command (Pikud HaOref) restrictions can cancel in-person demo days and meetups overnight. Before locking a date, check for an active large-scale call-up or escalation, and keep a contingency to shift to a digital-only launch or postpone in-person events. The Hebrew calendar (hebcal) does not cover this.

### Step 2: Map Israeli Tech Media Landscape
Identify target publications and their pitch preferences:

Verify each outlet is still publishing before you pitch it, the same way Step 3 tells you to verify each accelerator. This table was last checked in August 2026, and this skill has already shipped dead routes in both directions: Geektime's English edition went away, and a sibling skill was still recommending NoCamels after it had ceased operations. An outlet that has quietly stopped publishing looks identical to one that is ignoring you.

| Outlet | Focus | Language | Best For |
|--------|-------|----------|----------|
| Geektime | Startups, tech | Hebrew | Early-stage, product launches |
| Calcalist Tech | Business + tech | Hebrew | Funding rounds, established startups |
| Globes Tech | Business + tech | Hebrew | Enterprise, B2B, financial tech |
| TheMarker | Economy + tech | Hebrew | Market analysis, larger companies |
| CTech (Calcalist) | Israeli tech | English | International audience, dominant English-language Israeli tech outlet |
| Walla Tech | Consumer tech | Hebrew | Consumer products, mass market |

CTech (`https://www.calcalistech.com`) is now the primary English-language outlet for Israeli tech news. The standalone "Geektime English" edition is defunct, so route English-language pitches to CTech.

Pitch guidelines:
1. Hebrew outlets expect Hebrew pitches (not translated English)
2. Lead with the Israeli angle: founders, R&D center, local impact
3. Exclusive stories get better placement than mass press releases
5. **Outreach is relationship-driven, not form-driven.** A warm intro or a direct WhatsApp/email to a specific named reporter lands far better than a website contact form, which mostly goes unanswered. Build (or borrow, via an agency, see Step 9) a personal contact at the target desk in advance, that relationship is the real channel.
6. **Say the quiet part before building a media-first plan.** The Hebrew national tech desks overwhelmingly cover money and named logos: funding rounds, exits, M&A, layoffs, enterprise deals. A pre-funding product launch with no round and no named customer usually gets no national coverage, whatever the pitch quality. If that is the founder's situation, tell them so up front and shift the weight of the plan onto LinkedIn (Step 7), communities (Step 6), newsletters, podcasts and customer-led content, with media as upside rather than the spine.
7. Consult `references/tech-media.md` for detailed pitch templates and timing

### Step 3: Prepare Israeli VC Demo Day Materials
Israeli VC demo days follow specific conventions:

Demo day calendar (confirm each program is still running for the current year, the Israeli accelerator landscape shifts):
- **8200 EISP (8200 for Startups)** -- Active nonprofit accelerator, run in numbered batches out of Ramat Gan. The strongest recurring anchor. Its own site publishes neither cohort months nor a dated Demo Day, and as of August 2026 the current batch's registration is closed with the only open call being a pre-registration form for a future year. Read the current batch status on the program page before planning around it, and never assume a cohort window from a previous year.
- **MassChallenge Israel** -- Zero-equity accelerator, listed by MassChallenge as "hybrid programming based out of Jerusalem, Israel", one of its four regions.
- **Startup Nation Finder** -- Not an event, but the canonical database for finding active investors, programs, and demo days; especially useful since Startup Nation Central's February 2026 restructuring, which cut roughly 65 of its 80 staff and refocused the organisation on innovation diplomacy with a smaller team.

Two dead routes, verified August 2026, do not pitch them:
- **Techstars Tel Aviv** -- Techstars' current accelerator list contains no Israel program. (It does still run London and Tokyo, so this is an Israel exit, not a US-only consolidation.)
- **TheHive by Gvahim** -- `thehive.org.il` no longer resolves, and Gvahim's own site now lists only career and employment programs, with no accelerator, entrepreneurship track, or demo day.

Two programs are frequently mis-described as Israeli demo-day routes and are not: **Google for Startups** is a live global program, but the physical Campus Tel Aviv is gone (`campus.co` now redirects to `startup.google.com`, which lists no Israel location); **Microsoft for Startups** is a global self-serve credits and tooling program, with no Israel cohort or showcase to prepare for.

Pitch conventions for Israeli audiences:
1. Keep pitches to 5-7 minutes (Israelis value directness -- "dugri")
2. Lead with traction and numbers, not vision
3. Address the "why Israel" angle for international investors
4. Include military/intelligence background if relevant (8200, Unit 81, Mamram)
5. Budget slide: show amounts in both USD and NIS
6. Hebrew pitches are acceptable for local VCs; English for international events

### Step 4: Leverage 8200 and IDF Alumni Networks
Israeli military alumni networks are powerful launch channels:

| Network | Size | Access | Best For |
|---------|------|--------|----------|
| 8200 Alumni (Shmone Matayim) | 14,000+ | Alumni events, LinkedIn | Tech/cyber products |
| Mamram Alumni | 5,000+ | Facebook groups, meetups | Software/dev tools |
| Talpiot Alumni | 1,000+ | Exclusive network | Deep tech, academic |
| IDF Veterans Network | Broad | Various platforms | General awareness |

Engagement strategy:
1. Identify founders or team members with unit affiliations
2. Request introductions through shared service connections
3. Present at alumni-specific tech events and meetups
4. Use LinkedIn to connect with relevant unit alumni groups
5. Frame product relevance to the network's technical domain
6. Unit affiliation is a credibility signal, not a free one: service details for some units are not publicly disclosable, so let the person whose service it is decide what goes in the copy.

The 8200 figure is the number EISP's own program page publishes. The other network sizes are working estimates, not published counts, so treat them the way Step 6 treats community sizes and verify before planning reach around them.

### Step 5: Draft Hebrew Press Release
Hebrew press releases follow specific formatting conventions:

Structure:
1. **Headline (koterret):** Max 15 words, active voice, include key numbers
2. **Sub-headline (tat-koterret):** One sentence expanding on the headline
3. **Opening paragraph:** Who, what, when, where -- the core announcement
4. **Quote paragraph:** Founder or CEO quote in first person
5. **Details section:** Product features, market context, Israeli relevance
6. **Company boilerplate ("al ha-chevra", על החברה):** Standard company description
7. **Contact info:** PR contact with Israeli phone number (+972)

Hebrew press release tips:
1. Write natively in Hebrew, do not translate from English
2. Use formal Hebrew (lashon gvoha) for the body, conversational for quotes
3. Include NIS amounts alongside USD for Israeli media
4. Reference Israeli customers, partners, or market data
5. End with "le-fartim nosafim" (for more details) + contact information

### Step 6: Activate Israeli Early-Adopter Communities
Target communities where Israeli tech early adopters gather:

| Community | Platform | Size | Focus |
|-----------|----------|------|-------|
| Israeli Tech Startups | Facebook | 50,000+ | General startup discussion |
| Startup Israel | Facebook | 30,000+ | Founders and investors |
| Tech Careers Israel | Facebook | 100,000+ | Tech professionals |
| Frontend Israel | WhatsApp/Slack | 5,000+ | Frontend developers |
| DevOps Israel | Telegram | 3,000+ | DevOps practitioners |
| Israel Product Managers | Facebook | 15,000+ | Product community |
| Meetup.com Tel Aviv | Meetup | Various | In-person tech events |

Engagement approach:
1. Share value-first content before promotional posts
2. Offer Israeli-specific beta access or early-bird pricing in NIS
3. Post in Hebrew with English technical terms where natural
4. Engage in existing discussions before self-promoting
5. Offer to present at local meetups (Tel Aviv, Herzliya, Raanana tech hubs)

Community-size figures shift over time. Treat any subscriber count as a starting estimate and verify the current size on the group page before relying on it for reach planning.

Weight the plan by where the conversation actually is, not by headline membership. Israeli tech discussion has shifted substantially onto WhatsApp groups and Communities, Telegram channels, and per-stack Slack and Discord workspaces; the large Facebook groups still have real membership but far lower engagement per member than their size implies. Ask the founder which invite-gated groups they or their team are already in, since those are the ones that convert, and do not build the community plan out of Facebook alone.

### Step 7: Run a Founder-Led LinkedIn Launch
As of 2026, LinkedIn is a primary organic distribution channel for Israeli B2B and founder launches. A founder post often outperforms a company-page post for reach.

Launch post approach:
1. Post from the founder's personal profile, not (only) the company page. Founder posts are widely reported to out-reach company-page posts. LinkedIn does not publish its ranking mechanics, so treat this and the other reach heuristics in this step as practitioner consensus, not documented behaviour, and never quote them to a client as a LinkedIn rule.
2. Write two versions: Hebrew for the local network, English for international investors and customers. Pick the version that matches the primary audience for that post; some founders post both, spaced a day or two apart.
3. Open with a personal story or the problem, not a product announcement. Save the link or CTA for a comment or the end of the post.
4. Employee amplification, within the rules: tell the team the post is live and let them respond if they have something real to say. LinkedIn's Professional Community Policies state "Don't do things to artificially increase engagement with your content. Respond authentically to others' content and don't agree with others ahead of time to like or re-share each other's content." A rota of pre-agreed first-hour comments, an engagement pod, or identical copy-paste comments is what that sentence prohibits. Comments are commonly reported to carry more distribution weight than reactions, but that is practitioner analysis, not a published figure, and it is not a licence to manufacture them.
5. Timing: post Sunday to Tuesday morning, Israel time, to match the start of the local work week. Avoid Friday and Saturday.
6. Tag investors, partners, or design partners only when genuinely relevant. Irrelevant tagging annoys the people tagged and is widely reported to hurt reach; LinkedIn does not publish a tag penalty, so the durable reason is the first one.

### Step 8: Coordinate a Product Hunt or Global Launch Day
Many Israeli startups run a Product Hunt launch alongside local press. The two need to be sequenced so they reinforce each other instead of competing.

Coordination guidance:
1. Product Hunt's ranking day runs on US Pacific time (a launch "day" starts at 00:01 PT). Plan for the PH day to span parts of two Israel-time calendar days.
2. Set the Israeli media embargo to lift the same morning the PH launch goes live, so Hebrew coverage and the PH page point at each other.
3. Give an Israeli outlet (Hebrew exclusive) and CTech (English) the story under embargo a few days ahead; brief them that the PH launch is part of the same news beat.
4. Share the launch with the Israeli community (Step 6) and the founder's LinkedIn network (Step 7) during PT daytime, which is Israel evening. **Never ask for upvotes.** Product Hunt's own launch guide is explicit: "You can share your launch link however you wish. The only real rule here is that you cannot ask people directly to upvote your product. Instead, ask them to visit and comment." An agent drafting a WhatsApp or LinkedIn message from "mobilise the community" will write the prohibited version by default, so write the ask as "come see it and tell us what you think", in Hebrew too.
5. Avoid launching on a Friday or during a Hebrew-calendar holiday cluster (Step 1) even if the PH calendar slot looks open.

### Step 9: Decide DIY vs PR Agency
Israel has a deep bench of boutique PR agencies that specialize in tech and startups, and using one is a common norm rather than an exception.

Decision guidance:
1. DIY works when the founder already has Israeli media relationships, the story is straightforward (a feature or a small round), and budget is tight.
2. A boutique PR agency is worth it for a major milestone (large funding round, exit, category-defining launch), when you need embargoed exclusives placed fast, or when no one on the team has press contacts.
3. Boutique agencies in Israel typically work on a monthly retainer; one-off launch projects are also available. Get a clear scope (which outlets, Hebrew vs English, how many pitches) before signing.
4. Even with an agency, the founder still writes or heavily edits quotes. Israeli journalists can tell agency-templated quotes from authentic founder voice.

## Examples

### Example 1: B2B SaaS Launch in Israel
User says: "I'm launching a B2B SaaS product for Israeli businesses next month"
Actions:
1. Check: November timing is excellent (post-holidays)
2. Map: Target Geektime for product story, Calcalist for business angle
3. Prepare: Hebrew press release with NIS pricing
4. Activate: Post in the invite-gated WhatsApp and Slack groups the team is already in, then the large Facebook groups
5. Network: Leverage team's 8200 connections for introductions
Result: Complete Israeli launch plan with media list, press release template, and community outreach strategy

### Example 2: Demo Day Preparation
User says: "We're presenting at an Israeli VC demo day next week"
Actions:
1. Structure: 5-minute pitch with traction-first approach
2. Localize: Include NIS figures alongside USD, mention Israeli customers
3. Network: Identify attending VCs and their portfolio focus
4. Follow-up: Prepare Hebrew one-pager for post-demo distribution
Result: Concise Israeli-style pitch deck with local market data and follow-up materials

### Example 3: Hebrew Press Release
User says: "Write a press release for our funding round for Israeli media"
Actions:
1. Format: Hebrew press release structure with koterret and tat-koterret
2. Localize: Convert USD to NIS, add Israeli market context
3. Quote: Draft CEO quote in natural Hebrew
4. Target: Calcalist Tech for funding stories, CTech for English version
Result: Dual-language press release pair ready for Israeli and international media

## Bundled Resources

### References
- `references/tech-media.md` -- Israeli tech media outlet contact patterns and pitch format guidelines. Covers Geektime, Calcalist Tech, Globes Tech, TheMarker, and CTech with preferred pitch formats, editorial calendars, and exclusive vs. mass distribution strategies. Consult when planning media outreach for an Israeli product launch.

## Gotchas

- The Tishrei holiday cluster (Rosh Hashana through Sukkot, September-October) effectively shuts down Israel for 2-3 weeks. Agents may schedule launches during this period without checking the Hebrew calendar, which shifts dates every year.
- Hebrew press releases must be written natively in Hebrew, not translated from English. Israeli tech journalists can immediately tell translated content and will deprioritize it.
- Israeli VC pitches should be 5-7 minutes and lead with traction/metrics, not vision. Agents trained on US pitch conventions may produce longer, vision-first presentations that lose Israeli investor attention.
- WhatsApp follow-ups after media pitches are culturally acceptable and expected in Israel. Agents may suggest only email follow-ups, missing the most effective Israeli outreach channel.
- Israeli tech media outlets (Geektime, Calcalist Tech) expect Hebrew pitches for Hebrew coverage. Agents may draft English pitches for these outlets, which will be ignored.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Geektime | https://www.geektime.co.il | Leading Israeli tech news outlet, PR pitching |
| Calcalist | https://www.calcalist.co.il | Israeli business and tech coverage |
| CTech | https://www.calcalistech.com | Calcalist's English edition, dominant English-language Israeli tech outlet |
| TheMarker | https://www.themarker.com | Israeli business newspaper (Haaretz group) |
| Globes | https://www.globes.co.il | Israeli financial daily, enterprise coverage |
| Start-Up Nation Central | https://www.startupnationcentral.org | Israeli startup ecosystem data and trends |
| Israel Innovation Authority | https://innovationisrael.org.il/en | Grants, programs, ecosystem support |

## Recommended MCP Servers

| MCP Server | Why It Helps |
|------------|--------------|
| `hebcal` | Step 1 timing logic depends on exact Hebrew-calendar holiday dates, which shift every year. The hebcal MCP returns Hebrew holiday and Shabbat dates so launch scheduling avoids the Tishrei cluster, Passover, and other low-attention windows without guesswork. |

## Troubleshooting

### Error: "No media response to pitch"
Cause: Pitch may be in English to Hebrew-language outlets, or lacks Israeli angle
Solution: Rewrite pitch in native Hebrew. Lead with the Israeli connection: local team, Israeli customers, or market-specific data. Consider offering an exclusive to one outlet first.

### Error: "Launch during holiday period"
Cause: Product launch scheduled during Rosh Hashana, Sukkot, or Passover period
Solution: Reschedule to post-holiday window. November (post-Tishrei holidays) and January-February (post-Hanukkah) are optimal. Check Hebrew calendar for exact dates.

### Error: "Low community engagement"
Cause: Promotional content posted without prior community participation
Solution: Spend 2-3 weeks engaging authentically in Israeli tech communities before launching. Share useful content, answer questions, then introduce your product with a value-first approach.

### Error: "VC demo pitch too long"
Cause: Israeli investors expect concise, direct (dugri) presentations
Solution: Cut pitch to 5-7 minutes maximum. Lead with metrics and traction. Remove slides that do not directly support your ask. Israeli VCs will interrupt with questions -- welcome this as engagement.

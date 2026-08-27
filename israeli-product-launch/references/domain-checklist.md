# Domain checklist: Israeli Product Launch

Scope test: a founder says "I'm launching my product in Israel next month." Anything they must
do, or must not do, in that window is in scope. Legal exposure created by the marketing actions
this skill recommends is in scope by definition.

## Must cover

| Item | Why it is core |
|------|----------------|
| Consent basis for every launch list before the first send, with the message identifying itself as advertising, identifying the sender, and carrying an opt-out in the same channel | Section 30A of the Communications (Telecommunications and Broadcasts) Law, the Spam Law. Statutory damages are available with no proof of damage and accumulate across a list. Step 6 and the WhatsApp gotcha create exactly this exposure. |
| Never harvest contacts out of a Facebook, WhatsApp or Telegram group into a marketing list | Same statute (no consent), plus the platforms' own terms. The most likely way a founder following a community playbook creates a claim. |
| Website accessibility conformance and a published accessibility statement before traffic arrives | Equal Rights for Persons with Disabilities service-accessibility regulations. Standard version, size thresholds and exemptions must be looked up per launch, not quoted from memory. |
| Hebrew privacy notice live before the first signup, marketing consent captured separately from the terms checkbox, deletion path | Protection of Privacy Law as amended by Amendment 13, in force August 2025. Every action in a launch playbook creates a database. |
| Claims substantiation in all launch copy; no unsubstantiated superlatives or savings figures | Consumer Protection Law prohibition on misleading a consumer, which reaches advertising and pre-contract statements. This skill writes the copy, so the gate belongs here. |
| Consumer prices displayed in NIS as the final VAT-inclusive price | Consumer Protection Law and the price-marking rules made under it. |
| Hebrew-calendar timing: the Tishrei cluster, Passover, the Sunday-start work week | Already covered. Retained so a rewrite cannot lose it. |
| Yom HaShoah and Yom HaZikaron are no-announce days, and Yom HaAtzmaut is dated from the nightfall transition, not the calendar day | Universal Israeli industry norm: broadcast moves to mourning programming and brands suspend campaigns. A launch post on either day is a reputational incident. |
| Security-calendar check on both the market side and the team side: active call-up or escalation, Home Front Command gathering restrictions, a digital-only contingency, and cover for a founder or engineer called up mid-launch | Since late 2023 this rivals the holiday calendar as a timing risk, and hebcal does not cover it. |
| Product Hunt: share the link, never ask for upvotes | Product Hunt's own launch guide states this as its only real promotion rule. Solicited voting is the default thing an agent writes from "mobilise the community". |
| LinkedIn: no pre-arranged reciprocal engagement, no engagement pods, no rota of first-hour comments | LinkedIn's Professional Community Policies prohibit artificially increasing engagement and pre-agreed liking or re-sharing. |
| Set media expectations before building a media-first plan: without a funding round, exit or named logo, the Hebrew national tech desks usually will not cover a product launch | Visible in this skill's own `references/tech-media.md` coverage-priority table, which is dominated by funding events. |
| Hebrew press release written natively rather than translated; Hebrew pitches to Hebrew outlets; named-reporter, relationship-driven outreach over contact forms | Already covered. Retained as Must. |
| Verify every accelerator, program and outlet is still running before pitching it | This skill has already shipped three dead routes across its history (Techstars Tel Aviv, TheHive by Gvahim, Campus Tel Aviv). The landscape decays faster than the update cycle. |

## Should cover

| Item | Why |
|------|-----|
| Channel mix weighted to WhatsApp groups and Communities, Telegram, per-stack Slack and Discord, and LinkedIn, with the large Facebook groups as a secondary channel | Israeli tech discussion has substantially migrated off Facebook groups. Directionally high confidence; any single named group's current size is not verifiable and must be checked. |
| Arab-Israeli market and calendar for consumer-facing products: Ramadan, Eid al-Fitr, Eid al-Adha, Arabic-language consideration | Roughly a fifth of the population; its absence makes the skill's "Israel" Jewish-Israeli-only. |
| App Store and Google Play lane when the product ships as an app: Hebrew RTL metadata and screenshots, Israeli storefront availability, ILS price tiers, review lead time against a fixed press date, phased release, privacy declarations | Store review is the hard dependency that breaks fixed launch dates. |
| Israeli checkout reality: Bit, local card handling including instalment splitting, a Hebrew tax invoice or receipt, and the VAT-registration consequence of charging Israeli customers | An international-card-only checkout measurably leaks Israeli conversion, and Step 6 already tells the founder to price in NIS. |
| Hebrew landing page and RTL: layout, `.co.il` versus `.com`, Hebrew SEO, Hebrew support response expectations, and whether to localise before demand is validated | The destination of every channel in the plan. |
| A T-minus schedule for a one-month launch | The typical user constraint is "next month", and a step list with no dates does not answer it. |
| Launch measurement: KPIs, a UTM convention, and a stated definition of success | Otherwise the launch cannot be evaluated or repeated. |
| Crisis handling: a hostile group thread, a critical journalist, an escalation beginning after the date is locked, and who speaks | Israeli communities are blunt and fast. |
| Unit-affiliation discretion: military background is a credibility signal, but some service details are not publicly disclosable | Step 4 says "include if relevant" and needs the counterweight. |
| Demo-day and accelerator currency check, and the founder-led LinkedIn and DIY-versus-agency steps | Already covered and verified. Retained so a future edit does not regress them. |

## Out of scope (explicit)

- **Paid acquisition** (Google, Meta, LinkedIn ads, Israeli media buying, influencer fees). Excluded by the description; `israeli-paid-ads` covers it. Reviewed 2026-08-27 and kept out of scope: a founder would plausibly ask, but the answer is a route to the sibling skill rather than a duplicate lane here.
- **NoCamels as an English-language outlet.** Reviewed 2026-08-27. Do NOT add it. NoCamels ceased operations; its own About page records activity from 2011 to 2024 and a pause, and its last post is from October 2024. A reviewer recommended adding it in this cycle and was wrong; this row exists so the next cycle does not repeat it.
- **Fundraising mechanics**: term sheets, valuation, cap table, diligence. Only the demo-day presentation layer is in scope.
- **Incorporation, corporate structure, and Innovation Authority grant conditions.**
- **Israeli employment law and hiring**, including employer obligations toward employees on reserve duty.
- **Tax structuring** beyond the VAT-registration flag.
- **Product and engineering readiness**: load testing, on-call, feature flags.
- **Non-Israeli market launches**, except the Product Hunt sequencing interface.
- **Regulated-sector marketing rules** (health claims, financial promotion, gambling). If the product sits in one of those verticals, stop and route to a regulated-domain review rather than drafting copy.

## Authoritative sources

| Topic | Source | What to check |
|-------|--------|---------------|
| Anti-spam | Kol Zchut, Spam Law page; Communications (Telecommunications and Broadcasts) Law | Consent requirement, listed media, sender identification, opt-out, damages |
| Consumer protection and price display | Consumer Protection and Fair Trade Authority | Misleading-consumer prohibition, final-price display |
| VAT rate | Israel Tax Authority | Current standard rate and digital-services rules |
| Privacy | Privacy Protection Authority; Protection of Privacy Law as amended by Amendment 13 | Notice and consent, controller obligations, enforcement powers |
| Accessibility | Commission for Equal Rights of Persons with Disabilities | Conformance level, accessibility statement, thresholds and exemptions |
| Hebrew calendar | hebcal, and the recommended `hebcal` MCP | Exact holiday dates, which shift yearly |
| Security calendar | Home Front Command guidance; current reserve call-up status | Gathering restrictions affecting in-person events |
| Israeli tech media | geektime.co.il, calcalist.co.il, calcalistech.com, globes.co.il, themarker.com, tech.walla.co.il | Live outlet status, desk focus. Verify before every launch |
| Ecosystem programs and investors | Startup Nation Finder | Currently active accelerators, programs, demo days, investors |
| App stores | App Store Review Guidelines and App Store Connect; Google Play Console policy centre | Review timing, storefront and pricing configuration, privacy declarations |
| Product Hunt | Product Hunt launch guide | Vote-solicitation rule, launch-day mechanics |
| LinkedIn | LinkedIn Professional Community Policies | Authentic-engagement rules |

# Domain coverage checklist: israeli-paid-ads

Scope: paid media buying and optimization for advertisers selling into the Israeli market.
This file states WHAT must be covered and WHERE the authority lives. It deliberately states no
figures, rates, thresholds, character counts or dates: those live in `evidence.json` and the
skill body, and a third copy here would drift.

## Must cover (core)

| # | Requirement | Authority |
|---|---|---|
| M1 | Platform and campaign-type selection across Google Search, Demand Gen, Performance Max, Meta, LinkedIn, TikTok and Israeli native/classifieds inventory | Google Ads Help 13695777; each platform's objective docs |
| M2 | Google Display's migration into Demand Gen and the timetable that invalidates standalone-Display advice | Google Ads Help 13695777 |
| M3 | Hebrew keyword research: root morphology, smichut, definite article, transliteration, English-term search behaviour; Keyword Planner (Israel + Hebrew) as the sourced number path | Google Ads Help 7337243 |
| M4 | Responsive search ad text limits and that Hebrew counts single-width | Google Ads Help 7684791 |
| M5 | Sitelink asset text limit | Google Ads Help 2375416 |
| M6 | Callout asset text limit | Google Ads Help 6079510 |
| M7 | Meta text truncation as placement/device dependent rather than a published cap, with Ads Manager preview as the check | Meta Business Help Center (unreachable at time of writing) |
| M8 | Hebrew register, RTL rendering, mixed Hebrew/Latin/digit reordering, and the preview obligation | Google Ads Help 2404220 |
| M9 | Geographic targeting for Israel, and re-weighting from the campaign's own geo report | Google Ads Help 1722043 |
| M10 | Hebrew-calendar scheduling: Shabbat window, Yom Kippur, moving chagim, pre-chag demand | hebcal.com; Google Ads Help 2404244 |
| M11 | Age-bracket distortion from IDF conscription years | CBS statistical abstract |
| M12 | Israel device split as measured data, and explicit rejection of the unsourced mobile-share folklore | StatCounter, Israel platform share |
| M13 | Israel search-engine share (why Search planning is Google planning) | StatCounter, Israel search share |
| M14 | Consent gate 1, the DATA: Amendment 13 for customer lists, lookalike/Advantage+ seeds and pixel/CAPI remarketing | Privacy Protection Authority |
| M15 | Consent gate 2, the MESSAGE: Spam Law s.30A for contacting captured leads | Communications Law s.30A; kolzchut secondary |
| M16 | Consent gate 3: Google Consent Mode signals for EEA/UK traffic, distinct from Israeli duties | Google Ads Help 13695607 |
| M17 | Restricted targeting, per platform, Google: sensitive interest categories and the advertiser-curated-audience block | Google Ads Policy 143465 |
| M18 | Restricted targeting, per platform, Meta: audience definitions implying sensitive attributes | Meta Advertising Standards |
| M19 | Customer-list upload prerequisites, per platform, Meta: identifier hashing and Custom Audience terms acceptance | Meta Business Help Center (unreachable at time of writing) |
| M20 | Customer-list upload prerequisites, per platform, Google: Customer Match eligibility and policy | Google Ads Help 6379332 |
| M21 | VAT-inclusive price display in ads and on the landing page | Consumer Protection Law 5741-1981 and price-display regulations |
| M22 | Sponsored/native content labeling, including influencer disclosure | Consumer Protection and Fair Trade Authority |
| M23 | Distance-sale cancellation, per transaction type: goods | Consumer Protection Law s.14C; kolzchut secondary |
| M24 | Distance-sale cancellation, per transaction type: one-off service | as M23 |
| M25 | Distance-sale cancellation, per transaction type: continuing service | as M23 |
| M26 | Distance-sale cancellation, per transaction type: tourism service | as M23 |
| M27 | Distance-sale cancellation, per protected cohort: oleh chadash within the teudat-oleh period, person with a disability, person aged 65+ | Consumer Protection Law s.14C1; kolzchut secondary |
| M28 | Category restriction: financial services (risk disclosure, licensing) | Israel Securities Authority; Capital Market Authority |
| M29 | Category restriction: health and medical (no cure claims) | Ministry of Health; professional-advertising rules |
| M30 | Category restriction: alcohol (minor targeting, warnings) | Restriction of Alcohol Advertising Law |
| M31 | Category restriction: gambling and lottery (licensing) | Penal Law; Mifal HaPayis / Sports Betting Board |
| M32 | Category restriction: food (verifiable nutrition and health claims) | Ministry of Health food-labelling regulations |
| M33 | Category restriction: real estate (VAT treatment of new-construction prices) | price-display regulations; Israel Tax Authority |
| M34 | Bidding-strategy inventory INCLUDING which strategies are campaign-type restricted and which were withdrawn | Google Ads Help 2979071, 2459326 |
| M35 | Input-VAT treatment per taxpayer status: osek murshe (reclaims, so it must not enter the ROAS denominator) | VAT Law 5736-1975; Israel Tax Authority |
| M36 | Input-VAT treatment per taxpayer status: osek patur (charges no output VAT, cannot offset) | as M35 |
| M37 | Conditions on the deduction: business use, attribution to a taxable transaction, a proper tax invoice, and the allocation-number requirement with its stepped thresholds | Israel Tax Authority allocation-number guidance |
| M38 | Which entity invoices the advertiser and in what form; the imported-services branch when the invoice is foreign-issued | Israel Tax Authority; platform billing docs |
| M39 | ROAS basis symmetry: the revenue numerator and the spend denominator must share a VAT basis, and the platform optimizes to whatever conversion value is passed | Google Ads Help 1722022 |
| M40 | Conversion measurement as a BUILD step: tag/CAPI install, value and currency, deduplication, offline import for leads, verification before spend | Google Ads Help 1722022 |
| M41 | Hebrew negative-keyword discipline and search-terms-report cadence | Google Ads Help 2453972, 2472708 |

## Should cover (advanced)

| # | Requirement | Authority |
|---|---|---|
| S1 | Arabic-language advertising for Israel's Arabic-speaking market: separate ad groups, Arabic RTL copy, typically less competitive auctions | Google Ads Help 1722078; CBS |
| S2 | Russian-speaking segment as a separate targeting and copy track | Google Ads Help 1722078; CBS |
| S3 | Haredi audience reachability: filtered-internet subscriptions and low mainstream-social penetration mean paid social under-reaches this segment | Ministry of Communications; Israel Democracy Institute |
| S4 | Israeli native buying: which platform each network is bought in and which publishers it reaches | Taboola Realize; Outbrain |
| S5 | Yad2 and classifieds as high-intent local inventory distinct from search | Yad2 advertiser docs |
| S6 | Direct publisher buys and branded content, and the labeling duty that attaches | publisher ad-sales docs; Consumer Protection Authority |
| S7 | Security-situation pacing and brand safety: escalation pauses, alert periods, creative that ages badly | Google Ads Help 2404186; oref.org.il |
| S8 | Account and billing setup: account currency (fixed at creation), payment settings, monthly invoice artefacts finance needs | Google Ads Help 2375433; Meta billing help |
| S9 | Account structure: brand vs non-brand separation, intent tiering, naming that survives handover | Google Ads Help 1704396 |
| S10 | Auction Insights as the post-launch replacement for planning defaults | Google Ads Help 2579754 |
| S11 | Landing-page compliance beyond price, including the Israeli web-accessibility duty (IS 5568) | Equal Rights (Service Accessibility) Regulations |
| S12 | Experiment discipline and the learning period after a bid-strategy change | Google Ads Help 6318732 |
| S13 | Lead Ads to CRM plumbing and offline conversion import | Google Ads Help 2998031; Meta CAPI docs |
| S14 | Dayparting derived from the account's own hour/day report rather than a general peak-hours claim | Google Ads Help 2404244 |
| S15 | Seasonal budget planning against Israeli commercial peaks | hebcal.com; account year-over-year data |
| S16 | Ktiv male / ktiv haser and sofit normalization as a second axis of Hebrew query variance | practitioner; validate in Keyword Planner |

## Out of scope (explicit)
Each row states the question and its answer. Reviewed 2026-08-27.

- **"Will this write my organic social posts?"** No. Paid placements only; organic social has different metrics and no ad-review step. Covered by a separate skill.
- **"Will this rank my site in Google?"** No. SEO is out of scope. The only overlap is landing-page quality as a Quality Score input; the skill treats the landing page as an ad asset.
- **"Can I use this to send the email or SMS to the leads I collected?"** No. The skill states that the Spam Law gate exists and that consent to hold data is not consent to message (M15), and stops there. `israeli-email-sequences` covers the send.
- **"Can I run my US or EU campaigns with this?"** No, except the Consent Mode item (M16), which exists precisely because Israeli advertisers often also serve EEA/UK traffic. Everything else assumes Israeli law, Israeli VAT and the Hebrew calendar.
- **"Does this give me real Israeli CPC and CPM benchmarks I can quote a client?"** No, and this is stated at the point of use, not just here. There is no published Israeli benchmark dataset. The tables rank verticals; the sourced number is a Keyword Planner forecast for your own keywords, then your own post-launch data.
- **"Is this legal advice on Amendment 13, the Consumer Protection Law or my VAT position?"** No. The skill flags where a duty attaches and names the authority. It is not a substitute for a privacy lawyer or your accountant, and the VAT sections state a mechanism, not a ruling on your file.
- **"Will it log into my ad accounts and launch the campaign?"** No. There is no API integration. The skill produces the plan, copy, negative lists and checks; a human executes.
- **"Does it cover TV, radio, outdoor or print?"** No. Offline media carry a separate regulator and buying process.
- **"Does it cover ASO or affiliate networks?"** No. App campaigns are named as a campaign type under M1, but ASO is `israeli-aso` and affiliate/CPA management is a separate discipline.
- **"Does it tell me how to get an ad approved after a rejection?"** Only by pointing at the policy that was breached. The skill never advises restructuring an ad, account or audience to avoid review, rate limits or enforcement. Permanently out of scope.

## Authoritative sources
Google Ads Help: 7684791 (RSA), 2375416 (sitelink), 6079510 (callout), 13695777 (Demand Gen),
2979071 (automated bidding), 2459326 (Smart Bidding), 13695607 (consent mode EEA), 1722022
(conversion tracking), 1722043 / 1722078 (location and language), 6379332 (Customer Match),
2404244 (ad scheduling), 2404186 (content suitability), 2579754 (auction insights).
Google Ads Policy: 143465 (restricted targeting in personalized advertising).
Meta: transparency.meta.com/policies/ad-standards/, facebook.com/business/help.
StatCounter Israel: search share and platform share.
Israel: Privacy Protection Authority, Israel Tax Authority, Consumer Protection Law 5741-1981
and its regulations, Communications Law s.30A, kolzchut.org.il (secondary Hebrew explainer).
Native: ads.realizeperformance.com, my.outbrain.com. Calendar: hebcal.com.

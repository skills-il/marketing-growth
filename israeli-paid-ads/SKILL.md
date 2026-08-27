---
name: israeli-paid-ads
description: Create and optimize paid advertising campaigns for the Israeli market across Google Ads, Meta (Facebook/Instagram), and Israeli platforms (Taboola, Outbrain, Yad2, publisher networks). Use when user asks about Israeli PPC, Hebrew ad copy, Israeli audience targeting, or ad budget optimization. Covers Hebrew keyword research, Israeli Consumer Protection Law ad regulations, Amendment 13 consent rules for ad targeting, local bidding strategies, and audience segmentation. Do NOT use for organic social media, SEO, email marketing, or non-Israeli ad markets.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Israeli Paid Ads

## Instructions

### Step 1: Choose Platform and Campaign Type

Select the right platform based on business type, audience, and campaign objective. Each platform serves a different role in the Israeli digital ad ecosystem.

| Platform | Best For | Israeli Audience | Avg CPM (NIS) | Ad Formats |
|----------|----------|------------------|---------------|------------|
| Google Ads (Search) | High-intent traffic, lead gen | 98.17% search market share in Israel (StatCounter, July 2026) | N/A (CPC model) | Text ads, responsive search ads |
| Google Ads (Display) | Brand awareness, retargeting | Google Display Network reach in IL | 5-15 | Banner, responsive display |
| Meta (Facebook) | B2C, community, local business | ~7.6M Israeli users | 15-40 | Image, video, carousel, collection |
| Instagram | Lifestyle, fashion, food, travel | ~5M Israeli users | 20-50 | Stories, reels, feed, shopping |
| LinkedIn | B2B, SaaS, enterprise, recruiting | ~3M Israeli professionals | 40-120 | Single image / document / video ads, Sponsored Messaging (Message and Conversation ads), Lead Gen Forms. "InMail" is retired as ad terminology, the messaging product is Sponsored Messaging |
| TikTok | Gen Z, viral content, brand awareness | Growing Israeli user base (18-34) | 10-30 | In-feed video, branded effects |

The audience sizes and CPM bands here are practitioner estimates with no published source; only the Google search-share figure is sourced (StatCounter). Rank platforms with them, do not build a media plan on them. Pull real CPMs from each platform's forecasting tool.

**Campaign type selection guide:**

- **Lead generation**: Google Search Ads (high intent) or Meta Lead Ads (lower cost per lead, lower intent)
- **E-commerce sales**: Google Shopping + Meta Dynamic Product Ads (DPA)
- **App installs**: Meta App Install campaigns or Google App campaigns (UAC)
- **Brand awareness**: YouTube pre-roll, Meta reach campaigns, TikTok
- **Local business**: Google Local campaigns, Meta radius targeting around the business

Recent Google campaign-type changes: Discovery campaigns and Video Action campaigns have been folded into **Demand Gen**.

**Google Display is being folded into Demand Gen too, and this invalidates the Display row above on a published timetable.** Google states that Display Ads campaigns are moving to Demand Gen as the Google Display Network, that from June 2026 eligible advertisers can voluntarily migrate existing campaigns with an in-account migration tool, and that later new campaigns will only be creatable within Demand Gen with remaining campaigns migrated automatically. Plan new Display work as Demand Gen. Demand Gen serves YouTube (including Shorts), Discover, Gmail, Maps, and the Display Network, so it reaches a local-search surface standalone Display never did.

Standalone **Call ads** appear to be on the way out in favour of responsive search ads with call assets, but we could not confirm a deprecation date on any official Google page, so do not quote one. Build call campaigns as responsive search ads with call assets regardless, which is the configuration Google documents.
- **B2B**: LinkedIn Sponsored Content + Google Search for branded/non-branded terms

**Israeli publisher and native networks:** Taboola (via Realize at `ads.realizeperformance.com`), Outbrain Direct Response (a Teads subsidiary, bought at `my.outbrain.com`), Yad2 for high-intent local classifieds, and direct buys with Ynet, Walla and Globes. Taboola and Outbrain remain separate competitors. Details in `references/israeli-ad-regulations.md`. Israeli-platform campaigns are still subject to the VAT-inclusive pricing and labeling rules in Step 5.

### Step 2: Hebrew Keyword Research

Hebrew is a morphologically rich language with root-based word formation. A single root (shoresh) produces dozens of inflections, and keyword tools may not group them automatically. Thorough keyword research requires covering all variants.

**Hebrew morphology considerations:** a single root produces many inflections that keyword tools do not group for you: verb conjugations, noun forms, construct state (smichut), with and without the definite article, and colloquial spellings. The worked table is in `references/israeli-ad-regulations.md` under "Hebrew keyword morphology". Cover the variants deliberately; missing one silently forfeits its search volume.

**Keyword research process:**

1. **Seed keywords**: Start with 5-10 core terms in Hebrew. Include both formal and colloquial forms. Many Israelis search in English for tech terms (e.g., "CRM" not "ניהול קשרי לקוחות").
2. **Expand with Google Keyword Planner**: Set location to Israel, language to Hebrew. Export suggestions and group by intent (informational, commercial, transactional).
3. **Check English variants**: Israeli users frequently search in English or transliterated Hebrew (e.g., "ramzor" for רמזור). Add these as separate ad groups.
4. **Negative keywords in Hebrew**: Build a negative keyword list early. Common Hebrew negatives: "חינם" (free), "מה זה" (what is), "השוואה" (comparison, if not relevant).
5. **Competitor analysis**: Search your main keywords on google.co.il and note which competitors are bidding. Check their ad copy for messaging angles you can differentiate from.

**Tools:** Google Keyword Planner (region Israel, language Hebrew) is the sourced number path; Google Trends for Hebrew-vs-English volume; Search Console for existing query data; Ahrefs/Semrush for competitor gaps (limited Hebrew support).

### Step 3: Write Hebrew Ad Copy

Hebrew ad copy requires attention to character limits, RTL formatting, register, and cultural norms. Israeli consumers respond well to direct, informal communication with clear pricing.

**Google Ads character limits (apply equally to Hebrew):**

| Element | Character Limit | Hebrew Tip |
|---------|----------------|------------|
| Headline 1-15 | 30 chars each | Hebrew words are shorter on average, giving more room |
| Description 1-4 | 90 chars each | Use informal register, include NIS pricing |
| Display URL path | 15 chars each | Use Hebrew slugs: /ביטוח-רכב |
| Sitelink title | 25 chars | Short Hebrew CTAs: "קבלו הצעה", "צרו קשר" |
| Callout | 25 chars | "משלוח חינם", "אחריות שנתיים" |

**Hebrew ad copy best practices:**

1. **Use informal register (guf sheni)**: Address the reader as "אתה/את" not "אתם". Israeli ads use casual, direct language. Example: "מחפש ביטוח רכב? קבל הצעת מחיר תוך דקה" (not "המעוניינים בביטוח רכב מוזמנים...").
2. **Include prices with VAT**: Israeli law requires all advertised prices to include 18% VAT. Always show the final price in NIS. Example: "החל מ-99 ש\"ח לחודש (כולל מע\"מ)".
3. **Add local trust signals**: "חברה ישראלית", "שירות בעברית", "משלוח בכל הארץ", phone number with Israeli prefix (0X-XXXXXXX or *number).
4. **Use phone extensions**: Israelis prefer calling businesses directly. Add call extensions with local numbers. Click-to-call performs well on mobile.
5. **RTL preview**: Always preview ads in the Google Ads interface to verify Hebrew text renders correctly. Pay attention to mixed Hebrew/English strings (e.g., brand names, numbers) which may reorder in RTL context.

**Meta (Facebook/Instagram) ad copy:**

- Primary text: roughly 125 characters visible before "See more", headline roughly 27 visible. These are practitioner rules of thumb, not published Meta limits: the truncation point varies by placement and device, so preview in Ads Manager for the placements you are actually buying rather than writing to a fixed number.
- Headline: roughly 27 characters visible in feed. Treat any "maximum" you have seen quoted for this field as unverified and preview instead.
- Use emojis strategically (they work well in Israeli Facebook ads)
- Include a clear CTA in Hebrew: "הזמינו עכשיו", "קבלו הנחה", "הצטרפו אלינו"

### Step 4: Israeli Audience Targeting

Israeli audience targeting requires understanding the country's unique geographic, demographic, and behavioral patterns.

**Geographic targeting:**

Directional planning estimates, not measured shares, and they do not sum to a whole. Use them to rank regions by competition, never to size a market.

| Region | Population Share (approx) | Relative Competition | Notes |
|--------|--------------------------|----------------------|-------|
| Gush Dan (Tel Aviv metro) | ~40% | Highest | Highest CPCs; over-indexes on ad spend relative to population |
| Haifa and North | ~20% | Lower | Lower CPCs, more Hebrew-dominant |
| Jerusalem | ~12% | Moderate | Mixed Hebrew/Arabic, distinct demographics |
| Be'er Sheva and South | ~15% | Lower | Lower competition, lower CPCs |
| Judea and Samaria | ~5% | Lower | Requires careful geo-targeting |

For real regional weighting use the campaign's own geographic report after two to four weeks.

**Demographic targeting notes:**

- **Military service gap**: Israelis serve in the IDF from age 18-21 (men) or 18-20 (women). Purchasing power and consumer behavior differ significantly from other countries in this age range. Adjust age targeting accordingly: the "young professional" segment starts at 22-23 in Israel, not 18.
- **Shabbat scheduling**: Most Israeli consumers are inactive Friday afternoon (14:00) through Saturday evening (20:00). Pause or reduce bids during these hours to avoid wasted spend. Exception: secular audiences in Tel Aviv may still be active.
- **Holiday calendar**: Israeli holidays (Rosh Hashana, Yom Kippur, Sukkot, Pesach) follow the Hebrew calendar and shift dates yearly. Pause campaigns on Yom Kippur. Adjust budgets before holidays (pre-holiday shopping spikes are common).
- **Mobile-first, but not as lopsided as usually claimed**: Israeli web traffic is 53.62% mobile, 44.91% desktop, 1.47% tablet (StatCounter, July 2026). The widely repeated "over 70% mobile" figure does not hold for Israel. Still design ads and landing pages mobile-first and use vertical video for Meta and TikTok, but do not deprioritise desktop landing-page quality or desktop bid adjustments on the strength of a 70% number, because nearly half your traffic is desktop.

**Behavioral targeting on Meta:**

- Interest-based: Target Hebrew speakers, Israeli TV shows, local brands, Israeli news outlets
- Custom audiences: Upload customer phone lists or emails only with documented consent (Israeli phone format: 05X-XXXXXXX). See "Consent for ad targeting under Amendment 13" below before any list upload. Two operational gates block a first upload regardless of consent: Meta requires the identifiers to be **hashed** before upload, and the **Custom Audience Terms of Service must be accepted** on the ad account or the upload errors out. Check Meta's current customer-list documentation for the exact hashing algorithm and per-batch record limit before your first upload rather than assuming; the hashing requirement is also worth naming in your Amendment 13 documentation, since it is a genuine technical mitigation.
- Advantage+ audiences: Meta's predictive, AI-driven targeting. In an Advantage+ campaign you can feed a customer list or a lookalike seed as an "audience suggestion," which Meta treats as a soft signal and expands beyond. Pair broad Advantage+ targeting with diverse creative rather than narrow interest stacks.
- Advantage+ Shopping campaigns (ASC): for e-commerce, the default Meta structure now; the algorithm handles audience discovery from the catalog and pixel/CAPI signals.
- Lookalike audiences: still creatable, and **not** documented by Meta as deprecated. Marketing blogs widely claim a phase-out. We could not find a deprecation notice in Meta's own documentation, so do not tell a client lookalikes are being removed unless you can point at one. The defensible practitioner position is narrower: on most accounts broad Advantage+ targeting now performs at least as well as a narrow lookalike, so treat a lookalike as a seed to test against broad rather than as a default. That is judgment, not platform policy.
- **Google restricts sensitive-category targeting too, and this is the gap most agents miss.** Google's personalized-advertising policy lists sensitive interest categories including Health, Negative financial status, Gambling, Race and ethnicity, Religious beliefs and Sexual orientation, and states that advertisers promoting products or services falling within them "are unable to use advertiser-curated audiences". Advertiser-curated audiences are exactly what a Customer Match upload creates. So for an Israeli health, debt-relief, insurance or legal advertiser, the Customer Match plan may be blocked on Google for the same reason the equivalent Meta audience is, and you will find out AFTER doing the Amendment 13 consent work. Check the policy for your vertical before promising a client a list-based campaign.
- **Restricted custom audiences on Meta (this bites the same Israeli verticals).** Meta restricts audience definitions that imply sensitive attributes about people, and health and financial status are the long-standing examples. The highest-CPC verticals in Israel are Legal, Finance, Insurance and Health, so an audience built as "high income" or around a medical condition is the likely default an agent reaches for and a likely rejection. Check Meta's Advertising Standards (linked in Reference Links) for the current restricted categories before building one.

**Consent for ad targeting under Amendment 13 (gate 1, the DATA):** Amendment 13 to the Privacy Protection Law is in force. Uploading a customer list for Meta Custom Audiences or Google Customer Match, using that list as a lookalike or Advantage+ seed, and pixel/CAPI remarketing all require explicit, informed, freely given and GRANULAR consent for that specific use. A generic "we may contact you" checkbox is not enough, and bundled or pre-ticked consent is invalid. Keep documentation of when and how each contact consented; large and sensitive databases carry additional registration and notification duties. Treat consent and incident-reporting as live obligations and check the Privacy Protection Authority's current guidance, including its opinion on appointing a privacy protection officer, before running list-based or remarketing campaigns. This is a compliance area, not advertising advice; have a privacy lawyer review the consent flow. Google Consent Mode is a separate technical obligation for EEA/UK traffic, not a substitute. Full detail in `references/israeli-ad-regulations.md`.

**Contacting the leads you collect (Spam Law):** Amendment 13 governs the DATA; Israel's Spam Law (Section 30A of the Communications Law) governs the MESSAGING. Before you SMS, email, or auto-call a lead captured from a Lead Ad or landing-page form, you need prior opt-in consent, the message must identify the sender and carry the word "פרסומת" (advertisement) with a working opt-out, and a violation carries statutory damages of up to about 1,000 NIS per message with no proof of harm. Treat list-building (Amendment 13) and lead-contacting (Spam Law) as two separate consent gates.

### Step 5: Ad Regulations (Chok Haganat HaTzarchan)

Israeli advertising is regulated primarily by the Consumer Protection Law (חוק הגנת הצרכן, 1981) and its amendments. Non-compliance can result in fines and criminal penalties. See `references/israeli-ad-regulations.md` for the full regulatory reference.

**Mandatory requirements:**

| Requirement | Details | Penalty |
|-------------|---------|---------|
| VAT-inclusive pricing | All advertised prices must include 18% VAT | Fine + ad takedown |
| Sponsored content labeling | Must display "פרסומת" or "תוכן ממומן" | Fine per violation |
| Accurate claims | No misleading statements about product/service | Criminal penalties possible |
| Comparative advertising | Allowed only if claims are verifiable and accurate | Lawsuit + fine |

**Category-specific restrictions:** financial services, health/medical, alcohol, gambling, food and real estate each carry extra disclosure or licensing duties. The per-category table is in `references/israeli-ad-regulations.md`; check it before writing copy in any of those verticals.

**Influencer marketing rules:**

Israeli law requires influencers to clearly disclose paid partnerships. Use #פרסומת or #תוכן_ממומן in Hebrew posts. The disclosure must be visible without clicking "more" or scrolling.

**Landing page compliance:**

- Landing page prices must match ad prices (both VAT-inclusive)
- "Terms and conditions" links must be in Hebrew
- Return/cancellation policy must be accessible. For a distance sale (website or phone) the general right is 14 days, but the clock and the deadline vary by transaction type: a product runs 14 days from receipt of the goods or of the transaction document, whichever is later; a one-off service is 14 days but no later than two days before the service date; a continuing service is 14 days from the transaction even if service already started; an Israeli tourism service is 14 days but no later than seven business days before. Do not state a flat "14 days" without the type.
- **A new immigrant (oleh chadash holding a teudat oleh less than five years old), a person with a disability, or a person aged 65 or over may cancel within FOUR MONTHS rather than 14 days**, where the transaction involved a conversation with the business. This materially changes a cancellation policy and an agent writing Israeli landing-page terms will otherwise omit it entirely.
- Privacy policy required for any data collection

### Step 6: Set Up Conversion Measurement (do this BEFORE Step 7)

Every bidding, CPA and ROAS instruction below assumes conversions are being counted correctly. If they are not, Smart Bidding optimizes toward noise and the budget math is fiction. Build this first:

1. Install the Google tag / Meta pixel AND the server-side Conversions API where available, then deduplicate the two with a shared event ID so one purchase is not counted twice.
2. Pass a conversion **value** and an explicit **currency** (ILS), and decide the VAT basis of that value now (see "VAT and ROAS" below). The platform optimizes to whatever value you send.
3. Define which action is the conversion. For Lead Ads a form fill is not a qualified lead; import the CRM outcome as an offline conversion so bidding optimizes on the lead you actually wanted.
4. Fire a test conversion and confirm it appears in the platform before spending. Do not launch on untested tracking.
5. Pass consent signals (see Step 5) so EEA/UK traffic remains measurable.

### Step 7: Budget and Bidding

**Israeli CPC planning defaults by vertical (illustrative, NOT measured Israeli data):**

Order-of-magnitude planning defaults only. There is no published Israeli CPC benchmark dataset; the vertical ranking derives from US benchmark data adjusted for a smaller market. Do not quote these to a client as Israeli benchmarks. The sourced path is a Keyword Planner forecast (location Israel, language Hebrew) for your actual keywords, then your own search-terms and auction-insights reports.

The full per-vertical table lives in `references/israeli-ad-regulations.md` under "CPC planning defaults", and the same numbers are encoded in `scripts/cpc_calculator.py`, so run the script rather than retyping them.

**Budget planning with the bundled calculator:**

Use the bundled `scripts/cpc_calculator.py` to estimate campaign costs:

```bash
# Show all vertical benchmarks
python scripts/cpc_calculator.py --benchmarks

# Estimate campaign for e-commerce with 5,000 NIS budget
python scripts/cpc_calculator.py --vertical ecommerce --budget 5000

# Custom CPC estimate
python scripts/cpc_calculator.py --vertical legal --budget 10000 --cpc 30
```

The calculator treats the entered budget as ex-VAT ad spend (the amount that buys clicks), shows the reclaimable input VAT separately, and estimates conversions at multiple conversion rates (1%, 2%, 3%, 5%).

**Bidding strategy progression:**

| Stage | Strategy | When to Use |
|-------|----------|-------------|
| Launch (Week 1-2) | Manual CPC | Gathering data, fewer than 15 conversions |
| Learning (Week 3-4) | Maximize Conversions (add Target CPA once stable) | 15-30 conversions, letting Google's Smart Bidding adjust |
| Optimization (Month 2+) | Target CPA | 30+ conversions, stable conversion rate |
| Scale (Month 3+) | Target ROAS | Sufficient revenue data, e-commerce focused |
| Max performance | Maximize Conversions | High budget, broad targeting, trust the algorithm |

Google's current strategy list also includes **Maximize conversion value**, **Target impression share**, and **Target CPC**. Note the scope carefully: Google states Target CPC "is only available on Demand Gen campaigns". It is therefore NOT the Search-side replacement for ECPC, and an agent that reaches for it on a Search campaign will not find it. On Search, the replacement is Maximize Conversions, optionally with a Target CPA.

Note: Enhanced CPC (ECPC) is no longer available for Search and Display campaigns. Google states that effective the week of March 31, 2025 ECPC is no longer available for Search and Display campaigns. Campaigns not migrated proactively defaulted to Manual CPC. For the Learning stage, use Maximize Conversions (optionally with a Target CPA) instead. Verify against the Google Ads Help "About Smart Bidding" page.

**VAT and ROAS:**

For a VAT-registered business (osek murshe, the standard advertiser here), the 18% VAT on your Google/Meta invoice is input VAT (mas tashumot) that you reclaim against your output VAT on your bimonthly return. It is NOT a real cost, so it must NOT go into your ROAS denominator. Use the ex-VAT ad spend:

- Ad spend (ex-VAT): 1,000 NIS (the amount billed for clicks)
- VAT on the invoice: 180 NIS, reclaimed as input VAT, so the net cost stays 1,000 NIS
- Revenue generated: 5,000 NIS **ex-VAT**
- ROAS: 5,000 / 1,000 = 5.0x

**Both sides of the ratio must use the same VAT basis.** This skill also requires you to advertise VAT-inclusive prices, so the revenue your conversion tag reports is normally GROSS of output VAT, which is not your money either. Dividing gross revenue by ex-VAT spend inflates ROAS by the VAT fraction of revenue, which is the same size of error as the one this section exists to prevent, just in the other direction. Use ex-VAT revenue over ex-VAT spend, or gross over gross, never one of each. Decide which basis your conversion tag sends before you set any Target ROAS goal, because the platform optimizes to whatever value you pass it.

Only divide by 1.18 (5,000 / 1,180 = 4.24x) if you are an osek patur or otherwise cannot reclaim input VAT, or when you are explicitly modeling short-term cash flow (you front the VAT now and reclaim it on the next bimonthly return). Do not bake it into headline ROAS for a registered business. An osek patur does not charge VAT to customers and correspondingly may not offset VAT on purchases at all.

**First establish who invoices you and in what form.** The whole input-VAT mechanism below assumes the platform bills you through an entity that issues an Israeli tax invoice (חשבונית מס) with an Israeli VAT line. If your Google or Meta invoice is issued by a foreign entity instead, there is no Israeli tax invoice and no allocation number to look for, and the treatment is the one for imported services rather than the one below. We could not verify which applies to a given advertiser, so check an actual invoice with your accountant before building a ROAS model on it; if the VAT is not in fact reclaimable, the 1.18-divided figure is your real ROAS after all.

**The reclaim is conditional, and one condition changed in 2026.** Input VAT is deductible only where the expense is for business use, is attributed to a taxable transaction, and is backed by a proper tax invoice (חשבונית מס כדין) issued in the business's name. On top of that, an allocation number (מספר הקצאה) from the Tax Authority is now required to offset VAT on larger invoices, and the threshold has been ratcheting down: invoices from 01.06.2026 need one above 5,000 NIS, first-half-2026 invoices above 10,000 NIS, 2025 invoices above 20,000 NIS, and 2024 invoices above 25,000 NIS. Monthly ad spend at the budgets in this skill clears 5,000 NIS easily, so check that your platform invoice is a proper Israeli tax invoice carrying an allocation number where one is required. If it is not reclaimable, the VAT stops being a wash and your real ROAS is the 1.18-divided figure after all.

**Monthly budget minimums:** recommended starting budgets by platform are tabulated in `references/israeli-ad-regulations.md` under "Monthly budget minimums". They are planning defaults, not platform minimums.

## Examples

### Example 1: Set Up Hebrew Google Ads Campaign
User says: "Create a Google Ads campaign targeting Israeli customers"
Actions:
1. Set campaign location to Israel, language Hebrew + English
2. Write Hebrew ad copy (30 chars headline, 90 chars description)
3. Set budget in NIS, expect CPC of 2-8 NIS (varies by industry)
4. Add Hebrew negative keywords to avoid wasted spend
5. Set up conversion tracking with NIS values (use ex-VAT ad spend in ROAS for a registered business)
Result: Hebrew Google Ads campaign with Israeli market targeting

### Example 2: Launch Facebook Ads for Israeli Audience
User says: "Create Facebook ad campaigns for our Israeli restaurant chain"
Actions:
1. Target: Israel, age 25-54, Hebrew speakers, food interests
2. Create Hebrew ad copy with local references and NIS pricing
3. Use carousel format with Hebrew RTL text overlays
4. Set daily budget in NIS, expect CPM of 15-40 NIS
5. Schedule ads for Israeli peak hours (Sunday-Thursday evenings)
Result: Localized Facebook campaign targeting Israeli food audience

### Example 3: Calculate Campaign Budget
User says: "How much should I spend on Google Ads for my Israeli law firm?"
Actions:
1. Run `python scripts/cpc_calculator.py --vertical legal --budget 10000` to estimate clicks and conversions
2. Legal planning default CPC 15-40 NIS (avg 25 NIS), so a 10,000 NIS ex-VAT ad budget yields roughly 400 clicks (the 18% VAT is reclaimable, see Step 6). Replace this default with a Keyword Planner forecast for the firm's actual keywords before quoting it to the client
3. At 3% conversion rate the script reports 12 conversions at a CPA of 833 NIS. Use the script's output, not a rounded figure
4. Recommend starting with 8,000-12,000 NIS/month, scaling based on CPA targets
5. Set up Manual CPC bidding initially, move to Target CPA after accumulating 30+ conversions
Result: Data-driven budget recommendation with conversion estimates

## Bundled Resources

### Scripts
- `scripts/cpc_calculator.py` -- Calculates CPC benchmarks and budget estimates for Israeli ad campaigns. Supports all major verticals with min/avg/max CPC data. Treats the budget as ex-VAT ad spend and shows the reclaimable input VAT separately. Run: `python scripts/cpc_calculator.py --help`

### References
- `references/israeli-ad-regulations.md` -- Israeli advertising regulations including Consumer Protection Law requirements, Amendment 13 consent rules for ad targeting, digital advertising rules, restricted categories, Shabbat scheduling best practices, and audience targeting tips. Consult when verifying ad compliance or planning campaign schedules.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Google Ads Help, About Smart Bidding | https://support.google.com/google-ads/answer/2459326 | Current automated bidding strategies (Maximize Conversions, Target CPA, Target ROAS); confirms ECPC is gone |
| Google Ads policies | https://support.google.com/google-ads/answer/6008942 | Advertising policies and restricted-content rules |
| Meta Advertising Standards | https://transparency.meta.com/policies/ad-standards/ | Meta's ad content rules, applies to Israeli campaigns |
| Privacy Protection Authority (Amendment 13) | https://www.gov.il/en/departments/the_privacy_protection_authority/govil-landing-page | Amendment 13 consent guidance for customer lists, lookalike seeds, pixel/CAPI tracking |
| Kol Zchut, cancelling a distance transaction | https://www.kolzchut.org.il/he/ביטול_עסקת_מכר_מרחוק | Cancellation windows by transaction type, and the four-month right for olim, people with disabilities and over-65s |
| Israel Tax Authority | https://www.gov.il/he/departments/israel_tax_authority/govil-landing-page | VAT rate (currently 18%) applied to ad spend and pricing |

## Recommended MCP Servers

| MCP Server | Why It Helps |
|------------|--------------|
| `hebcal` | Step 4 scheduling depends on the Hebrew calendar: campaigns should pause on Yom Kippur and during Shabbat hours, and budgets shift before holidays. Holiday dates move every year. The hebcal MCP returns Hebrew holiday and Shabbat dates so dayparting and budget pacing can be automated against accurate dates. |

## Gotchas

- Israeli ad prices must include VAT by law. Agents generate copy with pre-VAT prices, which breaches the Consumer Protection Law.
- Agents divide ad spend by 1.18 when computing ROAS for a VAT-registered business. For an osek murshe the input VAT is reclaimable, so ROAS uses ex-VAT spend. Keep both sides of the ratio on the same VAT basis.
- Agents set nationwide targeting for a business that only serves one region, wasting budget in the most expensive auctions.
- Agents run campaigns 24/7 and burn budget through Shabbat and Yom Kippur, when engagement collapses.
- Agents target only one Hebrew inflection and miss the search volume sitting on the other forms of the same root.
- Mixed Hebrew/English/digit strings reorder unexpectedly in RTL. Always use the platform's ad preview before publishing.
- Agents suggest customer-list uploads, lookalike seeds or pixel/CAPI remarketing with no consent caveat, breaching Amendment 13.
- Agents recommend Enhanced CPC, which no longer exists for Search and Display. They also reach for Target CPC as its replacement, but Google states Target CPC is Demand Gen only.
- Agents repeat the blogged claim that Meta is retiring Lookalike Audiences. Do not tell a client that without a Meta deprecation notice you can point at.
- Agents build "high income" or condition-based audiences for Israeli finance, insurance, legal and health advertisers. Both Google and Meta restrict sensitive-category targeting, and Google blocks advertiser-curated audiences (which is what Customer Match creates) for those verticals.
- Agents quote the CPC and CPM tables as measured Israeli benchmarks. They are illustrative planning defaults derived from US data.
- Agents write a flat "14-day cancellation right" into landing-page terms, missing both the per-transaction-type variations and the four-month right for olim, people with disabilities and over-65s.
- Agents set Target CPA or Target ROAS before conversion tracking is installed and tested, so bidding optimizes on noise.

## Troubleshooting

### Error: "Hebrew ad text truncated"
Cause: Hebrew characters may have different display widths than Latin characters in certain fonts.
Solution: Test ad preview in Hebrew using the platform's built-in preview tool. Google Ads headline limit is 30 characters, and Hebrew words are often shorter than English equivalents, so you likely have room to expand. Check for mixed Hebrew/English strings that may cause unexpected RTL reordering.

### Error: "Unsure how VAT affects ROAS"
Cause: Israeli ad invoices add 18% VAT, but for a VAT-registered business that VAT is reclaimable input tax, so adding it to the ROAS denominator understates ROAS by ~18%.
Solution: For an osek murshe, compute ROAS on ex-VAT ad spend (Revenue / Ad Spend), because the 18% input VAT is offset against your output VAT. Add the 18% (Revenue / (Ad Spend * 1.18)) only for an osek patur who cannot reclaim it, or when modeling short-term cash flow.

### Error: "Low click-through rate on Hebrew ads"
Cause: Ad copy may be too formal or translated literally from English, which does not resonate with Israeli audiences.
Solution: Rewrite ads in natural conversational Hebrew. Use informal register (guf sheni: "אתה/את"), include NIS pricing with VAT, and add local trust signals like "חברה ישראלית" or a local phone number. Test 3-5 headline variations.

### Error: "Campaign spending but no conversions"
Cause: Common in the first 2 weeks of a new campaign, or due to targeting/landing page issues.
Solution: Check that the landing page is in Hebrew, loads fast on mobile, and has a clear CTA. Verify conversion tracking fires correctly. Review search terms report for irrelevant queries and add negative keywords. If targeting Gush Dan only, ensure radius is not too narrow. Allow 2-4 weeks of data before making major changes.

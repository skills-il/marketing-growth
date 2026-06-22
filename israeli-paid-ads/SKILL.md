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
| Google Ads (Search) | High-intent traffic, lead gen | ~95% search market share in Israel | N/A (CPC model) | Text ads, responsive search ads |
| Google Ads (Display) | Brand awareness, retargeting | Google Display Network reach in IL | 5-15 | Banner, responsive display |
| Meta (Facebook) | B2C, community, local business | ~7.6M Israeli users | 15-40 | Image, video, carousel, collection |
| Instagram | Lifestyle, fashion, food, travel | ~5M Israeli users | 20-50 | Stories, reels, feed, shopping |
| LinkedIn | B2B, SaaS, enterprise, recruiting | ~3M Israeli professionals | 40-120 | Sponsored content, InMail, lead gen |
| TikTok | Gen Z, viral content, brand awareness | Growing Israeli user base (18-34) | 10-30 | In-feed video, branded effects |

**Campaign type selection guide:**

- **Lead generation**: Google Search Ads (high intent) or Meta Lead Ads (lower cost per lead, lower intent)
- **E-commerce sales**: Google Shopping + Meta Dynamic Product Ads (DPA)
- **App installs**: Meta App Install campaigns or Google App campaigns (UAC)
- **Brand awareness**: YouTube pre-roll, Meta reach campaigns, TikTok
- **Local business**: Google Local campaigns, Meta radius targeting around the business

Recent Google campaign-type changes: Discovery campaigns and Video Action campaigns have been folded into **Demand Gen** (the Video Action migration completed by mid-2025). Standalone **Call ads** can no longer be created as of February 2026; use responsive search ads with call assets instead.
- **B2B**: LinkedIn Sponsored Content + Google Search for branded/non-branded terms

**Israeli publisher and native networks:**

Beyond the global platforms, Israel has its own ad inventory worth considering, especially for brand reach and native content:

| Platform | Type | Best For |
|----------|------|----------|
| Taboola (Realize) | Native content recommendation | Native ads on Ynet, Walla, Globes, and other major Israeli news sites. Israeli company. PPC model. Advertisers now buy through Taboola's performance platform "Realize" (ads.realizeperformance.com), which replaced the old Taboola Ads UI in 2025. |
| Outbrain (now Teads) | Native content recommendation | Native ads on Haaretz, TheMarker, Calcalist, Mako, Times of Israel. Israeli-founded. PPC model. Outbrain merged with Teads (closed Feb 2025) and the company rebranded to Teads; the Outbrain native product is now bought through the Teads platform. |
| Yad2 | Classifieds marketplace | Real estate, automotive, second-hand goods, local services; high-intent local audience. |
| Walla, Ynet, Globes (direct) | Publisher display / sponsored content | Direct media buys and branded content on Israel's largest news properties; strong for brand campaigns and PR-adjacent content. |

Taboola (now sold through its Realize platform) and Outbrain (now part of Teads after the 2025 merger) both run a pay-per-click model and cover most of the Israeli premium-publisher landscape between them. They remain two separate competitors, the long-rumored Taboola-Outbrain merger never closed, so do not treat them as one company, just expect the newer brand/platform names. Direct buys with a publisher's ad sales team make sense for larger brand budgets or sponsored-content campaigns. All Israeli-platform campaigns are still subject to the VAT-inclusive pricing and labeling rules in Step 5.

### Step 2: Hebrew Keyword Research

Hebrew is a morphologically rich language with root-based word formation. A single root (shoresh) produces dozens of inflections, and keyword tools may not group them automatically. Thorough keyword research requires covering all variants.

**Hebrew morphology considerations:**

| Pattern | Example Root | Inflections to Target |
|---------|-------------|----------------------|
| Verb conjugations | ל.מ.ד (learn) | לומד, לומדת, לומדים, ללמוד, למד, ילמד |
| Noun forms | ב.ט.ח (insure) | ביטוח, ביטוחים, מבוטח, מבוטחת |
| Construct state (smichut) | | ביטוח רכב, ביטוח בריאות, ביטוח חיים |
| With/without definite article | | ביטוח vs הביטוח |
| Colloquial spelling | | אינטרנט vs אינטרנת |

**Keyword research process:**

1. **Seed keywords**: Start with 5-10 core terms in Hebrew. Include both formal and colloquial forms. Many Israelis search in English for tech terms (e.g., "CRM" not "ניהול קשרי לקוחות").
2. **Expand with Google Keyword Planner**: Set location to Israel, language to Hebrew. Export suggestions and group by intent (informational, commercial, transactional).
3. **Check English variants**: Israeli users frequently search in English or transliterated Hebrew (e.g., "ramzor" for רמזור). Add these as separate ad groups.
4. **Negative keywords in Hebrew**: Build a negative keyword list early. Common Hebrew negatives: "חינם" (free), "מה זה" (what is), "השוואה" (comparison, if not relevant).
5. **Competitor analysis**: Search your main keywords on google.co.il and note which competitors are bidding. Check their ad copy for messaging angles you can differentiate from.

**Tools for Hebrew keyword research:**

- Google Keyword Planner (set region: Israel)
- Google Trends (compare Hebrew vs English search volume for the same concept)
- Google Search Console (existing site query data)
- Ahrefs/Semrush (limited Hebrew support, but useful for competitor gap analysis)

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

- Primary text: 125 chars visible before "See more" (Hebrew counts the same)
- Headline: 27 chars visible in feed (40 max)
- Use emojis strategically (they work well in Israeli Facebook ads)
- Include a clear CTA in Hebrew: "הזמינו עכשיו", "קבלו הנחה", "הצטרפו אלינו"

### Step 4: Israeli Audience Targeting

Israeli audience targeting requires understanding the country's unique geographic, demographic, and behavioral patterns.

**Geographic targeting:**

| Region | Population Share | Ad Spend Share | Notes |
|--------|-----------------|---------------|-------|
| Gush Dan (Tel Aviv metro) | ~40% | ~40-45% | Highest competition, highest CPCs |
| Haifa and North | ~20% | ~15% | Lower CPCs, more Hebrew-dominant |
| Jerusalem | ~12% | ~10% | Mixed Hebrew/Arabic, unique demographics |
| Be'er Sheva and South | ~15% | ~10% | Lower competition, lower CPCs |
| Judea and Samaria | ~5% | ~5% | Requires careful geo-targeting |

**Demographic targeting notes:**

- **Military service gap**: Israelis serve in the IDF from age 18-21 (men) or 18-20 (women). Purchasing power and consumer behavior differ significantly from other countries in this age range. Adjust age targeting accordingly: the "young professional" segment starts at 22-23 in Israel, not 18.
- **Shabbat scheduling**: Most Israeli consumers are inactive Friday afternoon (14:00) through Saturday evening (20:00). Pause or reduce bids during these hours to avoid wasted spend. Exception: secular audiences in Tel Aviv may still be active.
- **Holiday calendar**: Israeli holidays (Rosh Hashana, Yom Kippur, Sukkot, Pesach) follow the Hebrew calendar and shift dates yearly. Pause campaigns on Yom Kippur. Adjust budgets before holidays (pre-holiday shopping spikes are common).
- **Mobile-first**: Over 70% of Israeli web traffic is mobile. Design ads and landing pages for mobile first. Use vertical video formats for Meta and TikTok.

**Behavioral targeting on Meta:**

- Interest-based: Target Hebrew speakers, Israeli TV shows, local brands, Israeli news outlets
- Custom audiences: Upload customer phone lists or emails only with documented consent (Israeli phone format: 05X-XXXXXXX). See "Consent for ad targeting under Amendment 13" below before any list upload.
- Advantage+ audiences: Meta's predictive, AI-driven targeting. Meta is phasing out static Lookalike Audiences through 2026 in favor of Advantage+. In an Advantage+ campaign you can still feed a customer list or a former lookalike seed as an "audience suggestion," but Meta treats it as a soft signal and expands beyond it. Pair broad Advantage+ targeting with diverse creative rather than narrow interest stacks.
- Advantage+ Shopping campaigns (ASC): for e-commerce, the default Meta structure now; the algorithm handles audience discovery from the catalog and pixel/CAPI signals.
- Lookalike audiences: still creatable but effectively deprecated. Meta's own documentation now points to Advantage+ audience instead. Treat any existing lookalike as a seed, not a hard constraint.

**Consent for ad targeting under Amendment 13:**

Amendment 13 to the Privacy Protection Law came into force on August 14, 2025. It directly affects how you can build ad audiences from personal data:

- Uploading a customer phone or email list for Meta Custom Audiences (or Google Customer Match) requires explicit, informed, freely given consent from those contacts for that use. A generic "we may contact you" checkbox is not enough.
- Consent must be granular. Bundled or pre-ticked consent is invalid. Marketing consent has to be separable from consent to the core service.
- The same applies to using a customer list as a lookalike or Advantage+ seed, and to pixel / Conversions API (CAPI) tracking that builds remarketing audiences.
- Keep documentation of when and how each contact consented. Large marketing databases (10,000+ records) and sensitive-data databases still carry registration and notification duties.
- This is a compliance area, not advertising advice. Verify the current Privacy Protection Authority (PPA) guidance and have a privacy lawyer review your consent flow. See `references/israeli-ad-regulations.md`.
- **Google Consent Mode v2** (required since March 2024) is a separate, technical obligation: if you target or measure users in the EEA/UK (common for Israeli companies selling to Europe), you must pass consent signals to Google via Consent Mode or you lose conversion measurement and remarketing for that traffic. It complements Amendment 13, it does not replace the documented consent you need for Israeli contacts.

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

**Category-specific restrictions:**

| Category | Requirement |
|----------|-------------|
| Financial services | Must include risk disclaimers ("השקעה כרוכה בסיכון") |
| Health/Medical | Cannot promise cures, must include disclaimers |
| Alcohol | No targeting of minors, must include health warnings |
| Gambling/Lottery | Requires license from Israeli authority |
| Food | Nutrition and health claims must be verified |
| Real estate | Must specify if prices exclude VAT for new construction |

**Influencer marketing rules:**

Israeli law requires influencers to clearly disclose paid partnerships. Use #פרסומת or #תוכן_ממומן in Hebrew posts. The disclosure must be visible without clicking "more" or scrolling.

**Landing page compliance:**

- Landing page prices must match ad prices (both VAT-inclusive)
- "Terms and conditions" links must be in Hebrew
- Return/cancellation policy must be accessible (14-day cancellation right under Israeli law)
- Privacy policy required for any data collection

### Step 6: Budget and Bidding

**Israeli CPC benchmarks by vertical (2025-2026 benchmarks, verify current rates):**

| Vertical | CPC Range (NIS) | Avg CPC (NIS) | Competition Level |
|----------|----------------|---------------|-------------------|
| Legal | 15-40 | 25 | Very High |
| Finance | 10-35 | 20 | Very High |
| Insurance | 10-30 | 18 | High |
| Real Estate | 8-25 | 15 | High |
| SaaS/Tech | 5-20 | 12 | Medium-High |
| Health | 5-18 | 10 | Medium |
| Travel | 3-15 | 8 | Medium |
| Education | 3-12 | 7 | Medium |
| E-commerce | 2-8 | 4 | Low-Medium |
| Food | 2-6 | 3 | Low |

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

Note: Enhanced CPC (ECPC) is no longer available for Search and Display campaigns. Google stopped offering it for new Search and Display campaigns in October 2024 and completed the forced migration the week of March 31, 2025. Campaigns not migrated proactively defaulted to Manual CPC. For the Learning stage, use Maximize Conversions (optionally with a Target CPA) instead. Verify against the Google Ads Help "About Smart Bidding" page.

**VAT and ROAS:**

For a VAT-registered business (osek murshe, the standard advertiser here), the 18% VAT on your Google/Meta invoice is input VAT (mas tashumot) that you reclaim against your output VAT on your bimonthly return. It is NOT a real cost, so it must NOT go into your ROAS denominator. Use the ex-VAT ad spend:

- Ad spend (ex-VAT): 1,000 NIS (the amount billed for clicks)
- VAT on the invoice: 180 NIS, reclaimed as input VAT, so the net cost stays 1,000 NIS
- Revenue generated: 5,000 NIS
- ROAS: 5,000 / 1,000 = 5.0x

Only divide by 1.18 (5,000 / 1,180 = 4.24x) if you are an osek patur or otherwise cannot reclaim input VAT, or when you are explicitly modeling short-term cash flow (you front the VAT now and reclaim it on the next bimonthly return). Do not bake it into headline ROAS for a registered business.

**Monthly budget minimums (recommended):**

| Platform | Minimum Monthly (NIS) | Recommended Monthly (NIS) |
|----------|----------------------|--------------------------|
| Google Search | 1,500 | 5,000-15,000 |
| Google Display | 1,000 | 3,000-8,000 |
| Meta (Facebook) | 1,000 | 3,000-10,000 |
| LinkedIn | 3,000 | 8,000-20,000 |
| TikTok | 1,500 | 4,000-10,000 |

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
2. Legal vertical CPC range: 15-40 NIS (avg 25 NIS), so a 10,000 NIS ex-VAT ad budget yields ~400 clicks (the 18% VAT is reclaimable, see Step 6)
3. At 3% conversion rate: ~10 leads per month at ~1,000 NIS per lead
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
| Consumer Protection (gov.il) | https://www.gov.il/he/departments/units/consumer_protection_unit | Consumer Protection Law, VAT-inclusive pricing, sponsored-content labeling |
| Israel Tax Authority | https://www.gov.il/he/departments/israel_tax_authority/govil-landing-page | VAT rate (currently 18%) applied to ad spend and pricing |

## Recommended MCP Servers

| MCP Server | Why It Helps |
|------------|--------------|
| `hebcal` | Step 4 scheduling depends on the Hebrew calendar: campaigns should pause on Yom Kippur and during Shabbat hours, and budgets shift before holidays. Holiday dates move every year. The hebcal MCP returns Hebrew holiday and Shabbat dates so dayparting and budget pacing can be automated against accurate dates. |

## Gotchas

- Israeli ad prices must include VAT (18%) by law under Chok Haganat HaTzarchan (Consumer Protection Law). Agents may generate ad copy with pre-VAT prices, which violates Israeli advertising regulations.
- Do NOT inflate ROAS by 18% VAT for a VAT-registered business (osek murshe). The VAT on your ad invoice is reclaimable input VAT, so true ROAS uses ex-VAT spend (5,000 / 1,000 = 5.0x, not 5,000 / 1,180). Only an osek patur, who cannot reclaim it, or a cash-flow model adds the 18%. Agents often wrongly divide ad spend by 1.18.
- The Gush Dan metropolitan area (Tel Aviv area) accounts for approximately 40% of Israeli digital ad spend. Agents may set nationwide targeting when the business only serves a specific region, wasting budget.
- Israeli ad scheduling must avoid Shabbat (Friday afternoon through Saturday evening). Agents may run campaigns 24/7 and burn budget during zero-engagement hours.
- Hebrew ad headlines have a 30-character limit in Google Ads, but Hebrew words are often shorter than English equivalents. Agents may not take advantage of the extra room available in Hebrew headlines.
- Hebrew keyword research must account for morphological variants. A single root can produce dozens of word forms. Agents may target only one inflection and miss significant search volume from other forms.
- Mixed Hebrew/English text in ads can reorder unexpectedly in RTL rendering. Always preview ads in the platform's ad preview tool before publishing.
- Uploading customer phone or email lists for Meta Custom Audiences or Google Customer Match without explicit, granular, documented consent violates Amendment 13 to the Privacy Protection Law (in force since August 2025). Agents may suggest list uploads, lookalike seeds, or pixel/CAPI remarketing with no consent caveat.
- Enhanced CPC (ECPC) is no longer a selectable bidding strategy for Search and Display campaigns. Agents trained on older Google Ads material may still recommend it; use Maximize Conversions or Target CPA instead.
- Static Lookalike Audiences on Meta are being phased out through 2026 in favor of Advantage+ predictive targeting. Agents may present lookalikes as the current standard; treat them as soft seeds, not hard targeting.

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

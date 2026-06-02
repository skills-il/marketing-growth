---
name: israeli-market-fit
description: "Assess whether a product or service fits the Israeli market before you build, launch, or localize it. Use when a founder or marketer asks 'will this work in Israel', 'who is the Israeli buyer', wants buyer personas or avatars for Israel, market sizing, product-market-fit, or a go / pivot / no-go decision, or asks in Hebrew about התאמת מוצר לשוק הישראלי, חקר שוק, or אווטאר קונה. Produces a market-fit report: segment sizing (secular, Haredi, Arab-Israeli, olim, periphery), buyer-avatar cards, localized positioning angles, and a viability verdict contrasting the global market with Israeli reality (Hebrew and RTL, shekel pricing, payment habits, regulatory gates, seasonality). Israel is a small, segmented market where a global plan usually must change. Do NOT use for writing the survey itself (hebrew-survey-builder), running paid ads (israeli-paid-ads), SEO content (israeli-content-marketing), or launch PR (israeli-product-launch)."
license: MIT
compatibility: Works as a reasoning workflow on any agent. The optional market-sizing script needs Python 3. Network access helps for fresh competitor and pricing research.
---


# Israeli Market Fit Analyzer

## Problem

Founders and marketers keep treating Israel as "a small version of the US market" and bring a global product, a dollar price, and an English funnel into a country that is small, multilingual, deeply segmented, and full of regulatory gates. The result is wasted budget: a launch that fit Tel Aviv dies in Bnei Brak or Nazareth, a price that ignored VAT and local wages reads as overpriced, and an email funnel that ignored Israeli consent law is illegal before it sends. This skill runs the upstream "should we, and for whom" analysis first, so the go / pivot / no-go decision is made on Israeli reality, not a global assumption.

## Instructions

You are producing one deliverable: a structured **Israeli Market Fit report** in markdown
with four sections (Segment Sizing, Buyer Avatars, Positioning Angles, Viability Verdict).
Do not skip to a verdict before the sizing and avatars support it. Ask the user for the
product, the price, and the target buyer if any are missing.

Read `references/segments.md` for the segment data and the avatar-card template, and
`references/domain-checklist.md` for the full coverage list. Use `scripts/market-sizing.py`
when the user wants real TAM/SAM/SOM numbers.

### Step 1: Frame the product and the global-vs-Israel question

Restate, in one or two sentences, what the product is and what job it does. Then name the
core question: is there a real Israeli buyer, and what about the global plan must change.
Israel's whole population is about 10.178 million, so a product whose unit economics
assume a US-sized market often does not survive contact with the numbers. Flag that
upfront.

### Step 2: Segment the market (do not treat Israel as one market)

Split the addressable market into the real sub-markets and decide which ones the product
can actually serve. Use these shares of the population:

| Segment | Share of population | Reach reality |
|---------|---------------------|---------------|
| Jews and others (secular to traditional mainstream) | 76.3% | Reachable through mainstream Hebrew channels |
| Arab-Israeli | 21.1% | Arabic-first; separate social graph and retail |
| Haredi (ultra-Orthodox) | 14.3% of the total | Separate media universe; mainstream ads do not reach them |
| Foreigners and others | 2.6% | Olim and migrant-worker sub-markets |

The Haredi segment is very young (median age 16, with 57% aged 0-19), which changes which
products have a real adult buyer there. New olim and Russian-speakers cut across the Jewish
majority and have their own languages and channels. Periphery and development-town buyers
face thinner delivery and higher price sensitivity than the Gush Dan center.

For each segment, decide: can the product serve it at all, and is the language and channel
fit realistic. Drop segments you cannot honestly reach.

### Step 2b: If the product is B2B or SaaS, switch the lens

The consumer-segment shares above matter much less for B2B. For a B2B or SaaS product, size
by accounts, not population, and confront the hard truth: the domestic Israeli logo count is
small, and many Israeli startups deliberately sell out of Israel, so the local market is
often a design-partner and beachhead rather than the revenue market. Address these instead
of consumer avatars:

- The real domestic TAM is a count of relevant Israeli companies, which is usually a rounding
  error next to a global plan. Decide whether Israel is a revenue target or a proving ground.
- Enterprise and government buy through tenders (מכרז), resellers, and integrators, on long
  cycles. Plan the channel accordingly.
- Contracting is often in dollars for enterprise and shekels for SMB; decide your pricing
  currency per tier.

Then continue with Steps 3 to 7, sizing by accounts and writing buyer avatars for the
economic buyer and the champion inside the target organization rather than for a consumer.

### Step 3: Size the serviceable market bottom-up

For each segment you keep, estimate the serviceable market from the bottom up:
segment population, times a defensible adoption fraction, times annual spend per buyer.
Run `scripts/market-sizing.py` to keep yourself honest:

```bash
python scripts/market-sizing.py --segment-pop 7771000 --adoption 0.04 \
    --annual-spend 240 --serviceable 0.15
```

State your adoption and spend assumptions explicitly. The output (SOM) is the number the
verdict hangs on. If the SOM for every reachable segment is smaller than the fixed cost of
serving the market, that is a no-go signal regardless of how exciting the product is.

### Step 4: Build one buyer-avatar card per served segment

Fill the avatar template from `references/segments.md` for each segment you decided to
serve. Ground every field in the segment data, not invented demographics. Each card must
name: the language for product and support, the income band relative to the local average
wage (13,566 NIS per month as of January 2026), where they discover and where they buy,
preferred payment, the top objections, the trust triggers, and why the global pitch does
not land as-is.

### Step 5: Localize the positioning angles

Translate the product's value into Israeli reality, not a translated US pitch:

- **Language and UX:** Hebrew-first and RTL, with Arabic for the Arab segment where
  relevant. Go past "RTL": Hebrew that reads as machine-translated is a top trust-killer,
  mixed Hebrew/English/number lines break BiDi rendering, and date, phone, and address
  formats are local. Budget for a real Hebrew content writer, not a translation pass.
- **Pricing:** price in shekels, VAT-inclusive at 18%. Note that VAT is a recurring
  budget-bill lever in Israel, so confirm the current rate before you lock a price. Do not
  anchor willingness-to-pay to the average (mean) wage of 13,566 NIS per month: it is pulled
  up by high earners and the median is materially lower, so benchmark against local
  substitute prices, not US incomes. Interest-free installments (תשלומים) are an expectation,
  and they are themselves a pricing lever, not a footnote.
- **Payment rail:** the dominant business checkout is credit cards through local gateways
  and acquirers (for example Tranzila, Cardcom, Meshulam), which is also what processes
  installments. Not every foreign gateway supports Israeli installments, so a US-only Stripe
  setup may not be enough. Bit (Bank Hapoalim) and paybox (Discount Bank) dominate
  peer-to-peer transfers and suit small sellers and C2C, but they are not the primary
  business checkout, so do not plan your commerce rail around "accept Bit".
- **Channels:** map the product to where Israelis actually transact. For digital and D2C:
  WhatsApp commerce, Facebook groups, Yad2, and local marketplaces, not just the app stores.
  For physical goods on shelves: retail is concentrated and often gated by a single importer
  or distributor and by chains such as Shufersal, Rami Levy, and Super-Pharm. The real
  competitor is frequently a grey-market parallel importer selling the same brand cheaper, or
  buyers importing directly from foreign sites (check the current personal-import tax
  exemption that makes "I will just order it from abroad" the substitute).
- **Trust:** Israeli buyers are price-aggressive and recommendation-driven. Local phone
  support, Israeli social proof, and a Hebrew interface raise trust more than a slick
  global brand. Also check whether a local copycat already cloned the product or whether the
  global incumbent already serves Israel directly in English.

### Step 6: Flag the regulatory and seasonality gates

These are gates that can kill a product before marketing even starts. Name the ones that
apply:

- **Official standards (תקן רשמי):** the Standards Institution of Israel and the Ministry of
  Economy can declare a standard mandatory, blocking import or sale of regulated goods
  (electrical, toys, food, cosmetics) until lab-tested.
- **Hebrew labeling:** every consumer-product package must carry clear Hebrew labeling,
  even when imported.
- **Consumer Protection Law:** deceptive marketing is prohibited, and the displayed price
  must be the final price.
- **Data and privacy:** Amendment 13 to the Privacy Protection Law (in force since 14 August
  2025) strengthened data-protection obligations and enforcement for anyone holding customer
  data, so a marketing database is itself a compliance responsibility.
- **Marketing consent (anti-spam law):** sending promotional email or SMS requires the
  recipient's prior, explicit, written consent (active opt-in, not a pre-checked box). This
  is the anti-spam law, separate from Amendment 13. Sending without consent exposes you to
  statutory damages of up to 1,000 NIS per message without proof of damage, which a class
  action multiplies fast.
- **Seasonality:** demand swings around the Jewish-holiday calendar (Rosh Hashana, Pesach,
  Sukkot), Ramadan for the Arab segment, the August vacation, and reserve-duty (miluim)
  call-ups that disrupt B2B.

### Step 7: Write the viability verdict (go / pivot / no-go)

Combine the evidence into one explicit recommendation:

- **Go:** at least one reachable segment has a SOM that clears the cost floor, the channel
  fit is real, and no regulatory gate is fatal.
- **Pivot:** the demand exists but the global plan must change first (segment focus,
  language, price model, or a regulatory path). Name exactly what must change.
- **No-go:** the serviceable market is too small, a regulatory gate is prohibitive, or a
  free local substitute already owns the job.

End the report with the global-vs-Israel delta: a short list of what is true globally that
is not true in Israel, and what the founder must change to win here.

## Examples

**Example 1: Global SaaS founder.** User: "We have a US time-tracking SaaS at 12 dollars a
month. Will it work in Israel?" The skill sizes the secular Hebrew SMB segment bottom-up,
finds the SOM is small, flags that the price must move to shekels and VAT-inclusive
pricing with installments, that the channel is WhatsApp and Facebook groups rather than
paid search, and returns a "pivot" verdict: viable only if repriced and Hebrew-localized
with a free tier to beat the "good enough Excel" substitute.

**Example 2: Israeli D2C founder.** User: "אני רוצה למכור מוצרי טיפוח טבעיים, למי כדאי
לכוון?" The skill builds avatars for the secular mainstream and a modesty-aware Haredi
sub-segment, flags the Hebrew-labeling and official-standard gates for cosmetics, prices
against the local average wage, and recommends a "go" with a center-first launch and a
Bit-friendly checkout.

**Example 3: Adapting a global brand.** User: "Our meditation app is huge in the US, what
changes for Israel?" The skill returns the global-vs-Israel delta: smaller market, Hebrew
and RTL, holiday-and-miluim seasonality that changes when people seek calm, and a pricing
model in shekels, with a recommendation to localize content rather than translate it.

## Bundled Resources

- `references/segments.md`: the six Israeli market segments with sourced sizes, plus the
  buyer-avatar card template.
- `references/domain-checklist.md`: the full coverage checklist (must-cover, should-cover,
  out-of-scope) with authoritative sources.
- `scripts/market-sizing.py`: bottom-up TAM/SAM/SOM estimator that forces real adoption
  and spend assumptions.

## Gotchas

- **Treating Israel as one Hebrew market.** Agents routinely size off the full 10.178
  million and assume mainstream Instagram ads reach everyone. The Haredi (14.3%) and
  Arab-Israeli (21.1%) segments have separate channels and languages; sizing and avatars
  must be per segment.
- **Pricing in dollars.** Israeli buyers expect shekel prices that already include the 18%
  VAT and offer installments. A dollar price or a VAT-exclusive price reads as overpriced
  and, if the displayed price is not final, breaches consumer-protection rules.
- **Forgetting the regulatory gate exists.** For physical goods, agents jump to marketing
  and skip the official-standard (תקן רשמי) and Hebrew-labeling gates that can block import
  or sale entirely. Check the gate before you size the upside.
- **Building an email funnel without consent.** Defaulting to an opt-out mailing list or a
  pre-checked consent box violates the anti-spam law; consent must be prior, explicit, and in
  writing, and a customer database also carries Amendment 13 duties. Do not conflate the two:
  the email/SMS opt-in is the anti-spam law, the data obligations are Amendment 13.
- **Treating Bit or paybox as the business checkout.** Bit and paybox are peer-to-peer apps.
  The business commerce rail is credit cards through a local gateway with installments. An
  agent that recommends "just accept Bit" is giving a wrong checkout answer.
- **Assuming "no competitor in Israel."** The real competitor is often a free WhatsApp group,
  an Excel sheet, a Yad2 listing, a grey-market parallel importer selling the same brand
  cheaper, or buyers importing directly from abroad. List the local substitute, and the
  import-it-yourself substitute, before claiming a gap.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| CBS population release | https://www.cbs.gov.il/he/mediarelease/DocLib/2025/422/01_25_422b.pdf | Total population and Jewish/Arab/other split |
| IDI Haredi Yearbook 2025 | https://www.idi.org.il/haredi/2025/?chapter=62168 | Haredi share, median age, youth share |
| PwC Israel tax summary | https://taxsummaries.pwc.com/israel/corporate/other-taxes | Current standard VAT rate |
| Standards Institution of Israel | https://www.sii.org.il/he/israelistandards/ | Official-standard (תקן רשמי) and import rules |
| Consumer Protection Law (Nevo) | https://www.nevo.co.il/law_html/law00/70305.htm | Deception ban and final-price display |
| Hebrew labeling requirement | https://weksler-davidovich.co.il/consumer-protection-labeling/ | Mandatory Hebrew labeling on consumer products |
| Privacy Amendment 13 (gov.il) | https://www.gov.il/he/pages/13_amendment | Data-protection obligations for customer data |

## Recommended MCP Servers

No MCP server is required. This skill reasons over the bundled segment data and the user's
product description. For live competitor or pricing research, use the agent's built-in web
access.

## Troubleshooting

- **The verdict feels arbitrary.** You probably skipped the bottom-up sizing. Run
  `scripts/market-sizing.py` with explicit adoption and spend assumptions and let the SOM
  drive the verdict.
- **The avatars look generic.** Re-read `references/segments.md` and ground each field in
  segment data (language, median age, channels), not invented persona details.
- **The user only wants the buyer persona, not a full report.** Produce just the relevant
  avatar cards from Step 4, but still anchor them to the segment sizing so the persona is
  real and not a stereotype.
- **The product is B2B or government.** Note that procurement runs on long cycles and
  tenders (מכרז); the consumer-segment sizing matters less than the buyer organization and
  its tender rules.

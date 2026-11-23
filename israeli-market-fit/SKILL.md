---
name: israeli-market-fit
description: "Commercial analysis only. Assess whether a product or service fits the Israeli market before you build, launch, or localize it. Use when a founder or marketer asks 'will this work in Israel', 'who is the Israeli buyer', wants buyer personas or avatars for Israel, market sizing, product-market-fit, or a go / pivot / no-go decision, or asks in Hebrew about התאמת מוצר לשוק הישראלי, חקר שוק, or אווטאר קונה. Produces a market-fit report: segment sizing (secular, Haredi, Arab-Israeli, olim, periphery), buyer-avatar cards, localized positioning angles, and a viability verdict contrasting the global market with Israeli reality (Hebrew and RTL, shekel pricing, payment habits, regulatory gates, seasonality). Israel is a small, segmented market where a global plan usually must change. Do NOT use for writing the survey itself (hebrew-survey-builder), running paid ads (israeli-paid-ads), SEO content (israeli-content-marketing), or launch PR (israeli-product-launch)."
license: MIT
compatibility: Works as a reasoning workflow on any agent. The optional market-sizing script needs Python 3. Network access helps for fresh competitor and pricing research.
---


# Israeli Market Fit Analyzer

## Legal notice

This is a free information tool operated by an AI model. It segments the Israeli market, sizes it bottom-up, and flags possible regulatory and seasonality gates, alongside a general explanation of the applicable law. All of its output is produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion; it is a commercial and marketing analysis only. It does not examine your documents or engagements, does not test your product's specific facts against the text of the law and current case law, and does not determine whether any exemption or exception applies to you. An AI model may err, omit data, or present a wrong conclusion, and tax rates, amounts, and regulatory rules change.

The go / pivot / no-go verdict is a commercial assessment only, and is not a determination that the product does or does not comply with the law. Do not rely on the output as the basis for a legal decision or for dealings with an authority. It is not a substitute for advice that takes into account the particular data and needs of each person, and before setting a consumer price, building a customer database, sending marketing messages, or importing and selling a product, consult an advocate.

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
Israel's whole population is about 10.305 million (CBS, September 2026), so a product whose unit economics
assume a US-sized market often does not survive contact with the numbers. Flag that
upfront.

### Step 2: Segment the market (do not treat Israel as one market)

Split the addressable market into the real sub-markets and decide which ones the product
can actually serve. Use these shares of the population:

| Segment | People and share of population | Reach reality |
|---------|-------------------------------|---------------|
| Jews and others (secular to traditional mainstream, including olim) | 7.828 million, 76% | Reachable through mainstream Hebrew channels; olim and Russian-speakers have their own |
| Arab-Israeli | 2.173 million, 21.1% | Arabic-first; separate social graph and retail |
| Foreign nationals | 304 thousand, about 3% | Foreign workers, students, clergy, volunteers, people CBS classes as infiltrators (מסתננים), overstaying tourists, and their families. Not olim |
| Haredi (ultra-Orthodox), a SUBSET of the first row | about 1.45 million at end-2025, 14.3% on IDI's base | Separate media habits; mainstream Hebrew media plans under-reach them, so test by sub-group, channel and language |

**Do not add these rows up.** The first three are mutually exclusive and already total the
whole population. The Haredi row is carved out of the first row, not additional to it, so
the mainstream Hebrew segment you size in Step 3 is the first row MINUS the Haredi share,
roughly 6.375 million people (approximate, because the Haredi count is from end-2025).
Subtract before you size, or you will double-count the Haredi population and overstate the
mainstream market. The first three shares are of all 10.305 million. CBS's own headline
shares (78.3% and 21.7%) exclude foreign nationals, so do not mix the two. Olim, Russian
speakers and periphery cut across these rows: describe them as views, never add them on top.

The 21.1% figure is the CBS "Arabs" category (Muslims, Arab Christians and Druze). It is not
one commercial segment. Residency status differs (in East Jerusalem few residents hold Israeli
citizenship), and banking and credit-card access and street-level addressing can differ too,
so a product that depends on card checkout or on courier delivery to a street address may not
reach all of that 21.1%. Say which sub-population you are actually sizing.

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
  error next to a global plan. Show where the count came from and the filter used. Decide
  whether Israel is a revenue target or a proving ground.
- Enterprise and government buy through tenders (מכרז), resellers, and integrators, on long
  cycles. Plan the channel accordingly.
- Contracting is often in dollars for enterprise and shekels for SMB; decide your pricing
  currency per tier. The consumer price rules in Step 6 protect a buyer for mainly personal
  use. Whether a given plan's sales are consumer sales, including self-serve signups, is a
  question for an advocate.
- Do not apply Step 5's Hebrew-first rule automatically. Decide language per buyer: English
  can work for a developer tool sold to tech companies, while SMBs, accountants,
  municipalities and government buyers usually need Hebrew product, support and paperwork.

Then continue with Steps 3 to 7, sizing by accounts and writing buyer avatars for the
economic buyer and the champion inside the target organization rather than for a consumer.

### Step 3: Size the serviceable market bottom-up

For each segment you keep, size from the bottom up in one **buying unit**. Choose it first:
person, adult, household, parent of a child in the age band, or business account. Convert the
population to that unit, and keep adoption and spend per that same unit. A household product
sized on all 6.375 million people, babies included, is overstated about threefold, because
Israeli households average 3.17 people.

Defend the adoption and early-win fractions with evidence: Hebrew search demand
(`hebrew-seo-geo-toolkit`), a survey (`hebrew-survey-builder`), or a comparable local product. A
paid incumbent lowers what you can win early. Enter annual spend per unit
**net of any VAT you will charge** (at 18%, divide a VAT-inclusive price by 1.18), because VAT
is not your revenue. Run
`scripts/market-sizing.py` to keep yourself honest. This example is a household product, on
about 2 million mainstream households (6.375 million divided by 3.17, a rough and probably low
figure because household size differs by segment). For B2B, pass the account count as `--segment-pop`:

```bash
python scripts/market-sizing.py --segment-pop 2000000 --adoption 0.04 \
    --annual-spend 240 --serviceable 0.15
```

In the script, `--serviceable` means the share of adopters you can win early. On a host that
cannot run a script (Claude.ai, ChatGPT, Claude Desktop, Manus), do the same three lines by
hand instead, and show them: TAM = buying units x annual spend; SAM = TAM x adoption fraction;
SOM = SAM x the fraction you can win early. The discipline is the point, not the script.

State your assumptions explicitly. SOM is annual revenue once you have won those buyers, not
first-year revenue. Then test the plan you would actually run: SOM x gross margin (after landed
cost, including customs duty and purchase tax on imported goods), minus annual acquisition cost, must cover the shared fixed cost plus each served segment's own added cost
(Arabic support, Haredi channels). Sum only mutually exclusive segments. At steady state,
annual acquisition cost = buyers replaced per year x CAC. Buyers replaced per year = buyers /
lifetime in years. For monthly churn, lifetime in months = 1 / monthly churn, so 10% a month
means 1.2 x buyers a year; do not compound it. If buyers do not repeat, use all buyers and a one-year lifetime. Also
check each buyer: annual gross margin x lifetime in years must exceed CAC. With no measured
churn, assume a lifetime and use it in both calculations. Only a measured zero churn skips
them. Winning the first base (buyers x CAC) is an upfront investment, so
state how it is funded and how long it takes to pay back. If the plan does not clear the floor,
that is a no-go signal regardless of how exciting the product is.

### Step 4: Build one buyer-avatar card per served segment

Fill the avatar template from `references/segments.md` for each segment you decided to
serve. Ground every field in the segment data, not invented demographics. Each card must
name: the language for product and support, the income band relative to the statutory
average wage under s.1 of the National Insurance Law (13,566 NIS per month as of January
2026), where they discover and where they buy, preferred payment, the top objections, the
trust triggers, and why the global pitch does not land as-is. The average wage is higher than what a typical
earner makes, so do not anchor pricing on it alone.

### Step 5: Localize the positioning angles

Translate the product's value into Israeli reality, not a translated US pitch:

- **Language and UX:** for consumer products, Hebrew-first and RTL (B2B: see Step 2b), with Arabic for the Arab segment where
  relevant. Go past "RTL": Hebrew that reads as machine-translated is a top trust-killer,
  mixed Hebrew/English/number lines break BiDi rendering, and date, phone, and address
  formats are local. Budget for a real Hebrew content writer, not a translation pass.
- **Pricing:** show consumers one total price in shekels, including any VAT that applies (18%
  for an authorized dealer or company; an exempt dealer generally does not charge VAT). The total-price rule is a legal duty, not a style preference: see the
  Consumer Protection Law point in Step 6. Whether a foreign digital seller must charge Israeli
  VAT is an open question for an adviser. VAT is a
  recurring budget-bill lever in Israel, so confirm the current rate before you lock a price.
  For the income benchmark, note which "average wage" you are using: 13,566 NIS per month is
  the statutory average wage under s.1 of the National Insurance Law. The CBS average per employee post for Israeli workers
  was 13,884 NIS in 2025. Either way, benchmark against local
  substitute prices, not US incomes. Interest-free installments (תשלומים) are an expectation,
  and they are themselves a pricing lever, not a footnote.
- **Payment rail:** the dominant business checkout is credit cards through local gateways
  and acquirers (for example Grow, formerly Meshulam). Before relying on a foreign gateway, confirm that it serves
  your entity's country and supports Israeli installments. Bit (Bank Hapoalim) and paybox (Discount Bank) dominate
  peer-to-peer transfers. A gateway can add Bit as a checkout option (Grow offers it beside
  cards, Apple Pay and Google Pay), so offer it as an extra method, but do not plan the whole
  commerce rail around "accept Bit".
- **Channels:** map the product to where Israelis actually transact. For digital and D2C:
  WhatsApp commerce, Facebook groups, Yad2, and local marketplaces, not just the app stores.
  For physical goods on shelves: getting on a shelf can run through an importer or
  distributor and through retail chains such as Shufersal, the largest supermarket chain. The real
  competitor is frequently a grey-market parallel importer selling the same brand cheaper, or
  buyers importing directly from foreign sites. The personal-import tax exemption is what
  makes "I will just order it from abroad" a real substitute: the exemption ceiling is
  around 75 dollars. Shipping, insurance and split-shipment rules can change this, and tobacco
  and alcoholic drinks are not exempt, so check the Tax Authority. From 75 to 500 dollars the
  buyer is exempt from customs duty only, so VAT and any other applicable tax still apply. Treat the
  ceiling as volatile: orders set it at 150 and then 130 dollars before a Knesset vote returned
  it to 75 on 1 June 2026, so re-check it before you build a pricing argument on it.
- **Trust:** Israeli buyers are price-aggressive and recommendation-driven. Local phone
  support, Israeli social proof, and a Hebrew interface raise trust more than a slick
  global brand. Also check whether a local copycat already cloned the product or whether the
  global incumbent already serves Israel directly in English.

### Step 6: Flag the regulatory and seasonality gates

These are gates that can kill a product before marketing even starts. Name the gates that
commonly arise for this product category, as questions to take to an advocate. Do not state
that a gate does or does not apply to this product, and do not decide whether an exemption or
exception covers it.

- **Official standards (תקן רשמי):** the Minister of Economy and Industry can declare a
  standard, in whole or in part, official and therefore mandatory, which can block import or
  sale of regulated goods until the required conformity
  route is met.
- **Food and cosmetics run through the Ministry of Health:** a business that makes, imports,
  exports or stores cosmetics wholesale must register in the cosmetics dealers register, and an
  importer of non-animal food needs an importer certificate. Cosmetics and animal-derived food
  carry further pre-market requirements, so take the specific product to the Ministry before
  you set a launch date.
- **Sector licensing:** ask whether the activity needs a sector license or regulator approval,
  for example regulated financial services or health services.
- **Hebrew labeling:** consumer-product packaging generally must carry clear Hebrew labeling,
  even when imported.
- **Consumer Protection Law:** deceptive marketing is prohibited (s.2(a) bans anything
  liable to mislead a consumer on a material matter). Separately, s.17ד says a price
  advertised or quoted to a consumer may only be the total price (המחיר הכולל, defined in
  s.17א to include VAT, fees and every mandatory charge) and only in Israeli currency. So a
  consumer price in dollars, or one that adds VAT at checkout, is unlawful rather than merely
  unappealing. The s.17ז carve-outs are narrow. The chapter does not apply to goods for
  sale outside Israel, services performed wholly outside Israel, or, on conditions, hotel and
  self-drive car-rental services for tourists (First Schedule, Part A). Part B separately lets
  a short list (mainly international transport, port and airport charges, duty-free goods and
  outbound tourism) show the total price in foreign currency at a set exchange rate; it does
  not permit adding VAT at checkout. s.1 defines a consumer as someone buying for mainly
  personal, household or family use. When a tax rate changes, s.17ה allows seven days of
  displaying a price without the change, with a prominent notice at the place of business. It
  refers to ss.17א to 17ג, not to the advertising rule in s.17ד.
- **Cancellation rights, which are a product requirement and not a support policy:** the same
  law gives a distance-selling cancellation right under s.14ג(ג). For goods, the consumer may
  cancel until fourteen days after receiving the goods or the required written disclosure
  document, whichever is later. For a service, the fourteen days run from the transaction or
  that document, whichever is later; a one-off service must be cancelled at least two
  non-rest days before it is due, while a continuing service can be cancelled in the window
  even after it started. So a missing disclosure document keeps the window open. Under s.14ג1(ג)
  the window is four months for people with disabilities, consumers aged 65 or over, and new
  olim (within five years of their certificate) when the sale included a conversation with
  the seller, including one over electronic communication, which directly affects a
  phone-sold olim or senior funnel. s.14ג(ד) excludes
  perishables, made-to-order goods, opened recordable media, "information" as defined in the
  Computers Law, and hospitality, travel or leisure services cancelled within seven non-rest
  days of the service. Whether a digital product falls inside the information exclusion is a
  question for an advocate; do not assume either way. If the consumer cancels because of a
  defect, a mismatch, non-delivery or another breach, no cancellation fee may be charged.
  Otherwise the fee is capped at 5% or 100 NIS, whichever is lower, and a consumer who cancels
  a started continuing service pays for the part received (s.14ה).
- **Subscriptions and auto-renewal:** do not assume the law gives every plan a right to cancel
  at any time. s.13א1 gives that right for fixed-term deals only in the Fourth Schedule
  categories; whether this product is one is a question for an advocate. Once a continuing deal
  is validly cancelled it ends within three business days of the notice, or six if sent by
  registered mail (s.13ד(ג)). For a fixed-term plan, s.13א(ג) voids a clause that continues it
  past its end date, subject to the s.13א(ד) exceptions, and the seller normally needs the
  consumer's agreement to extend. A period at a discounted price or with another benefit can count
  as fixed-term even inside an open-ended plan, unless it is a limited-time reduction or benefit
  given without any condition, so raise intro prices and trials that convert to paid with an
  advocate. When charging by standing authorization, the seller generally must announce the end
  date 30 to 60 days ahead, show it on invoices in the last three months, and, if the consumer
  gave a mobile number, send an SMS 21 days before it. A site that sells online needs a dedicated, prominent cancellation link on its home page
  (s.14ט(ב)). Model the churn from all of this before you price an annual plan.
- **Who has to register for Israeli VAT:** the duty to show a consumer the total price is a
  separate question from whether you must register to collect VAT. For a non-resident digital
  service provider with no permanent establishment, Avalara's guide reports no low-turnover
  threshold and says registration and an Israel-resident VAT representative may be required.
  We could not confirm the Tax Authority's current position, so treat this as an open cost and
  timeline item, and ask the Israel Tax Authority or an Israeli tax adviser before you model
  the price. Imported physical goods raise their own customs and VAT questions.
- **Data and privacy:** Amendment 13 to the Privacy Protection Law (in force since 14 August
  2025) strengthened data-protection obligations and enforcement for anyone holding customer
  data, so a marketing database is itself a compliance responsibility. Treat this as enforced
  rather than theoretical: the Privacy Protection Authority issued its first administrative
  fine under the amendment in July 2026, against an HMO that reported a security incident
  late.
- **Marketing consent (anti-spam law, s.30א of the Communications Law):** advertising by fax,
  auto-dialer, SMS or "electronic message" requires the recipient's prior, explicit, written
  consent, and written includes an electronic message or recorded call. Treat a pre-checked box
  as not explicit. The electronic-message definition is technology-based, so the safe reading
  is that promotional WhatsApp broadcasts are covered too. This is separate from Amendment 13. Two narrow exceptions exist. Under s.30א(ג)
  you may market to someone who gave you their details while buying or negotiating to buy, if
  you told them then that the details would be used for marketing, gave them a chance to
  refuse, and the message concerns a similar product or service. Under s.30א(ב) one single
  message to a business, asking it to agree to receive advertising, is not a breach. A
  non-SMS message must be marked as advertising (in the title of an electronic message) and
  state the advertiser's name, address, contact details and a working way to refuse; an SMS
  needs the name and refusal contact. When a continuing deal ends, the customer counts as
  having refused further marketing (s.30א(ד)(2)). A court may award exemplary damages of up to
  1,000 NIS per message without proof of damage, and a sender in breach is presumed to have
  acted knowingly unless it proves otherwise. A spam class action is possible, but s.20(ה) of
  the Class Actions Law bars exemplary damages in one.
- **Do-Not-Call register (s.16ב and s.16ג):** a seller or anyone on its behalf may not make a
  marketing call, including over electronic communication, to a consumer's number listed in the
  register, and must verify the number first. A call by an outsourced center is attributed to
  the seller too. The Sixth Schedule holds the exceptions, so build the check into any phone
  funnel.
- **Seasonality:** demand swings around the Jewish-holiday calendar (Rosh Hashana, Pesach,
  Sukkot), Ramadan for the Arab segment, the August vacation, and reserve-duty (miluim)
  call-ups that disrupt B2B. Check whether your demand evidence overlaps a security event or
  a major call-up, since either can distort consumer demand too.
- **Election and coalition timing:** the 26th Knesset was elected on 27 October 2026, and as
  of 23 November 2026 coalition talks had not yet produced a government. Until a new
  government passes a budget, treat budget-driven inputs such as VAT and the personal-import
  ceiling as unsettled, and re-check them before you lock a price. For any later campaign,
  expect attention and ad inventory to tighten. If the product is near a political or civic
  theme, check current platform policy and Israeli election rules, including the disclosure
  duty on deep-fake (נחזות עמוקה) election propaganda, before planning a campaign.

### Step 7: Write the viability verdict (go / pivot / no-go)

Combine the evidence into one explicit recommendation:

- **Go:** at least one reachable segment plan clears the cost floor, the channel fit is real,
  the early-win fraction is a justified assumption with any paid incumbent weighed against it,
  and the plan budgets the time and cost of resolving the flagged regulatory questions with an
  advocate.
- **Pivot:** the demand exists but the global plan must change first (segment focus, language, price model, or a restriction the user or their advocate has already confirmed). Name exactly what must change.
- **No-go:** the serviceable market is too small, a free local substitute owns the job, or a
  restriction the user or their advocate has already confirmed breaks the economics.

Every Go or Pivot states that it is commercial and conditional on that legal check.

End the report with the global-vs-Israel delta: a short list of what is true globally that
is not true in Israel, and what the founder must change to win here.

## Examples

**Example 1: Global SaaS founder.** User: "We have a US time-tracking SaaS at 12 dollars a
month. Will it work in Israel?" The skill sizes the secular Hebrew SMB segment bottom-up,
finds the SOM is small, flags that the SMB tier should move to shekels, notes that the
total-price rule protects consumers and that whether this plan's sales are consumer sales,
including self-serve signups, is a question for an advocate, flags that the channel is WhatsApp and
Facebook groups rather than paid search, and returns a "pivot" verdict: viable only if repriced and Hebrew-localized
with a free tier to beat the "good enough Excel" substitute.

**Example 2: Israeli D2C founder.** User: "אני רוצה למכור מוצרי טיפוח טבעיים, למי כדאי
לכוון?" The skill builds avatars for the secular mainstream and a modesty-aware Haredi
sub-segment, flags the Hebrew-labeling and Ministry of Health cosmetics questions for an
advocate, prices against local substitutes, and recommends a commercial "go", conditional on
that check, with a center-first launch and a card checkout with installments, with Bit added
through the gateway.

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

- **Treating Israel as one Hebrew market.** Agents routinely size off the full 10.305
  million and assume mainstream Instagram ads reach everyone. The Haredi (14.3%) and
  Arab-Israeli (21.1%) segments have separate channels and languages; sizing and avatars
  must be per segment.
- **Pricing in dollars.** Israeli buyers expect shekel prices with installments. Agents treat
  this as a conversion tip, but for a consumer price s.17ד permits only the total price and only
  in Israeli currency, so a dollar price, or adding a tax that applies at checkout, is a breach
  unless a specific s.17ז carve-out covers it, which is a question for an advocate.
- **Forgetting the regulatory gate exists.** For physical goods, agents jump to marketing
  and skip the official-standard (תקן רשמי), Ministry of Health and Hebrew-labeling gates that
  can block import or sale entirely. Raise them with an advocate before you size the upside.
- **Building an email funnel without consent.** An opt-out mailing list does not give the prior
  explicit consent the anti-spam law requires, and a pre-checked box should be treated as not
  explicit. Consent must be prior, explicit, and in writing unless the narrow s.30א(ג)
  existing-customer exception is fully met. This applies to email and SMS and, on the safe
  reading, to WhatsApp broadcasts. A
  customer database also carries Amendment 13 duties. Do not conflate the two: the opt-in is the
  anti-spam law, the data obligations are Amendment 13.
- **Treating Bit or paybox as the whole checkout.** Bit and paybox began as peer-to-peer apps.
  The main business rail is credit cards through a local gateway with installments. Bit can be
  added through a gateway as an extra option, but "just accept Bit" is a wrong checkout answer.
- **Auto-renewing by default.** Copying a US subscription flow, including an intro price or a
  trial that converts to paid, can breach s.13א, and a missing cancellation link can breach
  s.14ט. Raise both with an advocate before you model annual-plan retention.
- **Cold-calling from a lead list.** A live sales call to a number in the Do-Not-Call register
  is prohibited (s.16ג), even through an outsourced call center.
- **Assuming "no competitor in Israel."** The real competitor is often a free WhatsApp group,
  an Excel sheet, a Yad2 listing, a grey-market parallel importer selling the same brand
  cheaper, or buyers importing directly from abroad. List the local substitute, and the
  import-it-yourself substitute, before claiming a gap.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| CBS population release | https://www.cbs.gov.il/he/mediarelease/DocLib/2026/282/11_26_282b.pdf | Total population, Jewish/Arab/foreign split, average wage |
| IDI Haredi Yearbook 2025 | https://www.idi.org.il/haredi/2025/?chapter=62168 | Haredi share, median age, youth share |
| PwC Israel tax summary | https://taxsummaries.pwc.com/israel/corporate/other-taxes | Current standard VAT rate |
| Standards Institution of Israel | https://www.sii.org.il/he/israelistandards/ | Official-standard (תקן רשמי) and import rules |
| Consumer Protection Law (Nevo) | https://www.nevo.co.il/law_html/law00/70305.htm | Deception ban, price display, cancellation and renewal |
| Hebrew labeling requirement | https://weksler-davidovich.co.il/consumer-protection-labeling/ | Mandatory Hebrew labeling on consumer products |
| Privacy Amendment 13 (gov.il) | https://www.gov.il/he/pages/13_amendment | Data-protection obligations for customer data |
| ISOC-IL on the 2026 election AI-disclosure rules | https://www.isoc.org.il/regulation-digital-services/deep-fake-election-law | Deep-fake disclosure duty and the prescribed logo |

## Recommended MCP Servers

No MCP server is required: the skill reasons over the bundled segment data and the user's
product description. Three published MCPs turn parts of the analysis from estimate into
measurement, and are worth adding when the user has them:

| MCP | What It Adds |
|-----|-------------|
| [Israeli Supermarket Prices](https://agentskills.co.il/he/mcp/supermarket-prices) | Real shelf prices across 35+ chains, so the Step 5 "benchmark against local substitute prices" step uses actual Israeli prices instead of a guess. |
| [Israeli CBS](https://agentskills.co.il/he/mcp/israeli-cbs) | CBS statistical series and price indices for sizing inputs and for CPI-adjusting a spend assumption. |
| [Israel Statistics](https://agentskills.co.il/he/mcp/israel-statistics) | CPI and producer/consumer index series, useful when a price assumption has to hold over a multi-year plan. |

For live competitor research, the agent's built-in web access is still the right tool.

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

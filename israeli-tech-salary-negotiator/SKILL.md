---
name: israeli-tech-salary-negotiator
description: Benchmark tech salaries in the Israeli market and craft data-driven negotiation strategies. Use when preparing for a salary negotiation, evaluating a job offer, or comparing total compensation packages at Israeli tech companies (startups, enterprises, multinational R&D centers). Covers base salary ranges by role and seniority, equity and options valuation, Israeli benefits analysis (pension, keren hishtalmut, car allowance, vacation), and counter-offer scripting with market data. Do NOT use for non-tech roles, freelance rate setting, or salary negotiations outside Israel.
license: MIT
allowed-tools: Bash(python:*) WebFetch Read
compatibility: Requires Claude Code or compatible AI coding agent
---

# Israeli Tech Salary Negotiator

## Instructions

### Step 1: Gather the User's Context

Before performing any analysis, collect the following information from the user:

1. **Role** (e.g., Backend Engineer, DevOps, Product Manager, Data Scientist)
2. **Seniority level** (Junior, Mid, Senior, Staff, Principal/Director)
3. **Location** (Tel Aviv, Haifa, Jerusalem, Beer Sheva, Remote)
4. **Company type** (Early-stage startup, Growth startup, Enterprise, Multinational R&D center)
5. **Current offer or salary** (if they have one)
6. **Years of experience**

If the user does not provide all details, make reasonable assumptions based on context and note them explicitly.

### Step 2: Benchmark Against Market Data

Consult `references/israeli-tech-salary-data.md` to find the relevant salary range for the user's role, seniority, and location. Present the data as:

- **25th percentile** (below market)
- **Median** (market rate)
- **75th percentile** (above market)
- **90th percentile** (top of market, typically FAANG or top-tier startups)

Adjust for company type:
- Early-stage startups: typically 10-20% below median but with larger equity grants
- Growth startups (Series B+): at or slightly above median
- Enterprises (Check Point, Amdocs): at median with strong benefits
- Multinational R&D (Google, Meta, Apple, Amazon, Microsoft): 75th-90th percentile

### Step 3: Analyze Total Compensation

Consult `references/israeli-benefits-guide.md` and use `scripts/salary-calculator.py` to compute total compensation:

```bash
python scripts/salary-calculator.py --base <base_salary> --pension-employee 6.0 --pension-employer 6.5 --keren-employee 2.5 --keren-employer 7.5 --vacation-days 18 --car-allowance 2500 --meal-allowance 1000
```

Break down the package into:
1. **Base salary** (gross monthly)
2. **Pension contributions** (employer portion, 6-6.5% of base)
3. **Keren Hishtalmut** (employer portion, 7.5% of base, tax-exempt after 6 years)
4. **Car allowance** (if applicable, NIS 2,000-5,000/month)
5. **Meal/recreation allowances**
6. **Equity/options** (valued using standard methods)
7. **Annual bonus** (if applicable)
8. **Vacation days** (monetary value)

Present the total annual compensation and compare it to market benchmarks.

### Step 3.5: Factor in the Section 45a Pension Tax Credit (Net Pay)

When a user is comparing two offers, or weighing a raise that crosses the pension-credit ceiling, the gross number alone is misleading. Income Tax Ordinance Section 45a (סעיף 45א) gives the employee a **35% tax credit** on the employee's mandatory pension contribution, up to an annual contribution ceiling. In 2026:

- **Pension-credit qualifying salary ceiling**: 9,700 NIS/month (116,400 NIS/year)
- **Qualifying contribution ceiling**: 679 NIS/month (8,148 NIS/year), equal to 7% of the qualifying salary
- **Maximum annual credit**: 35% x 8,148 = **2,851.8 NIS/year** (~238 NIS/month off income tax)

The credit is applied on the payslip automatically when the employee files Tofes 101 with pension data, so both offers below the ceiling typically give the same credit, and the net-pay comparison reduces to the usual marginal-rate math. Where the credit materially changes the comparison:

1. **Offers that replace pension with "global" cash salary** (common in foreign-remote roles). The employee loses the 45a credit entirely. That is ~2,850 NIS/year of lost net pay on top of the lost pension savings themselves.
2. **Low-base-salary offers paired with aggressive equity**. If the base is below the 9,700 NIS/month ceiling and the employee maxes out 7% pension contributions, the 45a credit fully offsets income tax on that contribution slice. Comparing a 9K/month base (with full credit) to a 12K/month base (partial credit) requires computing net, not gross.
3. **Severance-only ("pitzuim only") deals, or employer-only pension with no employee contribution**. The employee has no contribution to claim the credit on, which quietly shifts the net-pay calculation.

**Worked example**: Senior Backend Engineer comparing two offers, both nominally 40,000 NIS/month gross.

- **Offer A** (standard Israeli tech package): base 40,000, employee pension 6%, full 45a credit. Employee pension contribution 40,000 x 6% = 2,400 NIS/month, but only the first 679 NIS/month is credit-qualifying. Monthly 45a credit = 679 x 35% = **238 NIS**. The remaining 1,721 NIS of contribution is neither credited nor deducted (it is above the 45a cap, and employees cannot claim a Section 47 deduction on this slice since 47 is scoped to self-employed contributions). Net-of-credit cost to the employee of the mandatory 6% pension: 2,400 - 238 = 2,162 NIS.
- **Offer B** (foreign remote, "global" contract): base 40,000 paid as cash salary, no Israeli pension, no Section 14 severance. No 45a credit. The employee could open a voluntary pension plan on their own and claim a different tax benefit under Section 47 (deduction, not credit), but the employer contribution is gone. **Annual net-pay delta vs Offer A: 2,851 NIS from the lost 45a credit alone, plus ~71K/year of lost employer pension + severance.**

Run `scripts/salary-calculator.py` with `--pension-employee` set to the actual employee share, then manually subtract the 45a credit (238 NIS/month if contribution >= 679, or 35% of actual contribution if below) to get a net-pay comparison. Present both the gross and post-credit net numbers to the user so they understand what a "same base salary" offer really pays.

See `references/israeli-benefits-guide.md` Section 1.1 for the full 45a mechanics and edge cases (above-ceiling salary, part-time work, multiple employers).

### Step 4: Evaluate Equity and Options

If the offer includes equity, analyze it:

1. **Stock options (ISO/NSO)**: Calculate potential value based on strike price, current valuation, and vesting schedule (typically 4 years with 1-year cliff in Israel)
2. **RSUs**: Calculate current value and projected value
3. **For startups**: Apply a standard discount (50-80% for early stage, 20-40% for late stage) to account for illiquidity risk
4. **Tax implications**: Note the Israeli tax treatment (capital gains tax on options at 25%, RSUs under Section 102 trust can also qualify for 25% capital gains tax)

### Step 5: Identify Negotiation Leverage Points

Based on the analysis, identify the user's strongest negotiation points:

1. **Market gap**: If current offer is below median, quantify the gap
2. **Competing offers**: Guide user on how to leverage other offers
3. **Unique skills**: Identify high-demand skills (e.g., ML, security, distributed systems) that justify premium
4. **Location arbitrage**: Remote work from lower cost-of-living areas while being paid Tel Aviv rates
5. **Benefits optimization**: Sometimes easier to negotiate benefits than base salary (extra vacation, keren hishtalmut ceiling, signing bonus)

### Step 6: Draft the Counter-Offer

Generate a professional counter-offer communication (email or talking points) that:

1. Expresses enthusiasm for the role
2. Presents specific market data to justify the request
3. Proposes a specific number (aim for 75th percentile if offer is at median)
4. Includes fallback positions (e.g., "If base salary is fixed, I would appreciate X additional vacation days or a signing bonus of Y")
5. Maintains a collaborative tone throughout

Tailor the language to Israeli business culture, which tends to be direct and informal compared to US norms.

### Step 7: Prepare for the Negotiation Conversation

Provide the user with:

1. **Opening statement** for the negotiation meeting
2. **Responses to common pushbacks** ("This is our standard offer," "We don't negotiate for this level," "Budget is fixed")
3. **Questions to ask** that demonstrate value and gather information
4. **Walk-away criteria** to help the user decide their minimum acceptable offer

## Examples

### Example 1: Evaluating a Senior Backend Offer in Tel Aviv

User says: "I got an offer for a Senior Backend Engineer role at a Series B startup in Tel Aviv. They're offering 38K NIS base, 0.1% equity, standard benefits. Is this good?"

Actions:
1. Look up Senior Backend Engineer salary ranges in Tel Aviv from `references/israeli-tech-salary-data.md`
2. Compare 38K against the median (approximately 40-42K for Senior Backend in Tel Aviv)
3. Analyze benefits using `references/israeli-benefits-guide.md`
4. Run `scripts/salary-calculator.py` with the offered package
5. Evaluate 0.1% equity based on typical Series B valuations
6. Draft a counter-offer strategy targeting 42-44K base with justification

Result: Deliver a comprehensive analysis showing the offer is approximately 7% below median for the role and location, with a specific counter-offer email draft requesting 43K base, maintaining the equity grant, and suggesting a signing bonus of 10-15K NIS to bridge the gap.

### Example 2: Comparing Two Offers with Different Structures

User says: "I have two offers. Offer A: Google Tel Aviv, L4, 52K base, RSUs worth $80K over 4 years, 15% bonus. Offer B: A late-stage startup, Staff Engineer, 45K base, 0.3% options, no bonus but unlimited vacation."

Actions:
1. Benchmark both roles against market data from `references/israeli-tech-salary-data.md`
2. Calculate total compensation for Offer A including RSU vesting schedule and bonus
3. Calculate total compensation for Offer B with options valuation (apply 30% illiquidity discount for late-stage)
4. Compare benefits packages using `references/israeli-benefits-guide.md`
5. Run `scripts/salary-calculator.py` for both offers side by side
6. Factor in career trajectory differences (big tech vs. startup leadership)

Result: A side-by-side comparison table showing Offer A at approximately 900K NIS total annual compensation vs. Offer B at approximately 750-850K (depending on startup outcome), with a recommendation matrix based on risk tolerance, career goals, and financial needs.

### Example 3: Negotiating Keren Hishtalmut and Benefits

User says: "I'm a mid-level DevOps engineer in Haifa. My company offers the minimum pension (6%+6.5%) and no keren hishtalmut. I want to negotiate better benefits."

Actions:
1. Look up Mid DevOps salary ranges in Haifa
2. Calculate the monetary value of upgrading pension to 6%+6.5% and adding keren hishtalmut at 2.5%+7.5%
3. Run `scripts/salary-calculator.py` comparing current vs. desired benefits packages
4. Quantify the annual difference (typically 30-50K NIS per year in additional employer contributions)
5. Draft talking points for approaching HR about benefits upgrade

Result: A clear breakdown showing that upgrading to full benefits adds approximately 40K NIS annually in employer contributions, with a script for the conversation framed as "bringing my package in line with market standard" rather than asking for a raise.

## Bundled Resources

### Scripts
- `scripts/salary-calculator.py` - Calculate total annual compensation from base salary, benefits, equity, and allowances. Run: `python scripts/salary-calculator.py --help`

### References
- `references/israeli-tech-salary-data.md` - Comprehensive salary ranges by role, seniority, and city for Israeli tech positions. Consult when benchmarking any salary offer or comparing compensation across roles.
- `references/israeli-benefits-guide.md` - Detailed guide to Israeli employment benefits including pension, keren hishtalmut, vacation, car allowance, and meal benefits. Consult when evaluating the non-salary components of a compensation package.

## Gotchas

- Keren Hishtalmut (education fund) is a major Israeli benefit worth 7.5% of base salary from the employer, tax-exempt after 6 years. Agents unfamiliar with Israeli compensation may omit it entirely, undervaluing total compensation by tens of thousands of NIS annually.
- Israeli sick day payment structure differs from the US: day 1 is unpaid, days 2-3 at 50%, day 4+ at 100%. Agents may apply US-style sick leave when comparing packages.
- Stock options in Israeli startups typically use Section 102 trustee arrangements for favorable 25% capital gains tax treatment. Agents may apply US tax rates (which can be higher) when evaluating equity value.
- Israeli tech salaries are quoted as gross monthly (bruto chodshi), not annual. An offer of "40K" means 40,000 NIS per month. Agents may interpret this as annual, drastically miscalculating the package.
- The Israeli tech salary market shifts rapidly, especially in hot domains like AI/ML and cybersecurity. Salary benchmarks from even 12 months ago may be significantly outdated.
- The Section 45a pension tax credit (35% on employee contributions, capped at 679 NIS/month in 2026) is easy to omit when comparing Israeli employment against foreign-remote "global" contracts. Agents that only compare gross salary miss roughly 2,851 NIS/year of net pay plus the entire employer pension and severance stack (about 14.83% of gross). Any comparison between an Israeli local contract and a foreign employer-of-record contract must account for 45a explicitly.

## Reference Links

Use these official and authoritative sources to verify contribution rates, ceilings, and other legal figures before quoting them in a negotiation. Israeli thresholds update annually, so always cross-check.

| Source | URL | What to Check |
|---|---|---|
| Kol-Zchut: Annual Vacation | https://www.kolzchut.org.il/he/%D7%97%D7%95%D7%A4%D7%A9%D7%94_%D7%A9%D7%A0%D7%AA%D7%99%D7%AA | Statutory minimum vacation days by tenure for a 5-day workweek |
| Kol-Zchut: Keren Hishtalmut | https://www.kolzchut.org.il/he/%D7%A7%D7%A8%D7%9F_%D7%94%D7%A9%D7%AA%D7%9C%D7%9E%D7%95%D7%AA | Tax-qualifying salary ceiling, contribution rates, 6-year tax exemption rules |
| Kol-Zchut: Pension Tax Credit (Section 45a) | https://www.kolzchut.org.il/he/%D7%96%D7%99%D7%9B%D7%95%D7%99_%D7%9E%D7%9E%D7%A1_%D7%94%D7%9B%D7%A0%D7%A1%D7%94_%D7%91%D7%92%D7%99%D7%9F_%D7%94%D7%A4%D7%A8%D7%A9%D7%95%D7%AA_%D7%9C%D7%91%D7%99%D7%98%D7%95%D7%97_%D7%A4%D7%A0%D7%A1%D7%99%D7%95%D7%A0%D7%99 | 35% tax credit rate, annual contribution ceiling, qualifying-salary ceiling for Section 45a |
| Pensuni: 2026 Ceilings | https://pensuni.com/?p=827 | Current-year pension ceilings, average wage, mandatory contribution rates |
| Bituach Leumi | https://www.btl.gov.il/ | National Insurance and health tax rates that drive gross-to-net deltas |
| Israel Tax Authority | https://www.gov.il/en/departments/israel_tax_authority | Income tax brackets, credit points, Section 102 trustee option taxation |
| Supermarker (TheMarker) | https://www.supermarker.themarker.com/Gemel/HishtalmutFundTaxBenefits2017.aspx | Annual deposit ceilings for keren hishtalmut and kupot gemel |

## Troubleshooting

### Error: "Salary data seems outdated or does not match my experience"

Cause: Salary ranges in the reference data represent market averages and may not reflect hyper-growth periods, specific company tiers, or niche specializations (e.g., ML infrastructure, blockchain). The Israeli tech market can shift rapidly, especially in hot domains.

Solution: Use the reference data as a baseline and adjust using these multipliers: (1) For FAANG and tier-1 companies, add 20-40% to the listed ranges. (2) For niche specializations in high demand, add 10-25%. (3) Ask the user if they have data points from peers or recruiters to calibrate further. WebFetch can also be used to check recent salary surveys from sources like Glassdoor Israel or levels.fyi.

### Error: "Equity valuation is uncertain for early-stage startups"

Cause: Pre-Series A and Seed stage companies often lack reliable valuation data, making options grants difficult to value with confidence. The reference data applies standard discounts, but actual outcomes vary enormously.

Solution: Apply a conservative approach: (1) For pre-seed/seed, treat options as worth 0-20% of paper value. (2) For Series A, use 20-40% of paper value. (3) For Series B+, use 40-70% of paper value. Always present equity as a "potential upside" scenario rather than guaranteed compensation, and ensure the base salary alone meets the user's minimum needs.

### Error: "Python script fails with ModuleNotFoundError"

Cause: The `salary-calculator.py` script uses only Python standard library modules, but may fail if Python 3 is not available or the wrong Python version is invoked.

Solution: Ensure Python 3.6+ is installed. Run `python3 scripts/salary-calculator.py --help` instead of `python`. On macOS, `python` may still point to Python 2 on older systems.

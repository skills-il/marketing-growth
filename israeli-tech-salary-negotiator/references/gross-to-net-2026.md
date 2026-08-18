# Gross-to-Net Pay in Israel (2026)

The most common question a candidate asks is "what will I actually take home?" A gross salary figure (`bruto chodshi`) is not what lands in the bank account. This reference walks the gross-to-net calculation for a salaried Israeli tech employee using 2026 figures, so an offer comparison can be presented in net terms, not just gross.

**Last verified**: May 2026. Israeli thresholds update annually (and sometimes mid-year, as the April 2026 bracket revision shows). Always cross-check against the official sources at the bottom before quoting a number in a negotiation.

---

## The three deductions from gross salary

A salaried employee's net pay is gross salary minus three things:

1. **Income tax** (`mas hachnasa`) - progressive brackets, reduced by credit points.
2. **National Insurance** (`Bituach Leumi`) - the employee's own contribution, two-tier.
3. **Health tax** (`mas briut`) - collected together with Bituach Leumi, also two-tier.

Pension and Keren Hishtalmut employee contributions are also withheld, but those are savings, not taxes. The `salary-calculator.py` script already reports the "pre-tax effective pay" after pension and keren are removed. This reference covers the tax layer that sits on top.

---

## 1. Income tax brackets (2026)

Israel taxes monthly income progressively. The brackets below reflect the **April 2026 revision** (the 20% bracket was widened and the 31% bracket shifted up). Brackets are not indexed to inflation in 2026, they were set by the revision.

| Monthly income (NIS) | Marginal rate |
|---|---|
| 0 - 7,010 | 10% |
| 7,011 - 10,060 | 14% |
| 10,061 - 19,000 | 20% |
| 19,001 - 25,100 | 31% |
| 25,101 - 46,690 | 35% |
| 46,691 - 60,130 | 47% |
| above 60,130 | 47% + 3% surtax = 50% |

The 3% surtax (`mas yesef`) applies on annual taxable income above 721,560 NIS (roughly 60,130 NIS/month).

These are **marginal** rates: each slice of salary is taxed at its own bracket rate, not the whole salary at the top rate.

### Credit points (`nekudot zikui`)

Credit points are a flat reduction of the income tax bill, applied after the bracket math. In 2026 the value is **242 NIS per point per month** (2,904 NIS/year). The value is **frozen for 2026** (no inflation update).

Typical entitlements:

- Every Israeli resident: **2.25 points**
- Women: an additional **0.5 point** (2.75 total)
- Each child (for the parent claiming them), new immigrant status, completed academic degree, military reserve service, and other situations add more points.

A male tech employee with no extra entitlements gets 2.25 points = 544.5 NIS/month knocked off the income tax bill. A woman with no extra entitlements gets 2.75 points = 665.5 NIS/month. If credit points exceed the computed tax, the excess is generally not refunded as cash (it just zeroes the income tax).

### Worked income-tax example: 40,000 NIS/month gross, male, 2.25 points

Income tax is computed on the salary after the employee pension contribution is deducted (pension contributions up to the ceiling reduce taxable income). For simplicity here, assume the taxable base is the full 40,000 NIS (a precise calculation would first subtract the deductible pension slice).

| Slice | Amount in slice | Rate | Tax |
|---|---|---|---|
| 0 - 7,010 | 7,010 | 10% | 701.0 |
| 7,011 - 10,060 | 3,050 | 14% | 427.0 |
| 10,061 - 19,000 | 8,940 | 20% | 1,788.0 |
| 19,001 - 25,100 | 6,100 | 31% | 1,891.0 |
| 25,101 - 40,000 | 14,900 | 35% | 5,215.0 |
| **Gross income tax** | | | **10,022.0** |
| Less: 2.25 credit points | | | -544.5 |
| Less: Section 45a pension credit (see Section 1.1 of the benefits guide) | | | -238.0 |
| **Net income tax** | | | **~9,239.5** |

(The Section 45a credit is the 35%-of-employee-pension-contribution credit covered in `references/israeli-benefits-guide.md` Section 1.1. It is a credit, so it subtracts directly from the tax bill, the same way credit points do.)

---

## 2. National Insurance + 3. Health tax (employee side, 2026)

Bituach Leumi and `mas briut` are collected together and have the **same two-tier structure**. The split point in 2026 is **7,703 NIS/month** (the "reduced collection bracket", 60% of the average wage, raised from 7,522 in 2025). 2026 rates are unchanged from 2025; the threshold and ceiling rise each year with the average wage.

| Salary portion | National Insurance | Health tax | Combined |
|---|---|---|---|
| Up to 7,703 NIS/month | 1.04% | 3.23% | **4.27%** |
| 7,704 NIS/month up to the ceiling | 7.00% | 5.17% | **12.17%** |

The monthly contribution ceiling is **51,910 NIS** in 2026. Salary above the ceiling is not charged Bituach Leumi or health tax.

### Worked example: 40,000 NIS/month gross

| Slice | Amount | Combined rate | Charge |
|---|---|---|---|
| 0 - 7,703 | 7,703 | 4.27% | 328.9 |
| 7,704 - 40,000 | 32,297 | 12.17% | 3,930.5 |
| **Total Bituach Leumi + health tax** | | | **~4,259.4 NIS/month** |

---

## Putting it together: net pay on a 40,000 NIS/month offer

For a male Senior Backend Engineer, 40,000 NIS/month gross, 2.25 credit points, standard 6% employee pension and 2.5% employee keren:

| Line | Monthly (NIS) |
|---|---|
| Gross salary | 40,000.0 |
| Less: income tax (net of credit points + Section 45a) | -9,239.5 |
| Less: Bituach Leumi + health tax | -4,259.4 |
| Less: employee pension (6%) | -2,400.0 |
| Less: employee keren hishtalmut (2.5%) | -1,000.0 |
| **Net to bank account** | **~23,101.1** |

So a "40K offer" lands as roughly **23,000-23,500 NIS** in the bank, before factoring in any taxable benefits (`shovi rechev` for a company car, partially taxable meal allowances) that would push the tax up. Pension and keren are not lost money, they are forced savings, but they are not spendable take-home this month.

This is why an offer comparison should always show net, not just gross: two offers with the same gross can produce different net pay once company-car tax value, allowance taxability, and credit-point differences (for example a candidate with children) are factored in.

### How to use this in an offer comparison

1. Start from gross monthly salary.
2. Compute income tax via the bracket table, then subtract credit points (242 NIS x point count) and the Section 45a credit.
3. Compute Bituach Leumi + health tax via the two-tier table.
4. Subtract employee pension and keren contributions (savings, but not take-home).
5. Present **both** the gross figure and the net-to-bank figure to the candidate.
6. For company-car offers, add the `shovi rechev` to the taxable base before step 2, since it is taxed as income even though no cash changes hands.

Use `scripts/salary-calculator.py` for the employer-cost and pre-tax effective-pay side, and this reference for the tax layer that converts pre-tax pay into net-to-bank.

---

## Caveats

- The April 2026 bracket revision is reflected above. If a newer revision lands, re-verify against the Tax Authority.
- The worked examples tax the full gross for simplicity. A precise payslip first deducts the deductible portion of the pension contribution from the taxable base, which slightly lowers the income tax. Treat the net figures here as a close estimate, not a payslip-exact number.
- Annual `tium mas` (tax coordination) and year-end reconciliation can change the effective annual figure, especially for employees who changed jobs mid-year or have multiple employers.
- This reference covers salaried employees (`sachir`). Self-employed (`atzmai`) contributors have different Bituach Leumi rates and claim pension benefits under Section 47, not Section 45a.

## Sources

- Israel Tax Authority (income tax brackets, credit points): https://www.gov.il/en/departments/israel_tax_authority
- Bituach Leumi, employee contribution rates: https://www.btl.gov.il/Insurance/Rates/Pages/לעובדים שכירים.aspx
- Kol-Zchut, credit points (`nekudot zikui`): https://www.kolzchut.org.il/he/נקודות_זיכוי_ממס_הכנסה
- Globes, April 2026 revised income tax brackets: https://en.globes.co.il/en/article-revised-income-tax-brackets-boost-march-salary-1001539434

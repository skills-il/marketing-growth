# Israeli Employment Benefits Guide

A comprehensive guide to Israeli tech employment benefits, covering mandatory and common voluntary benefits. Understanding these components is essential for evaluating total compensation.

---

## 1. Pension (Pensia)

### Mandatory Contributions (2026)

By Israeli law, employers must provide pension contributions after a qualifying period. Rates below have been in force since the 2017 expansion order.

| Component | Minimum | Common in Tech | Maximum |
|---|---|---|---|
| Employee contribution | 6.0% | 6.0% | 7.0% |
| Employer contribution (tagmulim) | 6.5% | 6.5% | 7.5% |
| Employer severance component | 6.0% | 8.33% | 8.33% |

**Key notes**:
- The severance component (Pitzuim) at 8.33% means the employer pre-funds severance pay (1 month per year of employment, which equals 8.33% monthly)
- **Section 14 is a written arrangement, not a contribution rate.** Depositing 8.33% does not by itself create it; Section 14 applies only where the employer and employee sign an arrangement under the General Approval. Ask to see it, do not infer it from the percentage.
- **What Section 14 gives and what it costs.** With it, the accumulated severance in the fund is the employee's on any exit, including resignation, which is the upside. Against that, the employee gives up the statutory calculation of one month per year on the **last** salary. For a tech employee whose salary rises sharply, the balance accumulated on each year's then-current salary can be well below `last salary x years`, and the top-up claim is waived. The faster the expected salary growth, the more the statutory route is worth, and this is decided at offer stage and cannot be revisited.
- Total employer pension cost: **12.5% of salary at the statutory floor** (6.5% tagmulim + 6% severance), or **14.83%** where the offer carries the 8.33% tech-market severance rate. Say which one you are using.
- The 6.5% employer tagmulim includes work-disability cover. By law the tagmulim (benefits) portion must stay at least 5%, and the employer's combined tagmulim-plus-disability contribution is capped at 7.5%; if the disability cover costs more, the employer tops up tagmulim so it never drops below the 5% floor.
- Multiple pension "ceilings" exist in Israel (do not confuse them):
  - **The ceilings that actually bite in 2026**, each a different number, so name which one you mean: employer pension contributions above **2.5x the average wage (34,422.5 NIS/month)** lose their exemption and are imputed to the employee; the keren hishtalmut qualifying ceiling is **15,712 NIS/month**; the Section 45a qualifying salary is **9,700 NIS/month**; the severance deposit ceiling is **3,800 NIS/month**. An earlier edition of this guide stated a single "~47,465 NIS/month tax-qualifying ceiling" which corresponds to none of these and could not be traced to any source; it has been removed.
  - **Comprehensive fund max insurable salary**: roughly 24,700 to 30,500 NIS/month in 2026 (varies with total contribution rate). Salary above flows to a supplementary fund.
  - **Comprehensive fund monthly premium ceiling**: 5,645 NIS/month in 2026 (20.5% of 2x average wage, 13,769 NIS).

### Pension Types
- **Comprehensive pension fund (Kupat Gemel)**: Most common, includes savings + insurance + severance
- **Old pension funds (Pensia Tiktivit)**: Closed to new members, very generous
- **Manager's insurance (Bituach Menahalim)**: More flexible, sometimes preferred by higher earners

### Monetary Value Example
For a 40K NIS/month base salary:
- Employer pension: 40,000 x 6.5% = 2,600 NIS/month
- Employer severance: 40,000 x 8.33% = 3,332 NIS/month
- **Total employer pension cost: 5,932 NIS/month (71,184 NIS/year)**

---

## 1.1 Section 45a Pension Tax Credit (Net-Pay Impact)

Employer pension contributions are only half of the story. The employee's own pension contribution also drives a tax benefit, and it shows up on the payslip as a credit (not a deduction). This is governed by Section 45a (סעיף 45א) of the Income Tax Ordinance and applies to every salaried employee (שכיר) whose payslip includes a pension deduction.

### Mechanics

When the employee files **Tofes 101** (Form 101) at the start of employment and declares the active pension arrangement, payroll automatically applies a 35% credit on the qualifying portion of the employee's contribution. The credit is deducted directly from the monthly income-tax liability, so it reduces net-to-pocket tax, not the taxable base.

### Ceilings (2026)

| Parameter | 2026 value |
|---|---|
| Credit rate | 35% of qualifying employee contribution |
| Qualifying salary ceiling (`הכנסה מזכה`) | 9,700 NIS/month (116,400 NIS/year) |
| Qualifying contribution ceiling | 679 NIS/month (8,148 NIS/year), equal to 7% of the qualifying salary |
| Maximum annual credit | 8,148 x 35% = **2,851.8 NIS/year** (~238 NIS/month) |

### Where the credit stops helping

Contributions above the 679 NIS/month ceiling do **not** generate additional Section 45a credit on the insured-salary slice, and that excess is funded from after-tax net pay.

There is a route on the **unpensioned salary** slice (`sachar lo mevutach`: overtime, company-car imputed value, commissions), but it is means-tested against insured salary and the test excludes most of this skill's audience:

| Insured salary | What the employee gets on the unpensioned slice |
|---|---|
| At or below 24,250 NIS/month (2026) | Section 47 **deduction** plus an additional Section 45a credit |
| Above 24,250 NIS/month (2026) | **No Section 47 deduction.** Only a Section 45a credit, at 5% of the unpensioned income, capped by the 9,700 NIS qualifying ceiling |

Worked example from the source: an employee on 30,000 NIS of which 25,000 is pensioned may deposit 5% of the 5,000 unpensioned slice, i.e. 250 NIS/month or 3,000 NIS/year, and receives a 35% credit on it, 1,050 NIS. Section 47 is therefore not a self-employed-only provision, but for a 40,000 NIS tech salary the deduction is out of reach and only the credit remains. State it that way rather than promising a deduction.

For a 40,000 NIS/month tech salary, the employee's mandatory 6% contribution is 2,400 NIS/month. Only the first 679 NIS of that produces a 238 NIS credit. The remaining 1,721 NIS is effectively after-tax savings into the pension fund.

### Who does Section 45a help the most

| Employee situation | Effect of Section 45a |
|---|---|
| Full-time Israeli tech employee with standard 6% employee pension | Fully receives the maximum credit (238 NIS/month ~ 2,852 NIS/year) |
| Employee below the 9,700 NIS/month ceiling with 7% pension contributions | Credit is smaller in absolute terms but covers 100% of the marginal tax on the contribution slice |
| Employee on a foreign-remote "global" contract with no Israeli pension | **Zero 45a credit.** Loses ~2,852 NIS/year on top of the missing pension and severance |
| Employee with multiple concurrent employers | The ceiling is per person, not per employer. HR must coordinate or the employee claims via annual tax return |
| Part-time employee below the contribution ceiling | Credit is proportional to actual contribution (35% of whatever was deducted, capped at 679 NIS/month) |

### How to factor Section 45a into an offer comparison

1. Compute the **monthly employee pension contribution** in NIS for each offer (employee-pension-rate x base salary).
2. If contribution >= 679 NIS/month, assume **238 NIS/month credit**.
3. If contribution < 679 NIS/month, credit is **35% of the actual monthly contribution**.
4. Add this credit to the net pay of Israeli-contract offers. Zero it out for foreign-contract offers that pay gross cash with no Israeli pension.
5. Present both gross and post-credit net figures when walking the user through the comparison.

### Common pitfalls

- Payroll systems need the Form 101 declaration to apply the credit. A new hire who forgets to tick the pension section on Form 101 will see the credit missing from their first payslip until corrected (the difference refunds via the annual תיאום מס or Tofes 135 at year-end).
- The 45a credit is separate from the Keren Hishtalmut tax treatment. Keren Hishtalmut gives tax-exempt growth on the fund itself; 45a gives a front-loaded monthly credit on the pension contribution. They stack.
- "Section 47" (סעיף 47) often comes up in the same breath. Section 47 is a **deduction** from taxable income, available to the self-employed and, for a salaried employee, on the portion of pay that is **not** pensioned. It is therefore not a self-employed-only provision. But the deduction is lost once insured salary exceeds 24,250 NIS/month (2026), leaving only a 45a credit on the unpensioned slice, so for most tech salaries the practical answer is credit, not deduction. See the table above.

### Sources
- Kol-Zchut: [Pension tax credit (Section 45a)](https://www.kolzchut.org.il/he/זיכוי_ממס_הכנסה_בגין_הפרשות_לביטוח_פנסיוני)
- Pensuni: [Tax benefits for salaried employees in pension funds 2026](https://pensuni.com/?p=1532)
- Supermarker: [Section 45a and 47 tax benefits in 2026](https://www.supermarker.themarker.com/Gemel/TaxBenefitsForKupatGemelAndHishtalmut.aspx)

---

## 2. Keren Hishtalmut

An Israeli-specific savings/investment fund with significant tax advantages. This is NOT mandatory but is standard in the tech industry and considered a core benefit.

### Contribution Rates

| Component | Common | Maximum tax-exempt |
|---|---|---|
| Employee contribution | 2.5% | 2.5% |
| Employer contribution | 7.5% | 7.5% |

### Tax Benefits
- Withdrawals after 6 years: **completely tax-exempt** (up to a ceiling)
- Withdrawals after 3 years: tax-exempt only if used for education/professional development
- The tax-exempt qualifying salary ceiling is **15,712 NIS/month in 2026** (max tax-benefited employer deposit: 1,178 NIS/month at 7.5%; the combined employer-plus-employee tax-benefited deposit is 1,571 NIS/month at 10%). Employer contributions on salary above this ceiling become taxable income for the employee, and the investment growth on the above-ceiling portion does NOT get the after-6-years capital-gains exemption either. So for a 40K+ tech salary the keren is only fully tax-advantaged on roughly the first 15,712 NIS of salary, factor that in before valuing a "7.5% on full salary" offer at face value.
- Many tech salaries sit above this ceiling, so you should verify whether your employer contributes the full 7.5% on actual salary or only up to the tax-benefited ceiling.

### Monetary Value Example
For a 40K NIS/month base salary:
- Employer contribution: 40,000 x 7.5% = 3,000 NIS/month
- Employee contribution: 40,000 x 2.5% = 1,000 NIS/month
- **Employer cost: 3,000 NIS/month (36,000 NIS/year)**
- **After 6 years, the accumulated amount (with investment returns) is withdrawn tax-free**

### Why Keren Hishtalmut Matters in Negotiation
This benefit is one of the most valuable in the Israeli market. An employer who does not offer it is effectively paying 7.5% less than one who does. Always negotiate for Keren Hishtalmut before negotiating base salary increases, as it is tax-advantaged for both parties.

---

## 3. Vacation and Time Off

### Statutory Minimums (by seniority)

There are **two** ladders for a 5-day workweek, and which one applies changes the answer by up to 6 net days at 9 years' tenure. Check which one the employer is under before quoting a minimum. Where both could apply, the employee is entitled to the **higher** of the two.

**Workplaces covered by the expansion order on the move to a 5-day working week (`tzav harchava`).** Do not assume this covers a given employer: the order does **not** apply to workplaces with fewer than four employees, to government or municipal companies, to employers where the move to a 5-day week is regulated by a collective agreement, or to employers the order's supervisory committee has excluded. Confirm before quoting this ladder as a floor.

| Years of tenure | Net days (actual working days) | Gross days (incl. weekly rest) |
|---|---|---|
| 1-4 years (from 01.01.2017) | 12 | 16 |
| 5 years | 12 | 16 |
| 6-8 years | 17 | 23 |
| 9 years and above | 23 | 31 |

**Workplaces on the statutory floor only:**

| Years of tenure | Net days | Gross days |
|---|---|---|
| 1-4 years (from 01.01.2017) | 12 | 16 |
| 5 years | 12 | 16 |
| 6 years | 14 | 18 |
| 7 years | 15 | 21 |
| 8 years | 16 | 22 |
| 9 years | 17 | 23 |
| 10 years | 18 | 24 |
| 11 years | 19 | 25 |
| 12 years | 20 | 26 |
| 13 years | 20 | 27 |
| 14 years and above | 20 | 28 |

Typical tech practice sits above both floors, commonly 18-22 net days early on and 22-26 for senior tenure, but the floor is what a negotiation can fall back on.

Note: Israeli law expresses vacation in gross days including the weekly rest day. Tech contracts almost always quote net working days, which is the smaller number, so always confirm which one an offer means.

### Additional Time Off
- **Sick days**: 1.5 days per month (18 per year), accumulating up to 90 days. First day unpaid, days 2-3 at 50%, day 4+ at 100%.
- **Recuperation pay (Dmey Havra'a)**: Annual lump sum based on tenure. **451.5 NIS per day, private sector, for havra'a year 2026** (1.7.2025 to 30.6.2026). The rate was updated on 18.08.2026 from the previous 418 NIS, and employers who already paid 2026 havra'a at 418 owe the difference retroactively, which is a legitimate thing for a candidate to raise. Public sector is 511.6 NIS. Typical entitlement is 5-10 days per year depending on tenure, and it is payable only after the first full year of employment (then retroactively from day one).
- **Jewish holidays**: 9 paid holiday days per year (Rosh Hashana, Yom Kippur, Sukkot, Simchat Torah, Pesach, Shavuot, Independence Day, etc.)
- **Reserve duty (Miluim)**: Employer must maintain salary during reserve duty; the state reimburses the employer.
- **Unlimited vacation**: Increasingly common in Israeli tech (especially startups), but verify the actual culture around taking time off.

### Monetary Value of Extra Vacation Days
Each vacation day is worth: monthly salary / 22 working days.
For a 40K salary: 40,000 / 22 = 1,818 NIS per day.
Negotiating 5 extra vacation days = approximately 9,090 NIS/year in value.

---

## 4. Car Allowance / Company Car

### Grades and Typical Values

| Grade | Monthly Gross Value | Tax Impact (Shovi Rechev) | Typical Level |
|---|---|---|---|
| No car benefit | 0 | 0 | Junior |
| Car allowance (cash) | 2,000 - 3,500 NIS | Taxed as income | Mid-level |
| Company car Grade 1-3 | 3,000 - 4,500 NIS equivalent | Shovi: 2,500 - 4,000 NIS | Senior |
| Company car Grade 4-6 | 4,500 - 6,500 NIS equivalent | Shovi: 4,000 - 6,500 NIS | Staff / Director |
| Company car Grade 7+ | 6,500 - 10,000 NIS equivalent | Shovi: 6,500 - 9,000 NIS | VP / C-level |

**Key notes**:
- "Shovi Rechev" (car value) is a taxable benefit added to your gross income for tax purposes
- Cash car allowance is often more transparent and tax-efficient than a company car
- Some companies offer a choice between company car and car allowance
- Parking costs in Tel Aviv (500-1,500 NIS/month) may or may not be included

---

## 5. Meal and Food Benefits

| Benefit | Typical Value | Tax Treatment |
|---|---|---|
| Cibus / 10bis card | 40-60 NIS/working day | **Taxable in most configurations, verify before valuing.** An employer-funded meal card redeemed off-premises is generally imputed to the employee as a benefit; the narrow exemption is for meals actually provided at the workplace. Do not book this line at face value in a net comparison until you have checked the current Tax Authority position for the specific arrangement |
| Monthly meal allowance | 800 - 1,200 NIS | Partially taxable |
| On-site cafeteria | Varies | Generally tax-exempt |
| Friday food budget | 100-200 NIS/week | Depends on structure |

**Annual value**: Approximately 10,000 - 15,000 NIS/year for standard meal benefits.

---

## 6. Additional Common Benefits in Israeli Tech

### Education and Professional Development
- Conference budget: 5,000 - 15,000 NIS/year
- Online learning subscriptions (Udemy, Coursera, etc.)
- Book/resource budget: 1,000 - 3,000 NIS/year
- Degree/certification reimbursement: partial or full

### Health and Wellness
- Supplementary health insurance (Bituach Briut Mashlim): 200-500 NIS/month value
- Dental insurance: 100-200 NIS/month value
- Gym membership or fitness budget: 200-400 NIS/month
- Mental health benefits (therapy sessions): increasingly common

### Work-Life Benefits
- Hybrid/remote work policy
- Home office setup budget: one-time 3,000 - 8,000 NIS
- Internet/phone stipend: 100-300 NIS/month
- Flexible hours

### Financial Benefits
- Annual bonus: 0-20% of base salary (highly variable)
- Signing bonus: 10,000 - 50,000 NIS (common when switching jobs)
- Relocation assistance (for moves within Israel): rare but possible
- Employee stock purchase plan (ESPP): typically 15% discount

### Insurance
- Life insurance (Bituach Chaim): often included in pension package
- Disability insurance (Ovdan Kosher Avoda): critical, usually 0.5-1.5% of salary
- Travel insurance for business trips

---

## 7. Total Compensation Calculation Template

For a Senior Engineer in Tel Aviv earning 42,000 NIS/month base:

| Component | Monthly | Annual |
|---|---|---|
| Base salary (gross) | 42,000 | 504,000 |
| Employer pension (6.5%) | 2,730 | 32,760 |
| Employer severance (8.33%) | 3,499 | 41,986 |
| Keren Hishtalmut employer (7.5%) | 3,150 | 37,800 |
| Car allowance | 3,000 | 36,000 |
| Meal benefit | 1,000 | 12,000 |
| Recuperation pay (6 days x 451.5) | - | 2,709 |
| **Total employer cost** | **~55,400** | **~667,050** |

This means an employer offering 42K base is actually spending approximately 55K/month, and the employee's total compensation package is worth approximately 667K NIS/year before equity and bonuses.

**Employee-side net-pay bonus**: the Section 45a pension tax credit adds about **238 NIS/month (2,852 NIS/year)** in net pay on top of the gross salary, as long as the employee pension contribution is at least 679 NIS/month (see Section 1.1). This credit is lost entirely under foreign-remote "global" contracts.

---

## 8. Negotiation Priority Order

When negotiating, prioritize benefits in this order (by financial impact and tax efficiency):

1. **Keren Hishtalmut** (if not offered): worth 7.5% of salary, tax-free after 6 years
2. **Base salary**: the foundation for all percentage-based benefits
3. **Signing bonus**: one-time, often easier to approve than salary increases
4. **Pension upgrade** (to max employer rates): long-term compound value
5. **Car allowance / upgrade**: meaningful monthly value
6. **Extra vacation days**: quality of life plus monetary value
7. **Annual bonus structure**: variable but can be significant
8. **Education budget**: career investment
9. **Hybrid/remote flexibility**: lifestyle value (hard to quantify)
10. **Equity acceleration / additional grant**: for equity-heavy packages

---

## 9. Red Flags in Benefit Packages

Watch for these warning signs:

- **No Keren Hishtalmut**: standard in tech, absence is a 7.5% pay cut
- **Pension below statutory minimum**: the 2017 expansion order fixed the floor at 6% employee + 6.5% tagmulim + 6% severance. Any offer below this is non-compliant, not a negotiation point.
- **Tech offers at the statutory floor**: should be at least 6%+6.5% tagmulim + 8.33% severance in tech, with Section 14 applied
- **No severance fund (Pitzuim)**: 6% is the statutory floor and is compliant, so it is not by itself a red flag; less than 6% is. Below 8.33% simply means the offer is under the tech-market norm and is a negotiating point rather than a defect
- **Section 14 not applied**: means severance is not guaranteed via the pension fund
- **"Global" salary with no Israeli benefits**: common in remote roles for foreign companies, but you lose significant tax-advantaged benefits
- **Unlimited vacation with low actual usage**: ask about average days taken by the team
- **Equity with no clear vesting or exercise terms**: get everything in writing

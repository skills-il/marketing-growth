---
name: israeli-email-sequences
description: Design email marketing sequences for the Israeli market with Hebrew RTL rendering, Jewish and national holiday scheduling, and anti-spam law compliance. Use when user asks about Israeli email marketing, Hebrew email campaigns, Chok HaSpam compliance, Hebrew newsletter design, or holiday-triggered email sequences. Covers Amendment 40 compliance, RTL rendering, and subject line optimization.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Israeli Email Sequences

## Instructions

### Chok HaSpam Compliance (Amendment 40)
Israeli anti-spam law (Amendment 40 to the Communications Law, in force since Dec 2008) requires explicit opt-in consent before sending commercial email, SMS, or fax. Every message must identify the sender, include a working one-click unsubscribe mechanism honored upon receipt (2 business days is the safe default), and maintain provable consent records (timestamp, source, IP). Statutory damages: up to 1,000 NIS per message without proof of harm, and class actions are common (Knesset bill in 2024 proposed raising the cap to 5,000 NIS but as of 2026-04-25 has not passed).

### Privacy Protection Law Amendment 13 (in force August 14, 2025)
On top of Chok HaSpam, Amendment 13 to the Privacy Protection Law tightens marketing-data rules. Marketing email lists are a "database" subject to the law: you must (1) inform subjects at collection time why you collect data and who receives it, (2) honor erasure and access requests within 30 days, (3) document a Data Protection Officer (DPO) for businesses with 100k+ subjects or sensitive data, (4) report serious breaches to the Privacy Protection Authority (PPA) within 24 hours. Administrative fines under Amendment 13 reach 3.2M NIS (capped at 5% of annual turnover) for severe violations. Apply both Chok HaSpam (consent + unsubscribe) AND Amendment 13 (data rights + breach reporting) when designing sequences.

### Hebrew RTL Email Rendering
Use `dir="rtl"` on the html element AND every `table`/`td`. Gmail web/Android renders RTL well; Outlook (desktop + Outlook.com) needs MSO conditional comments wrapping the table. Apple Mail respects `dir` natively. Font stack: Arial, Tahoma, sans-serif (web-safe only; Google Fonts and Resend's default Inter do not always load in Outlook). Wrap numbers, prices, and English brand names in `<span dir="ltr">` to prevent reversal. Note: `gmail.co.il` is Walla Mail (Israeli webmail), NOT Google. Its rendering engine is closer to Outlook than Gmail, so test there explicitly.

### Hebrew Subject Lines
Keep subject lines 40-50 characters (mobile cuts off after ~30 in Hebrew due to wider glyphs). Personalization (first name, city) lifts open rates 15-20%. Israeli benchmarks (Mailchimp + Brevo regional reports, 2024-2025): 22-28% open rate, 2-4% click rate, 0.2-0.5% unsubscribe rate. Best send times: Tuesday/Wednesday, 9-10 AM or 7-8 PM Israel time. Avoid Friday afternoon and Saturday entirely.

### Holiday Email Calendar
Active campaign windows: Rosh Hashana (Tishrei 1, Sep/Oct), Hanukkah (Kislev 25, Dec), Tu BiShvat (Shvat 15, Jan/Feb), Purim (Adar 14, Feb/Mar), Pesach (Nisan 15, Apr), Lag BaOmer (Iyar 18, May), Shavuot (Sivan 6, May/Jun), Yom Ha'atzmaut (Iyar 5, Apr/May). NEVER send commercial email on Yom Kippur (Tishrei 10), Yom HaZikaron (Iyar 4), Yom HaShoah (Nisan 27), or during the 7-day shiva period after a national tragedy. Tisha B'Av (Av 9, Jul/Aug) is also avoided by religious audiences. Use the Hebcal API to compute Gregorian dates per year.

### ESP Availability in Israel (2026)
Mailchimp, Brevo (formerly Sendinblue), SendGrid, Resend, Customer.io, Klaviyo, ActiveCampaign all serve Israel without restrictions (no GDPR-style data residency requirement after Amendment 13; Israel is recognized by the EU as having adequate protection). HubSpot, Iterable, Constant Contact also work. Local Israeli ESPs (Smoove at smoove.io, ActiveTrail, Rav Messer, InWise) ship native Hebrew RTL templates and Israeli holiday calendars by default. For Hebrew-first deliverability and SMS combined, ActiveTrail or Smoove typically beat US-based ESPs.

### Sequence Types
- **Welcome (5 emails over 10 days):** Day 0 brand intro, Day 2 value prop + lead magnet, Day 4 social proof with Israeli customers, Day 7 product showcase with NIS pricing, Day 10 limited offer.
- **Cart Abandonment (3 emails: 1h, 24h, 72h):** reminder, social proof + urgency, discount in NIS.
- **Post-Purchase (4 emails: 1d, 7d, 30d, 90d):** thank-you + delivery, how-to-use, review request, replenishment/cross-sell.
- **Re-engagement (3 emails: 30, 45, 60 days inactive):** "we miss you", best-of digest, win-back offer or sunset.
- **Holiday (1-3 emails per holiday):** teaser, main offer, last-chance.

## Examples

### Example 1: Build Hebrew Welcome Email Sequence
User says: "Create a 5-email welcome sequence for Israeli subscribers"
Actions:
1. Email 1: Welcome + brand story (send immediately, Hebrew RTL)
2. Email 2: Value proposition + free resource (Day 2)
3. Email 3: Social proof with Israeli customers (Day 4)
4. Email 4: Product showcase with NIS pricing (Day 7)
5. Email 5: Limited offer + urgency (Day 10)
6. Include unsubscribe link per Israeli spam law (Chok HaSpam)
Result: 5-email Hebrew welcome sequence with Chok HaSpam compliance

### Example 2: Create Hebrew Abandoned Cart Recovery
User says: "Set up abandoned cart emails for our Israeli e-commerce store"
Actions:
1. Email 1: Reminder with cart items (1 hour after abandonment)
2. Email 2: Social proof + urgency (24 hours)
3. Email 3: Discount offer in NIS (48 hours)
4. All emails: RTL layout, NIS pricing, Hebrew subject lines
5. Include proper opt-out mechanism per Chok HaSpam
Result: 3-email Hebrew cart recovery sequence with Israeli compliance

## Bundled Resources

### Scripts
- `scripts/email_compliance_checker.py` -- Validates email content against Israeli Chok HaSpam requirements. Run: `python scripts/email_compliance_checker.py --help`

### References
- `references/chok-haspam-guide.md` -- Complete guide to Israeli anti-spam law (Chok HaSpam, 2008), opt-in requirements, penalties (up to 1,000 NIS per message), and compliance checklist. Consult when building any email marketing for Israeli audiences.

## Gotchas

- Israeli anti-spam law (Chok HaSpam, Amendment 40) requires explicit opt-in consent, not just opt-out. Agents trained on US CAN-SPAM rules may suggest opt-out-only flows, which violate Israeli law.
- Privacy Protection Law Amendment 13 (Aug 2025) layers data-rights duties on top of Chok HaSpam: 30-day access/erasure response, 24-hour breach reporting to the PPA, DPO appointment for large lists. Agents trained pre-2025 may miss this entirely and only address Chok HaSpam.
- Statutory damages under Chok HaSpam are up to 1,000 NIS per message without proof of harm. Class actions multiply this fast. Amendment 13 administrative fines reach 3.2M NIS for severe violations. Agents tend to understate legal risk.
- `gmail.co.il` is Walla Mail (Israeli webmail), not Google. Its RTL engine behaves more like Outlook than Gmail. If you only test against Gmail, you will miss broken rendering for a real chunk of Israeli recipients.
- Commercial email must never be sent on Yom Kippur, Yom HaZikaron, Yom HaShoah, or during national mourning periods. Agents may not have these dates in their calendar and could schedule campaigns during sensitive periods.
- Hebrew email RTL requires `dir="rtl"` on both the HTML element and every table/td cell. Agents may only set it at the top level, causing rendering issues in Outlook (common in Israeli businesses) and Walla Mail.
- Numbers and English text within Hebrew emails need `dir="ltr"` span wrappers to display correctly. Agents often forget this, causing phone numbers and prices to render in reverse order.
- Israeli ESPs (Smoove, ActiveTrail, InWise, Rav Messer) ship Hebrew-RTL templates and Israeli holiday calendars out of the box. Agents default-recommending Mailchimp/SendGrid leave Hebrew users with worse defaults and broken Outlook rendering.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Israel Communications Law (Amendment 40) | https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawPrimary.aspx?lawitemid=2001205 | Chok HaSpam text, opt-in requirements, statutory damages |
| Privacy Protection Authority (PPA) | https://www.gov.il/en/departments/the_privacy_protection_authority | Amendment 13 guidance, breach reporting, DPO requirements |
| Privacy Protection Law (Amendment 13) | https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawBill.aspx?t=LawReshumot&lawitemid=2202316 | Marketing-database duties effective Aug 2025 |
| Hebcal API | https://www.hebcal.com/home/developer-apis | Jewish + Israeli holiday dates for campaign scheduling |
| Kol Zchut – Consumer Rights | https://www.kolzchut.org.il/en | Bilingual explanations of anti-spam rights |
| MJML Email Framework | https://mjml.io/documentation | RTL email templates, Gmail/Outlook rendering |
| Resend Hebrew/RTL guide | https://resend.com/docs/send-with-react-email | RTL React Email templates with `dir="rtl"` |
| Smoove (Israeli ESP) | https://www.smoove.io | Hebrew-native ESP with built-in Israeli holiday calendar |
| ActiveTrail (Israeli ESP) | https://www.activetrail.com | Hebrew RTL templates, SMS + email combined |

## Troubleshooting

### Error: "Hebrew email renders LTR in some clients"
Cause: Email client ignoring dir="rtl" attribute
Solution: Add `dir="rtl"` to the outermost table AND each content cell. Use inline CSS `direction: rtl; text-align: right;` as fallback. Test in Outlook (common in Israeli businesses).

### Error: "Unsubscribe link not meeting legal requirements"
Cause: Chok HaSpam requires specific unsubscribe format
Solution: Unsubscribe link must be clearly visible, work with one click, and process within 2 business days. Include physical address and sender identification in Hebrew.

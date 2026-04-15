---
name: israeli-email-sequences
description: Design email marketing sequences for the Israeli market with Hebrew RTL rendering, Jewish and national holiday scheduling, and anti-spam law compliance. Use when user asks about Israeli email marketing, Hebrew email campaigns, Chok HaSpam compliance, Hebrew newsletter design, or holiday-triggered email sequences. Covers Amendment 40 compliance, RTL rendering, and subject line optimization.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex.
---

# Israeli Email Sequences

## Instructions

### Chok HaSpam Compliance (Amendment 40)
Israeli anti-spam law requires explicit opt-in consent before sending commercial email. Every email must identify the sender, include a working unsubscribe mechanism (honored within 2 business days), and maintain consent records. Penalties up to 1,000 NIS per message (civil, without proof of damages).

### Hebrew RTL Email Rendering
Use dir="rtl" on html element and every table/td. Gmail (~45% market share) has good RTL support. Outlook needs MSO conditional comments. Font stack: Arial, Tahoma, sans-serif (not Google Fonts). Wrap numbers in span dir="ltr".

### Hebrew Subject Lines
Keep 40-50 characters. Personalization increases open rates 15-20%. Israeli email benchmarks: 20-25% open rate, 2-4% click rate. Best send times: Tuesday/Wednesday, 9-10 AM or 7-8 PM.

### Holiday Email Calendar
Key holidays for campaigns: Rosh Hashana, Hanukkah, Purim, Pesach, Yom Ha'atzmaut. NEVER send commercial email on Yom Kippur or Yom HaZikaron.

### Sequence Types
Welcome (5 emails over 10 days), Cart Abandonment (3 emails: 1h, 24h, 72h), Re-engagement (3 emails: 30, 45, 60 days).

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
- Penalties under Chok HaSpam are up to 1,000 NIS per message without requiring proof of damages. Agents may understate the legal risk of non-compliance.
- Commercial email must never be sent on Yom Kippur or Yom HaZikaron. Agents may not have these dates in their calendar and could schedule campaigns during these sensitive periods.
- Hebrew email RTL requires `dir="rtl"` on both the HTML element and every table/td cell. Agents may only set it at the top level, causing rendering issues in Outlook which is common in Israeli businesses.
- Numbers and English text within Hebrew emails need `dir="ltr"` span wrappers to display correctly. Agents often forget this, causing phone numbers and prices to render in reverse order.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Israel Communications Law (Amendment 40) | https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawPrimary.aspx?lawitemid=2001205 | Chok HaSpam text, opt-in requirements, penalties |
| Privacy Protection Authority | https://www.gov.il/en/departments/the_privacy_protection_authority | Consent, database registration, marketing data |
| Hebcal API | https://www.hebcal.com/home/developer-apis | Jewish holiday dates for campaign scheduling |
| Kol Zchut – Consumer Rights | https://www.kolzchut.org.il/en | Bilingual explanations of anti-spam rights |
| MJML Email Framework | https://mjml.io/documentation | RTL email templates, Gmail/Outlook rendering |

## Troubleshooting

### Error: "Hebrew email renders LTR in some clients"
Cause: Email client ignoring dir="rtl" attribute
Solution: Add `dir="rtl"` to the outermost table AND each content cell. Use inline CSS `direction: rtl; text-align: right;` as fallback. Test in Outlook (common in Israeli businesses).

### Error: "Unsubscribe link not meeting legal requirements"
Cause: Chok HaSpam requires specific unsubscribe format
Solution: Unsubscribe link must be clearly visible, work with one click, and process within 2 business days. Include physical address and sender identification in Hebrew.

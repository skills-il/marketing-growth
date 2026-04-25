# Chok HaSpam (Israeli Anti-Spam Law) Guide

## Amendment 40 to the Communications Law (in force Dec 2008)
The Israeli anti-spam law requires **explicit prior consent (opt-in)** before sending commercial electronic messages (email, SMS, fax, automated calls).

## Key Requirements
1. **Explicit consent**: Must be recorded and provable (timestamp, source, IP)
2. **Sender identification**: Every message must clearly identify who sent it (legal entity name, contact info)
3. **Unsubscribe mechanism**: Must be honored upon receipt; 2 business days is the safe operational default
4. **No pre-checked boxes**: Consent must be active, not passive
5. **Subject-line tag**: Commercial messages must be marked "פרסומת" (advertisement) in the subject or first words

## Statutory Damages and Enforcement
- Up to **1,000 NIS per message** civil damages without proof of harm (סעיף 30א(י) לחוק התקשורת)
- Class actions are common and routinely award millions of shekels in aggregate
- A 2024 Knesset bill proposed raising the cap to 5,000 NIS per message; as of 2026-04-25 it has not passed
- Privacy Protection Authority can also impose administrative fines under Amendment 13 (see below)

## Exceptions (Consent Not Required)
- Existing customer relationship: purchased a similar product/service in the last 12 months
- B2B messages to a publicly listed business contact, when relevant to that business's stated activity
- All exceptions still require: working unsubscribe link, sender identification, "פרסומת" tag

## Privacy Protection Law Amendment 13 (in force Aug 14, 2025)
On top of Chok HaSpam, marketing email lists are a "database" subject to additional duties:
- **30-day response** to access, correction, and erasure requests
- **24-hour breach reporting** to the PPA for serious incidents
- **DPO appointment** for businesses with 100k+ subjects or sensitive data
- **Administrative fines** up to 3.2M NIS (capped at 5% of annual turnover) for severe violations

## Best Practices
- Double opt-in recommended
- Keep consent records with timestamp, source, IP, and exact wording shown to the user
- Honor unsubscribe within 24 hours operationally (the law requires "upon receipt")
- Include physical address and legal-entity name in footer
- Add "להסרה השיבו 'הסר'" or one-click link in every message
- Never buy email lists
- Separate transactional from marketing emails (transactional are exempt from opt-in but still subject to Amendment 13)
- Document the lawful basis for each contact (consent / customer relationship / B2B)

## Email Benchmarks for Israel (2024-2025)
| Metric | Average |
|--------|---------|
| Open rate | 22-28% |
| Click rate | 2-4% |
| Unsubscribe rate | 0.2-0.5% |
| Bounce rate | < 2% (over 5% triggers Gmail/Yahoo throttling) |
| Best send day | Tuesday/Wednesday |
| Best send time | 9-10 AM or 7-8 PM Israel time |
| Avoid | Friday afternoon, Saturday, all national memorial days |

## References
- Communications Law (Telecommunications and Broadcasts) Amendment 40: https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawPrimary.aspx?lawitemid=2001205
- Privacy Protection Law Amendment 13: https://main.knesset.gov.il/Activity/Legislation/Laws/Pages/LawBill.aspx?t=LawReshumot&lawitemid=2202316
- Privacy Protection Authority guidance: https://www.gov.il/en/departments/the_privacy_protection_authority

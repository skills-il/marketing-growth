# Chok HaSpam (Israeli Anti-Spam Law) Guide

Section references are to section 30A of the Communications Law (Telecommunications and Broadcasts), as amended by Amendment 40 (in force Dec 2008) and amended again most recently in 2022.

## Consent (section 30A(b))
Express **prior** consent is required before sending a commercial message by email, SMS, fax, or automated dialer. The consent must be **in writing**, and the statute expressly extends "in writing" to an electronic message or a **recorded call**. Consent must be active, not passive: no pre-checked boxes. Keep a provable record with timestamp, source, IP, and the exact wording shown to the user.

A **one-off** approach to a recipient who is a **business**, or for a donation or advocacy, offering the recipient the chance to opt in, is expressly not a breach. This permits one invitation, not an ongoing B2B campaign.

## What the message must contain

### Email, fax, and automated dialer (section 30A(e)(1))
The advertiser must state the following prominently, clearly, and non-misleadingly:

1. That it is an advertisement. The word **"פרסומת"** (or "בקשת תרומה" / "תעמולה") must appear at the **start** of the message, and for an electronic message, **in the subject line**.
2. The advertiser's **name, address, and contact details**.
3. The recipient's right to send a refusal notice at any time, a simple and reasonable way to send it, and, for an electronic message, a **valid internet address of the advertiser** for that purpose.

An automated-dialer ad additionally has to open the voice message with a removal offer and let the recipient remove themselves by pressing a key (section 30A(e)(1)(c)(2)).

### SMS is a carve-out (section 30A(e)(2))
"Notwithstanding paragraph (1)", an advertiser sending by **short message** shall state **only** its name and its contact details for giving a refusal notice. The address requirement drops out. This carve-out is specific to short messages; it does not extend to fax, email, or automated dialer.

## Refusal notices (section 30A(d))
The recipient may send a refusal notice at any time, free of charge apart from the cost of sending it, **in writing or by the same channel the ad arrived on, at the recipient's choice**. Where the parties are in a continuing-supply contract, the recipient is treated as having refused when that contract ends.

**The statute sets no deadline for honouring a refusal.** Honour it immediately. The "48 hours" / "2 days" figure comes from Google's and Yahoo's bulk-sender rules, not from Israeli law, and applies only to marketing mail.

## Exceptions to the consent requirement

### Existing customer (section 30A(c)), all three limbs, cumulatively
1. The recipient gave their details to the advertiser during a purchase or a negotiation for one, **and** the advertiser told them the details would be used to send advertising.
2. The advertiser gave the recipient an opportunity to refuse, and the recipient did not.
3. The advertisement concerns a product or service **of a similar kind** to the one in limb 1.

There is **no** 12-month recency window in the statute. Do not assert one.

### Non-profit email (section 30A(b1))
An association (עמותה) or public-benefit company may send email for donations or advocacy without prior consent, provided the recipient has not refused.

All exceptions still require the full section 30A(e) disclosure block, including the "פרסומת" tag and a working refusal route.

## Damages and enforcement
- Section 30A(j)(1): a court **may** award up to **1,000 NIS per offending message** without proof of harm, where the sending was knowing. This is a ceiling and is discretionary, not an automatic tariff.
- Section 30A(j)(5) creates a rebuttable presumption of knowledge, with no defence available where a refusal notice had already been given, where the advertiser had previously breached, or where the address list was randomly generated.
- Class actions are common and aggregate quickly.
- A bill raising the ceiling to 5,000 NIS has been discussed but is **not enacted**; the consolidated statute still reads 1,000 NIS as of August 2026.
- Criminal liability under section 30A(f) is by reference to the Penal Law section 61 fine bands, not a figure stated in the Communications Law. Do not quote a shekel figure for it without the current section 61 update order.

## Privacy Protection Law Amendment 13 (in force Aug 14, 2025)
Marketing lists are databases, so these duties stack on top of Chok HaSpam.

| Duty | Rule |
|------|------|
| Registration | Required for a database whose main purpose is supplying personal data to others as a business or for consideration, **including direct-mail services**, holding data on more than **10,000** people (section 8A(a)) |
| Notification | A non-registrable database holding specially-sensitive data on more than **100,000** people notifies the Authority within **30 days** (section 8A(b)(1)) |
| DPO | Four triggers in section 17ב1(a); the only numeric one is the same 10,000-person direct-mail test. **No 100,000-subject trigger exists.** |
| Direct mail | Sections 17ד-17ו. Registration with "direct-mail services" as a registered purpose, and every approach must disclose that it is direct mail **with the database's registration number**, the deletion right and where to write, and the controller's identity, address, and data sources. Section 17ג was repealed. |
| Access | 30 days to grant access (1981 access regulations, reg. 4(a); Registrar may extend by 15 days); **21 days** to notify a refusal (reg. 5(a)) |
| Security incidents | A serious incident is reported to the Registrar **immediately** (reg. 11(d), 2017 Data Security Regulations). Applies to medium and high security-level databases only. There is no 24-hour clock. |
| Penalties | Section 23כו fixed amounts, e.g. 150,000 NIS, doubled where the database covers a million people or more. Where a computed penalty falls below 30,000 NIS the head of the Authority may impose 30,000 NIS. **The 5%-of-turnover figure is a reduction applied under the Fifth Schedule on the violator's application, not a cap.** |

## Best Practices
- Double opt-in is the cheapest way to make the written-consent requirement provable.
- Store the consent record with timestamp, source, IP, and the exact wording shown.
- Honour refusals immediately; treat 48 hours as the outer platform limit, not the target.
- Put the advertiser's legal-entity name, address, and contact details in the footer.
- Add a one-click unsubscribe (RFC 8058) alongside the statutory refusal route. They are different requirements and one does not satisfy the other.
- Never buy email lists. A bought list carries no section 30A(b) consent you can evidence and no purchase relationship to found the section 30A(c) exception on.
- Keep transactional and marketing streams separate. Section 30A bites on a message that is a דבר פרסומת, and Google's one-click unsubscribe rule is expressly limited to marketing and promotional mail, so a genuinely transactional message sits outside both. Amendment 13 still applies to the underlying database either way. Where a message mixes service content with an offer, treat it as advertising.
- Document the lawful basis per contact: consent, existing-customer exception, or non-profit.

## Email Benchmarks for Israel
The only current Israel-specific published figures come from ActiveTrail's 2026 Israeli benchmark report (a vendor source; treat accordingly).

| Metric | Value | Source |
|--------|-------|--------|
| Open rate, average | ~40% | ActiveTrail 2026 IL benchmark |
| Open rate, top decile | >53% | ActiveTrail 2026 IL benchmark |
| Click rate, average | ~3% | ActiveTrail 2026 IL benchmark |
| Click rate, leaders | ~5% | ActiveTrail 2026 IL benchmark |
| Unsubscribe rate | not published for Israel | none |
| Spam complaint rate | keep below 0.10%, never reach 0.30% | Google sender guidelines |
| Best send day | Tuesday/Wednesday | operational convention |
| Best send time | 9-10 AM or 7-8 PM Israel time | operational convention |
| Avoid | Friday afternoon, Saturday, national memorial days | Chok HaSpam practice + audience norms |

Mailchimp publishes no Israel or Middle East breakdown, and its benchmark page states its data was last updated in December 2023. Do not attribute Israeli figures to Mailchimp or Brevo. Open rates in every current source are inflated by Apple Mail Privacy Protection, which auto-opens messages; click rate is the more reliable comparison.

## References
- Communications Law section 30A, consolidated text: https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%AA%D7%A7%D7%A9%D7%95%D7%A8%D7%AA_(%D7%91%D7%96%D7%A7_%D7%95%D7%A9%D7%99%D7%93%D7%95%D7%A8%D7%99%D7%9D)
- Privacy Protection Law as amended, consolidated text: https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%92%D7%A0%D7%AA_%D7%94%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA
- Privacy Protection Authority: https://www.gov.il/he/departments/the_privacy_protection_authority
- Google Email sender guidelines: https://support.google.com/a/answer/81126?hl=en
- Yahoo sender best practices: https://senders.yahooinc.com/best-practices/

---
name: israeli-email-sequences
description: Not legal advice. Design email marketing sequences for the Israeli market with Hebrew RTL rendering, Jewish and national holiday scheduling, and anti-spam law compliance. Use when user asks about Israeli email marketing, Hebrew email campaigns, Chok HaSpam compliance, Hebrew newsletter design, or holiday-triggered email sequences. Covers Amendment 40 compliance, RTL rendering, and subject line optimization.
license: MIT
compatibility: Works with Claude Code, Cursor, GitHub Copilot, Windsurf, OpenCode, Codex, Antigravity, Gemini CLI.
---

# Israeli Email Sequences

## Legal notice

Not legal advice. This skill explains what the Communications Law and the Privacy Protection Law require of a sender; it does not decide whether your particular campaign, list, or consent record complies. It is not a substitute for advice from a licensed Israeli lawyer that takes account of your own facts, and the bundled validator checks the structure of an email, not its legality. Its output is generated automatically by an AI model, which may err, omit data, or state a wrong conclusion, and any use of it is at your sole responsibility. No lawyer has reviewed or approved it, and it must not be presented or relied on as a legal opinion or as evidence. Before launching a campaign to a list you did not build under documented consent, before relying on the section 30A(c) exception, and before responding to a demand letter or a class-action claim, consult a lawyer.

## Instructions

### Chok HaSpam Compliance (Amendment 40, section 30A of the Communications Law)
Israeli anti-spam law (Amendment 40, in force since Dec 2008) requires express prior consent before sending a commercial message by email, SMS, fax, or automated dialer. Section 30A(b) requires that consent be **in writing**, which the statute expressly defines to include an electronic message or a recorded call. A one-off approach asking a *business* recipient to opt in is not itself a breach.

**What every commercial email must contain (section 30A(e)(1)):**
1. The word **"פרסומת"** (or "בקשת תרומה" / "תעמולה") at the **start of the ad**, and for an electronic message, in the **subject line** as well. Put it in both places; the statute requires the opening of the message and the subject. This is the requirement most non-Israeli tooling omits, and it is not optional.
2. The advertiser's name, **address**, and contact details.
3. The recipient's right to send a refusal notice at any time, a simple and reasonable way to send it, and a valid internet address of the advertiser for that purpose.

**SMS is a deliberate carve-out (section 30A(e)(2)).** For a short-message ad the statute says the advertiser shall state *only* its name and the contact details for giving a refusal notice. The address drops out. Do not copy the full email disclosure block into an SMS, and do not assume the SMS list is the same list.

**The existing-customer exception (section 30A(c))** needs all three limbs together: the recipient gave their details during a purchase or negotiation for one AND was told the details would be used for advertising; they were given a chance to refuse and did not; and the ad concerns a **similar** product or service. There is no 12-month window in the statute. A registered charity or public-benefit company may email for donations or advocacy under section 30A(b1) unless the recipient has refused.

**Damages:** section 30A(j)(1) lets a court award up to 1,000 NIS per offending message with no proof of harm, where the sending was knowing. It is a ceiling, not a tariff. Class actions are common. A bill raising the ceiling to 5,000 NIS has been discussed but is **not** enacted; the consolidated statute still reads 1,000 NIS, so never quote a higher figure to a client.

**Who has to prove what.** This is the fact that decides a real claim, and it is the reason record-keeping is the defence rather than hygiene. The claimant produces the message; the advertiser has to produce the consent. Section 30A(j)(5) adds a rebuttable presumption of knowledge, and it gives no way out where a refusal notice had already been given, where the advertiser had breached before, or where the address list was randomly generated. A defensible record is per-contact and holds the address, the timestamp, the IP, the form or system it came from, and the exact opt-in wording that was on screen. Keep it for the life of the limitation period rather than for as long as the contact stays on the list, since a claim (and especially a class action) can land years after the send. Confirm the applicable period with a lawyer and set the retention rule from that, not from your list-cleanup schedule. Export the records when you change ESP, which is where they are usually lost.

**Refusal notices:** the statute sets **no** deadline for honouring one, so honour it immediately. The "2 days" figure that circulates is not Israeli law, it is Google's and Yahoo's platform requirement (see the deliverability section). Note also that the recipient chooses the channel: a refusal may arrive as a reply, so an unmonitored `no-reply@` From address is itself a compliance gap. Suppress a refusal across every channel and every list in the account, not just the one that carried the message.

**Which channels this covers.** The statute defines an electronic message as a coded telecom message carried **over the internet**, and a short message as one carried over a telecom network to terminal equipment. WhatsApp, Telegram and in-app push therefore sit more naturally in the electronic-message limb than in the short-message carve-out, which means the full section 30A(e)(1) disclosure applies rather than the reduced SMS list. That is a reading of the statutory text, not a settled ruling, so treat the full list as the conservative default for any internet-carried channel and take advice before relying on the carve-out outside true SMS. Meta's own opt-in and template-approval rules apply on top and are not a substitute for consent under this section.

### Privacy Protection Law Amendment 13 (in force August 14, 2025)
A marketing list is a database under the law, so Amendment 13 duties stack on top of Chok HaSpam.

- **Registration (section 8א(a)):** a database whose main purpose is collecting personal data to pass to others as a business or for consideration, **including direct-mail services**, must register once it holds data on more than 10,000 people. This is the threshold a list broker or an agency running client lists is most likely to cross.
- **Notification (section 8א(b)(1)):** a database holding specially-sensitive information on more than 100,000 people that is *not* registrable must notify the Authority within 30 days.
- **DPO (section 17ב1(a)):** four triggers, only one of which is numeric, the same "supplying data to others, including direct-mail services, on more than 10,000 people" test. The others are being a public body, or having regular large-scale monitoring or large-scale sensitive-data processing as a core activity. There is no 100,000-subject DPO trigger.
- **Direct mail (sections 17ד to 17ו):** processing personal data in a direct-mail database requires registration with "direct-mail services" as a registered purpose. Every direct-mail approach must clearly state that it is direct mail **together with the database's registration number**, the right to be deleted and where to write, and the controller's identity, address, and the sources the data came from. Section 17ג was repealed by Amendment 13, so cite 17ד to 17ו.
- **Access and correction:** 30 days to grant access under the 1981 access regulations (extendable by 15 days by the Registrar), and 21 days to notify a refusal.
- **Security incidents:** a serious incident must be reported to the Registrar **immediately** (regulation 11(d) of the 2017 Data Security Regulations), not within a fixed 24-hour clock, and the duty attaches only to medium and high security-level databases.
- **Penalties:** there is no flat 5%-of-turnover cap. Section 23כו sets fixed amounts, for example 150,000 NIS, doubled where the database covers a million people or more, and where a computed penalty falls below 30,000 NIS the head of the Authority may impose 30,000 NIS instead. The 5% figure is a **reduction the violator must apply for**, not a ceiling that applies automatically.
- **EU adequacy:** Decision 2011/61/EU still stands, so there is no data-residency barrier to using a US or EU ESP. The most recent concluded Commission review is the January 2024 report on the eleven pre-GDPR adequacy decisions, which **predates** Amendment 13. No post-Amendment-13 adequacy review has concluded, so do not tell a client the transfer position has been re-confirmed for the current law.

### Consent Capture and Double Opt-In
Double opt-in is the cheapest way to turn "we had consent" into something you can put in front of a court, and every ESP named below ships single opt-in as the default, so it is a setting you have to turn on.

- The **confirmation email is not an advertisement**. It carries no offer, so it is not a דבר פרסומת and must NOT be tagged "פרסומת". Tagging it both confuses the recipient at the exact moment you need them to click and mislabels a transactional message.
- An **unconfirmed address is not a subscriber**. It must not enter the welcome flow, the newsletter, or any promotional step. Gate flow entry on the confirmed state, and re-check it at every step rather than only at entry, since a contact can refuse mid-sequence.
- Give the confirmation link an expiry and a re-send path, and keep the pending state visible so nobody "fixes" a stalled list by bulk-confirming it.
- For a list you inherited, bought, or built on single opt-in, run a **re-permission campaign** before any promotional send. Everyone who does not re-confirm is suppressed, not mailed. This is the most common real Israeli situation and the most expensive one to get wrong.
- The compliance duties land in three different layers, which is why they get missed: the "פרסומת" tag is typed into the **subject field** of each campaign or flow step and has to survive A/B subject variants and personalisation; the advertiser name, address, contact details and the section 17ו registration number live in a **footer content block**, and no ESP has a field for the registration number so it is added by hand; and `List-Unsubscribe` is an **ESP account or domain setting**, emitted as a header, not something you can add to the HTML. Check each one in the layer it actually lives in.

### Scheduling Triggered Flows Around Shabbat and Blackout Dates
Blackout dates are easy for a broadcast and easy to get wrong in an automation, which is the failure this section exists to prevent. A 1h/24h/72h cart sequence and a Day 0/2/4/7/10 welcome sequence will, across a normal week of enrolments, fire on Shabbat and can fire on Yom Kippur or Yom HaZikaron. The audience norm the skill states for broadcasts has to be enforced as a rule inside the flow.

- Set the account timezone to Asia/Jerusalem and remember Israeli DST moves the Friday cutoff through the year.
- Holidays and Shabbat **begin at sunset the evening before**, so a Friday afternoon send is already inside the blackout. Compute the entry, not the calendar date.
- Resolve the dates per year rather than hardcoding them, via the Hebcal API or the Hebcal MCP, and feed them into a suppression window rather than into a content calendar.
- Decide per step whether a blocked send **holds and releases** after the window or is **skipped**. For cart abandonment a held 1-hour email arriving 30 hours later is worse than no email; for a welcome step, holding is usually right.
- Use the ESP's quiet-hours or send-window feature to enforce it, and verify it applies to flow steps and not only to scheduled campaigns, which is a common gap.

### List Hygiene and Deliverability Operations
Authentication gets you accepted; these keep you accepted. This is the half of deliverability that a sequence design usually omits.

- **Warm up** a new sending domain or a post-migration one with a ramped volume against your most engaged segment. Launching a welcome sequence is exactly when a cold domain gets its reputation set.
- Remove **hard bounces** immediately. Retry soft bounces a limited number of times, then suppress.
- Keep a **global suppression list** at account level, and make it survive ESP migration and every CSV re-import. Re-importing an old list resurrects unsubscribed addresses, which is both a reputation event and a per-message exposure at up to 1,000 NIS each. This is the single most common way an Israeli sender turns a clean record into a claim.
- Segment by engagement and run a real **sunset policy**: stop mailing contacts who have not engaged in a defined window, attempt one win-back, then suppress. Sending to a dead tail is how the spam rate crosses 0.10%.
- Watch role addresses (`info@`, `office@`) on Israeli B2B lists, which attract complaints and traps.
- Monitor complaint rate continuously in Google Postmaster Tools and Microsoft SNDS rather than checking it after an incident.

### Hebrew RTL Email Rendering
Set `dir="rtl"` on the `html` element and on each `table`/`td`. Repeating it per cell is defensive rather than universally required: the documented client that strips `dir` from `table` and `td` is Orange webmail. Add inline `direction: rtl; text-align: right;` as the real fallback, since CSS survives where the attribute is stripped.

Known rendering bugs worth designing around: Outlook on Windows reverses word order for LTR runs inside an `[dir=rtl]` block (and the reverse), and Gmail on mobile applies RTL to the *entire* message when it detects an RTL language. Wrap numbers, prices, URLs, and English brand names in `<span dir="ltr">` so they do not reverse.

In MJML the `dir` attribute goes on the **root `<mjml>` tag**, which propagates it to `html` and the body wrapper; it is not an `mj-body` attribute. Use `<mj-section direction="rtl">` to invert desktop column order.

Font stack: Arial, Tahoma, sans-serif. These are email-safe faces that carry Hebrew glyphs; webfonts including Google Fonts do not load reliably in Outlook, so treat any Hebrew webfont as progressive enhancement over a safe fallback.

### Hebrew Subject Lines
Remember that the word "פרסומת" occupies the start of the line by law, so budget your hook around it. Keep the whole line short, since Hebrew glyphs are wider than Latin ones and mobile clients truncate sooner than the character counts quoted for English copy. Test the truncation point on your own audience's devices rather than trusting a number. Personalization (first name, city) is a standard lift.

**Israeli benchmarks.** The only current Israel-specific figures come from ActiveTrail's 2026 Israeli benchmark report: average open rate about 40%, crossing 53% for the top decile of organizations, and average click rate around 3%, rising to 5% for the leaders. No unsubscribe figure is published there, so do not quote one. Treat open rates with suspicion: Apple Mail Privacy Protection auto-opens messages and inflates exactly this metric. Click rate is the more honest signal.

Send timing below is operational convention among Israeli senders rather than measured data: Tuesday/Wednesday, 9-10 AM or 7-8 PM Israel time. Avoid Friday afternoon and Saturday entirely, which is an audience norm rather than a legal rule.

### Holiday Email Calendar
Active campaign windows: Rosh Hashana (Tishrei 1, Sep/Oct), Hanukkah (Kislev 25, Dec), Tu BiShvat (Shvat 15, Jan/Feb), Purim (Adar 14, Feb/Mar), Pesach (Nisan 15, Apr), Lag BaOmer (Iyar 18, May), Shavuot (Sivan 6, May/Jun), Yom Ha'atzmaut (Iyar 5, Apr/May). NEVER send commercial email on Yom Kippur (Tishrei 10), Yom HaZikaron (Iyar 4), Yom HaShoah (Nisan 27), or during a national mourning period. Tisha B'Av (Av 9, Jul/Aug) is also avoided by religious audiences. Compute the Gregorian date per year rather than hardcoding it.

### ESP Availability in Israel (2026)
Mailchimp, Brevo (formerly Sendinblue), SendGrid (a Twilio product), Resend, Customer.io, Klaviyo, ActiveCampaign, HubSpot and Iterable all serve Israel; adequacy means there is no data-residency blocker. Treat every tier, price, and quota as unverified. Vendor plans change often and several of these vendors gate their pricing behind JavaScript, so read the vendor's own current pricing page before promising a client anything.

Israeli vendors: **ActiveTrail** (activetrail.com), **smoove** (smoove.io), **Rav Messer**, and **inwise** (inwise.com). All four were live at the time of writing and all market email together with SMS. Rav Messer's current site is **responder.co.il**. Their advantage is a Hebrew-language product and Israeli support rather than any documented RTL-template or holiday-calendar feature, so evaluate templates yourself instead of assuming one ships Hebrew-correct defaults.

Do not repeat the claim that ActiveTrail was acquired by Bird or MessageBird. No published source supports it. Check any vendor's current ownership in your own contract rather than in a skill file.

### Deliverability and Authentication (mandatory at scale)
Three inbox providers now gate bulk mail on authentication.

- **Google** (since 1 Feb 2024): more than 5,000 messages per day to personal Gmail accounts in a 24-hour window makes you a bulk sender. The count is per **primary** domain, so subdomains aggregate, and the status is **permanent** once assigned. Since November 2025 Google has been ramping enforcement to temporary and permanent rejections rather than just spam foldering.
- **Yahoo**: same core requirements, with no volume threshold found on its own best-practices page, and it states the unsubscribe rule explicitly as "honor unsubscribes within 2 days".
- **Microsoft** (since 5 May 2025): domains sending over 5,000 messages per day to consumer Outlook, Hotmail, or Live must pass SPF, DKIM, and DMARC. Microsoft's announcement is internally inconsistent about the current action, describing both junk-folder routing and a `550 5.7.515` rejection, with full rejection dated "to be announced". Design for rejection.

Requirements:
- **SPF and DKIM**: both must be set up. Only **one** of them has to be aligned with the From domain for DMARC alignment to pass.
- **DMARC**: a published policy, `p=none` is sufficient to pass, with `rua` aggregate reporting. `p=quarantine` or `p=reject` once you trust your alignment.
- **One-click unsubscribe**: RFC 8058, both `List-Unsubscribe-Post: List-Unsubscribe=One-Click` and a `List-Unsubscribe` header pointing at an HTTPS endpoint. Google directs senders to follow the RFC 8058 specification itself, so the header must act on POST rather than hand the reader a preferences page. Required for marketing and promotional mail only; transactional mail is excluded. Honour requests within 48 hours.
- **Spam rate**: Google states two distinct figures. Keep the Postmaster Tools rate below **0.10%**, and never reach **0.30%**. Above 0.3% you become ineligible for mitigation until you have stayed under it for 7 consecutive days.

DKIM2 is an IETF Internet-Draft (`draft-ietf-dkim-dkim2-spec`, July 2026) with no RFC and no provider deployment; keep using standard DKIM and ignore advice to migrate.

### Sequence Types
- **Welcome (5 emails over 10 days):** Day 0 brand intro, Day 2 value prop + lead magnet, Day 4 social proof with Israeli customers, Day 7 product showcase with NIS pricing, Day 10 limited offer.
- **Cart Abandonment (3 emails: 1h, 24h, 72h):** reminder, social proof + urgency, discount in NIS.
- **Post-Purchase (4 emails: 1d, 7d, 30d, 90d):** thank-you + delivery, how-to-use, review request, replenishment/cross-sell. This archetype straddles the advertising boundary: the first two steps are transactional, while the review request and the cross-sell carry an ask and an offer, so they need consent, the tag, and one-click unsubscribe. Send the transactional steps from the transactional domain so they do not inherit marketing reputation.
- **Re-engagement (3 emails: 30, 45, 60 days inactive):** "we miss you", best-of digest, win-back offer or sunset.
- **Holiday (1-3 emails per holiday):** teaser, main offer, last-chance.

## Examples

### Example 1: Build Hebrew Welcome Email Sequence
User says: "Create a 5-email welcome sequence for Israeli subscribers"
Actions:
1. Confirm the lawful basis first: express written consent, or the section 30A(c) existing-customer limbs. If neither holds, the sequence cannot be sent at all and no amount of design fixes that.
2. Email 1: Welcome + brand story (send immediately, Hebrew RTL)
3. Email 2: Value proposition + free resource (Day 2)
4. Email 3: Social proof with Israeli customers (Day 4)
5. Email 4: Product showcase with NIS pricing (Day 7)
6. Email 5: Limited offer + urgency (Day 10)
7. Every email: subject line opens with "פרסומת", footer carries advertiser name, address, contact details, and a one-click unsubscribe
Result: a 5-email Hebrew welcome sequence built against the section 30A(e)(1) disclosure checklist. The lawful basis and the consent record are still yours to establish.

### Example 2: Create Hebrew Abandoned Cart Recovery
User says: "Set up abandoned cart emails for our Israeli e-commerce store"
Actions:
1. Email 1: Reminder with cart items (1 hour after abandonment)
2. Email 2: Social proof + urgency (24 hours)
3. Email 3: Discount offer in NIS (72 hours)
4. All emails: RTL layout, NIS pricing wrapped in `<span dir="ltr">`, Hebrew subject lines opening with "פרסומת"
5. Set the exit condition before the content: a completed purchase must remove the contact from the remaining steps, or you will send a discount to someone who has already paid
6. If you also send an SMS reminder, use the section 30A(e)(2) short form: advertiser name and refusal-contact details only. Do not assume that short form covers a WhatsApp reminder
Result: a 3-email Hebrew cart recovery sequence built against the section 30A(e)(1) disclosure checklist. The lawful basis and the consent record are still yours to establish.

## Bundled Resources

### Scripts
- `scripts/email_validator.py` -- Validates email HTML for RTL attributes and Chok HaSpam basics. Run: `python scripts/email_validator.py --input email.html`. It checks structure, not legality; it cannot tell you whether your consent record is valid.

### References
- `references/chok-haspam-guide.md` -- Section-by-section guide to Chok HaSpam: consent form, the section 30A(e) disclosure lists, the exceptions, damages, and the Amendment 13 duties that stack on top. Consult when building any email marketing for Israeli audiences.

## Recommended MCP Servers

| MCP | What It Adds |
|-----|-------------|
| [Hebcal MCP](https://agentskills.co.il/he/mcp/hebcal) | Resolves Jewish and Israeli holiday dates to Gregorian dates per year, so send-window and blackout-date logic is computed rather than hardcoded |

## Gotchas

- Chok HaSpam requires express prior opt-in, not opt-out. Agents trained on US CAN-SPAM rules suggest opt-out-only flows, which are unlawful in Israel.
- The mandatory word "פרסומת" at the start of the subject line is the single most-omitted requirement. Non-Israeli ESP templates have no field for it, and a compliant footer does not cure its absence.
- Section 30A(e)(2) *reduces* the disclosure list for SMS to name plus refusal-contact details. Agents reason by analogy from email and add the postal address, which is not what the carve-out says. Getting this backwards in either direction is a live risk.
- The existing-customer exception has three cumulative limbs and no 12-month window. Agents commonly invent a recency window borrowed from other jurisdictions.
- Amendment 13 duties are date-sensitive: report a serious security incident **immediately** (not on a 24-hour clock), grant access within 30 days, and notify a refusal to grant it within 21. Agents trained pre-2025 may miss Amendment 13 entirely.
- Amendment 13 has no flat 5%-of-turnover fine cap. The 5% is a reduction the violator applies for; the operative amounts are the fixed sums in section 23כו. Agents both understate and mis-shape this risk.
- Direct-mail messages must carry the database's **registration number** under section 17ו. Nothing in a standard ESP template emits it, so it has to be added to the footer by hand.
- Israeli businesses run heavily on Outlook, where LTR runs inside an RTL block render with reversed word order. Numbers and English text need `dir="ltr"` span wrappers or phone numbers and prices come out backwards.
- In MJML the `dir` attribute belongs on the root `<mjml>` tag, not `mj-body`. Setting it in the wrong place silently produces an LTR document.
- Bulk-sender status at Google is **permanent** once you cross 5,000/day to Gmail, and it aggregates across subdomains of one primary domain. A one-off launch blast permanently changes the rules your ordinary sending is judged by.
- Splitting transactional mail onto one domain (support@) and marketing onto another (marketing@) while publishing DKIM for only one is a recurring cause of silent deliverability loss. Both must authenticate independently or the marketing domain loses deliverability silently while the transactional one stays fine.
- Do not assume an Israeli ESP ships Hebrew-correct RTL templates or an Israeli holiday calendar by default. None of the four vendors documents those features; check the actual template output before recommending one on that basis.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Communications Law, section 30A (consolidated text) | https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%AA%D7%A7%D7%A9%D7%95%D7%A8%D7%AA_(%D7%91%D7%96%D7%A7_%D7%95%D7%A9%D7%99%D7%93%D7%95%D7%A8%D7%99%D7%9D) | Disclosure lists in 30A(e), the SMS carve-out, exceptions, damages |
| Privacy Protection Authority (PPA) | https://www.gov.il/en/departments/the_privacy_protection_authority | Amendment 13 guidance, breach reporting, DPO requirements |
| Privacy Protection Law as amended (consolidated text) | https://he.wikisource.org/wiki/%D7%97%D7%95%D7%A7_%D7%94%D7%92%D7%A0%D7%AA_%D7%94%D7%A4%D7%A8%D7%98%D7%99%D7%95%D7%AA | Registration in s.8א, DPO in s.17ב1, direct mail in s.17ד-17ו, penalties in s.23כו |
| Google Email sender guidelines | https://support.google.com/a/answer/81126?hl=en | Bulk thresholds, DMARC, one-click unsubscribe, spam rates |
| Yahoo sender best practices | https://senders.yahooinc.com/best-practices/ | Yahoo's authentication and 2-day unsubscribe rule |
| Hebcal API | https://www.hebcal.com/home/developer-apis | Jewish + Israeli holiday dates for campaign scheduling |
| Kol Zchut, Chok HaSpam (Hebrew) | https://www.kolzchut.org.il/he/%D7%A4%D7%99%D7%A6%D7%95%D7%99_%D7%91%D7%92%D7%99%D7%9F_%D7%9E%D7%A9%D7%9C%D7%95%D7%97_%D7%93%D7%91%D7%A8%D7%99_%D7%A4%D7%A8%D7%A1%D7%95%D7%9E%D7%AA_%D7%9C%D7%9C%D7%90_%D7%94%D7%A1%D7%9B%D7%9E%D7%94_%D7%A9%D7%9C_%D7%94%D7%A0%D7%9E%D7%A2%D7%9F_(%D7%97%D7%95%D7%A7_%D7%94%D7%A1%D7%A4%D7%90%D7%9D) | Plain-language summary of the anti-spam rights. Kol Zchut removed its English pages in 2023, so Hebrew only. |
| MJML Email Framework | https://mjml.io/documentation | The root-tag `dir` attribute and `mj-section direction` |
| Can I Email, `dir` support | https://www.caniemail.com/features/html-dir/ | Per-client `dir` support and the documented RTL bugs |
| smoove (Israeli ESP) | https://www.smoove.io | Hebrew-language ESP, email + SMS + WhatsApp |
| ActiveTrail (Israeli ESP) | https://www.activetrail.com | Hebrew ESP, email + SMS + WhatsApp, publishes Israeli benchmarks |

## Troubleshooting

### Error: "Hebrew email renders LTR in some clients"
Cause: the client stripped or ignored the `dir="rtl"` attribute. Verified stripping is documented for Orange webmail on `table` and `td`; for other clients this is the likeliest cause but not confirmed per-client.
Solution: set `dir="rtl"` on the outermost table and each content cell, and add inline CSS `direction: rtl; text-align: right;` which survives attribute stripping. Test in Outlook on Windows, where the separate documented bug is reversed word order for LTR runs inside RTL blocks.

### Error: "Unsubscribe link not meeting legal requirements"
Cause: two different rules are being conflated. Chok HaSpam requires a simple and reasonable refusal route plus a valid internet address for it, and sets no deadline. Google and Yahoo separately require RFC 8058 one-click headers and processing within 48 hours.
Solution: satisfy both. Emit `List-Unsubscribe-Post: List-Unsubscribe=One-Click` and a `List-Unsubscribe` HTTPS endpoint that acts on POST rather than serving a landing page, process within 48 hours, and put the advertiser's name, address, and contact details in the footer with the subject line opening on "פרסומת".

### Error: "Campaign suddenly landing in spam after a volume spike"
Cause: crossing 5,000 messages/day to Gmail makes bulk-sender rules apply permanently, and they aggregate across subdomains of one primary domain. Microsoft applies its own 5,000/day rule to consumer Outlook.
Solution: check DMARC alignment first (both SPF and DKIM configured, at least one aligned to the From domain), then the Postmaster Tools spam rate against the 0.10% guideline and the 0.30% hard line. Above 0.3% you stay ineligible for mitigation until 7 consecutive days below it.

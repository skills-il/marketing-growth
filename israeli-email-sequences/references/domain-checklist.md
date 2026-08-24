# Domain checklist: Israeli email marketing sequences

Anchor for the Phase 5.8 expert review. Scope: designing and sending commercial email (and adjacent SMS) sequences to an Israeli audience, in Hebrew, lawfully and deliverably.

## Must cover (core)

| Item | Why it is core |
|---|---|
| Express prior consent, in writing including electronic message or recorded call | Communications Law s.30A(b). The threshold question for every sequence. |
| The "פרסומת" / "בקשת תרומה" / "תעמולה" tag at the start of the subject line | s.30A(e)(1)(a). The single most-omitted statutory element; no non-Israeli ESP emits it. |
| Advertiser name, address, contact details | s.30A(e)(1)(b). |
| Refusal route plus a valid internet address for it | s.30A(e)(1)(c)(1). |
| SMS carve-out reducing the list to name plus refusal contact | s.30A(e)(2). Reasoning by analogy from email produces the wrong disclosure. |
| Existing-customer exception, three cumulative limbs, no recency window | s.30A(c). The most-used lawful basis in Israeli e-commerce. |
| Non-profit donation/advocacy email route | s.30A(b1). |
| Statutory damages ceiling of 1,000 NIS per message, discretionary, knowledge required | s.30A(j)(1) and (j)(5). |
| Refusal notice: channel of the recipient's choice, free, and no statutory deadline | s.30A(d). Distinguishing this from the platform 48-hour rule is core. |
| Amendment 13 registration at 10,000 for direct-mail-purpose databases | Privacy Protection Law s.8א(a). |
| Amendment 13 notification at 100,000 for sensitive non-registrable databases, 30 days | s.8א(b)(1). |
| DPO triggers, four, one numeric | s.17ב1(a). |
| Direct-mail disclosure including the database registration number | s.17ו. Nothing in an ESP template emits it. |
| Access 30 days, refusal notice 21 days | 1981 access regulations, regs. 4(a) and 5(a). |
| Serious security incident reported immediately | 2017 Data Security Regulations, reg. 11(d). Medium and high security-level databases only. |
| Administrative penalties as fixed amounts, with the 5% turnover figure operating as a reduction under the Fifth Schedule | s.23כו. |
| Gmail/Yahoo/Microsoft bulk-sender authentication requirements | Deliverability failure makes every other item moot. |
| SPF + DKIM both configured, one aligned; DMARC at least p=none | Google sender guidelines. |
| RFC 8058 one-click unsubscribe, marketing mail only, 48 hours | Google and Yahoo. |
| Spam rate below 0.10%, never reaching 0.30% | Google publishes two distinct figures. |
| Hebrew RTL: `dir` placement, documented client bugs, LTR spans for numbers | The rendering failure mode specific to this audience. |
| Blackout dates: Yom Kippur, Yom HaZikaron, Yom HaShoah, national mourning | Audience norm with reputational and commercial consequence. |
| Enforcing blackout dates inside TRIGGERED flows, not only broadcasts | Added 2026-08-24. A 1h/24h/72h or Day 0-10 flow fires on Shabbat and can fire on a memorial day across a normal week of enrolments. The description promises holiday-aware scheduling, so a broadcast-only answer does not discharge it. |
| Burden of proving consent sits on the advertiser; what a defensible record contains | Added 2026-08-24. s.30A(י)(5) presumption. This is the fact that decides a claim, so it is core, not hygiene. |
| Double opt-in mechanics, including that the confirmation email is not a דבר פרסומת | Added 2026-08-24. A blanket "tag every email פרסומת" rule mislabels the confirmation and depresses the confirm rate. |
| Re-permission for an inherited or single-opt-in list | Added 2026-08-24. The most common real Israeli starting position. |
| Which layer each duty is satisfied in (subject field, footer block, ESP header setting) | Added 2026-08-24. Duties stated without their layer are unactionable, and the header/HTML confusion produces false validator findings. |
| Suppression list surviving ESP migration and CSV re-import | Added 2026-08-24. Re-importing an old list resurrects refusals at up to 1,000 NIS per message. |
| Bounce handling, warmup, engagement segmentation, sunset policy | Added 2026-08-24. Authentication alone does not keep a sender in the inbox, and a sequence skill owns the launch moment when reputation is set. |
| Whether an internet-carried channel (WhatsApp, Telegram, push) takes the full 30A(e)(1) list or the SMS carve-out | Added 2026-08-24. Moved in from the out-of-scope row below. |

## Should cover (advanced)

| Item | Why |
|---|---|
| MJML `dir` on the root tag and `mj-section direction` | The most common Hebrew-email build tool. |
| Israeli ESP landscape and what is actually verifiable about it | Vendor selection is a real user question; the RTL-template claim is not documented. |
| Israel's EU adequacy status and the absence of a post-Amendment-13 review | Determines whether a US or EU ESP is usable. |
| Israel-specific benchmarks with the Apple MPP caveat | Users ask "is my open rate good"; the honest answer needs the caveat. |
| Sequence archetypes and cadences (welcome, cart, post-purchase, re-engagement, holiday) | The practical deliverable. |
| Separate DKIM for transactional and marketing sending domains | Common Israeli failure mode. |

## Out of scope (explicit)

| Item | Rationale (reviewed 2026-08-24) |
|---|---|
| Drafting the actual marketing copy | The skill designs sequences and compliance structure; copywriting is a general capability, not an Israel-specific one. |
| Full SMS/WhatsApp/push campaign *strategy* | Re-litigated 2026-08-24 and narrowed. The DISCLOSURE question for every adjacent channel is now Must-cover, because an Israeli sequence routinely has an SMS or WhatsApp limb and the 30A(e)(1)-versus-30A(e)(2) split is exactly what a user asks. What remains out of scope is channel-native campaign strategy: template approval workflows, per-message pricing, conversation windows, and creative for those channels. |
| ESP API integration code | Vendor APIs drift faster than this skill's cycle. The skill names vendors and tells the user to read current docs rather than encoding endpoints, per the anti-fabrication rule. |
| Litigation strategy and defending a class action | Emitting a legal position on a live dispute is outside a marketing skill and edges on reserved advocate work. |
| Per-year Hebrew holiday date tables | Deliberately delegated to Hebcal (API and MCP) so the dates are computed, not frozen. |

## Authoritative sources
- Communications Law (Telecommunications and Broadcasts) s.30A, consolidated text on he.wikisource
- Privacy Protection Law as amended by Amendment 13; Privacy Protection (Data Security) Regulations 2017; Privacy Protection (Conditions for Inspecting Information) Regulations 1981
- Privacy Protection Authority, gov.il
- Google Email sender guidelines; Yahoo sender best practices; Microsoft high-volume sender announcement
- Can I Email (`dir` support), MJML documentation
- ActiveTrail Israeli benchmark report (vendor source, labelled as such)

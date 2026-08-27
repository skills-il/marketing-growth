# Domain checklist: Israeli Social Content

Scope: organic (unpaid) social content and scheduling for audiences inside Israel, across Meta
surfaces, TikTok and LinkedIn. No statistic belongs in this file; figures live in the skill body
with a citation in `evidence.json`.

## Must cover

| Item | Why it is core |
|------|----------------|
| Platform music licensing is an account-type question: the general in-app sound catalogue is licensed for personal use, business accounts need commercially-licensed or original audio | The skill's primary creative instruction is to build on trending sounds, and the failure mode (muted audio or removed video) lands on the launch itself. Applies on both TikTok and Meta surfaces. |
| Facebook group conduct: read the pinned rules, get admin permission for commercial posts, never cross-post identical copy | Groups are the skill's stated primary channel, and cross-group duplication is the standard trigger under Meta's spam and inauthentic-behaviour standards. Losing the page or a manager's personal profile is the realistic consequence. |
| Commercial-interest disclosure on organic brand content, including staff posting inside community groups | Israeli consumer-protection law prohibits misleading a consumer, which reaches a brand representative posting a "personal story" or an "advice request" as an ordinary member. That is exactly the format this skill recommends. |
| AI-content disclosure, with the platforms' scopes treated as different from one another and the label name read off the live policy page | This is a content-generation skill, so the duty attaches to its primary output. TikTok's auto-applied label cannot be removed once it fires, which changes the order of operations. |
| Anti-spam consent (Section 30A of the Communications Law) whenever a social plan turns into outbound DM, WhatsApp or Telegram broadcast | The duty attaches to the message, not to whether money was spent, and Israeli practice treats messaging-app broadcast as covered. The skill points managers at those surfaces. |
| Commercial blackout days: Yom Kippur, Yom HaZikaron, Yom HaShoah, and 7 October, plus the Yom HaZikaron to Yom Ha'atzmaut transition at nightfall | Statutory memorial days with a national siren, and universal Israeli brand practice. A scheduler firing commercial content into a siren is the highest-consequence failure this skill can produce. |
| A security-event pause protocol with a named owner and a resumption criterion | Standard Israeli agency practice since October 2023. The skill ships an automated scheduler into an interrupt-driven calendar, so scheduling advice without a kill switch is incomplete. |
| Hebrew-calendar dates resolved per year, with Sukkot and Pesach treated as week-long chol hamoed windows and Tishrei as a multi-week cluster | The Hebrew calendar shifts against the Gregorian one every year; hardcoding a date is the recurring failure. |
| Shabbat and the Sunday-to-Thursday work week stated as audience-dependent, not as universal Israeli facts | The weekly rest day differs by religious community, so stating these universally is wrong for the Arab-Israeli audience. |
| Arab-Israeli audience and Ramadan and the two Eids covered, or the skill's Hebrew-only scope stated explicitly | The skill's name claims the whole Israeli market. Silence is a mis-scope, not a scope decision. |
| RTL caption correctness stated per UAX #9: only a strong LTR letter sets a line left-to-right; digits and emoji are neutral and skipped; Latin-script hashtags flip a line and Hebrew-script ones do not; isolates (RLI/PDI) are the correct wrapper and RLM/LRM the fallback; Arabic uses ALM | This is the skill's flagship Israel-specific technical claim and the only place where being approximately right sends the user to the wrong repair. It was stated wrongly for two of its four cases until August 2026. |
| Hebrew subtitles and alt text on published media | Most social video is watched muted, and Israeli service-accessibility duties push captioned media toward being the baseline for a business. The skill contains a full video production spec, so this belongs with it. |
| Caption, hashtag and format limits taken only from platform developer or help documentation, with the document named | This skill shipped a marketing-blog caption limit as fact for a full cycle. |

## Should cover

| Item | Why |
|------|-----|
| Hebrew-language moderation reality: keep an appeals path, keep more than one page admin, keep off-platform copies | Automated enforcement on Hebrew content is less reliable than on English, and account continuity underpins the whole strategy. |
| WhatsApp Channels and Telegram channels as legitimate one-to-many organic distribution, with their anti-spam implications attached | The skill's own reference file ranks these as the highest-penetration surfaces in the country while excluding them from the platform mix. |
| Russian-speaking audience and its community groups | A real segment the skill does not name, secondary to Arabic because its Hebrew-language reach overlaps more. |
| Hebrew hashtag mechanics: no underscores, no spaces, Hebrew words concatenate | Correct as written; an input-behaviour convention rather than a rule with a legal or platform consequence. |
| Register: spoken Hebrew over formal written Hebrew, dugri tone | A well-attested market characteristic, but a matter of craft rather than correctness. |
| Link placement as practitioner practice, never as a documented Meta rule and never with a percentage | Meta's published demotion list does not include external links. Recorded here so a later cycle does not re-harden it into a rule. |
| Instagram ranking signals presented as industry read, bounded by what Instagram's own ranking explainer actually says | Recorded so the hedge added in August 2026 is not quietly dropped. |
| Posting times, days and cadences flagged as unsourced heuristics to test against the account's own analytics | No platform publishes optimal posting times for Israel, and the scheduler's numbers are the skill's most-acted-on output. |
| Platform ownership and policy volatility: re-verify TikTok claims against current TikTok documentation | A re-verification instruction rather than a substantive claim. |

## Out of scope (explicit)

- **Paid advertising**: campaign structure, budgets, bidding, targeting, ads-manager mechanics, ad-policy review. Excluded by the description; `israeli-paid-ads` covers it. Reviewed 2026-08-27 and kept out of scope. Ad-account consequences of an organic violation may be mentioned as a consequence but not instructed on.
- **Influencer and creator outreach**: sourcing, negotiating, contracting, or disclosing paid creator partnerships. The disclosure duty for a brand's own organic posts stays in Must-cover and is not delegated here.
- **SEO and long-form web content writing.** The mobile and desktop split is retained only as a caution against reusing social copy on a landing page.
- **Community management operations**: comment moderation policy, escalation trees, review management.
- **Analytics implementation**: pixels, conversion tracking, UTM taxonomies, attribution.
- **Design and video production execution.** Format specs and accessibility requirements are in scope; producing the asset is not.
- **Legal advice.** The statutes named here are cited so the skill flags a duty and routes the user onward. The skill states that a duty exists; it does not assess a specific post's legality.

## Authoritative sources

| Source | Authoritative for |
|--------|-------------------|
| Unicode Standard Annex #9 (UAX #9) | Bidirectional algorithm: base-direction resolution, character types, explicit formatting characters |
| TikTok Content Posting API reference | TikTok caption length and hashtag and mention counting |
| TikTok Community Guidelines and AI-generated content help articles | AI labelling duty, auto-label behaviour and irreversibility |
| TikTok music and commercial-use terms | Which audio a business account may use |
| Meta Instagram Platform media reference | Instagram caption, hashtag and @-tag limits |
| Meta Community Standards | Spam, inauthentic behaviour, group conduct |
| Meta Transparency Center, types of content we demote | The boundary of what may be claimed about reach reduction |
| Instagram's published ranking explainer | The boundary of what may be claimed about ranking signals |
| Meta's current AI-content labelling help page | Meta's AI disclosure scope and current control name |
| LinkedIn Business Solutions | LinkedIn organic content guidance |
| Communications (Telecommunications and Broadcasts) Law, Section 30A | Unsolicited commercial messages |
| Consumer Protection Law and the Consumer Protection and Fair Trade Authority | Commercial-content disclosure, misleading the consumer |
| Commission for Equal Rights of Persons with Disabilities | Accessibility of published digital media |
| Hebcal, or an equivalent Hebrew-calendar source | Current-year Gregorian dates for Hebrew-calendar holidays |
| DataReportal Digital Israel, current edition | Israeli platform audience sizes, with its ad-reach methodology stated |
| StatCounter Israel platform market share | Israeli web mobile and desktop split. Web only, never social |
| Central Bureau of Statistics | Population composition by language and community |

# Domain coverage checklist: Hebrew SEO and GEO

The canonical coverage list for this skill. Used by the expert-review gate to test what
is MISSING rather than what is wrong. Updated 2026-11-03 (v2.4.0).

## Must cover (core)

| Item | Why it is core |
|---|---|
| Intake before auditing (site type, area, languages, target searches, account access, platform, real hours) | The fix-first order differs completely between a local service and a SaaS page. |
| A prioritized fix list as the deliverable, with evidence per row | The user asks "what do I fix first"; a tutorial does not answer it. |
| Access and indexing blockers first: status, noindex, robots.txt per crawler and path, CDN refusing crawlers, text not in raw HTML | Nothing else matters while these fail. |
| Tool failures kept separate from site findings (local TLS, firewall refusing scripts) | Reporting the auditor's own failure as site downtime is a false diagnosis. |
| Search generative AI control in Search Console | Google makes inclusion there a condition of eligibility for AI Overviews and AI Mode (all sites since 31 August 2026). |
| Google Business Profile for local businesses: category, hours incl. holidays, NAP match | Often the largest lever for an Israeli local service business. |
| Hebrew keyword forms measured against real queries (prefixes with ה-elision, gershayim spellings) | Generated forms nobody searches for are noise; the Search Console export settles it. |
| hreflang per Google's rules: language-only code valid, reciprocity, one method, audience-based x-default | Folklore versions ("always he-IL", "sitemap required", "x-default English") mislead. |
| `.co.il` as a geotargeting signal; server location irrelevant for a ccTLD; no Search Console country targeting | Prevents hosting moves and phantom "google.co.il property" setups. |
| Israeli LocalBusiness schema: real week (do not assume Shabbat closure), `specialOpeningHoursSpecification` for holidays, English `dayOfWeek` | Israeli hours do not fit the Mon-Fri default; holidays are when hours change most. |
| `+972` phone as Google's recommendation (not a validation rule), `ILS` currency | Accurate framing of what is required versus recommended. |
| Training vs search-index vs user-triggered crawlers, per vendor (OpenAI, Anthropic, Perplexity, Google, Apple, Mistral) | Allowing only training crawlers leaves the site ineligible for AI search citations. |
| Markup Google no longer rewards (FAQ since 7 May 2026, HowTo since 2023, Speakable US English news only) | Prevents promising clients a result that does not exist. |
| Google's own AI optimization guidance: still SEO, no special markup, fan-out pages are scaled content abuse | The primary source on what Google wants. |
| Princeton GEO methods, ranked per Table 1, with the metric and language caveats | The paper is English, 2023 engines; keyword stuffing is below baseline on word count only. |
| No invented statistics or quotes | GEO advice invites fabrication; it damages trust and can create legal exposure. |
| Search Console Generative AI reports: impressions only, all sites since 31 August 2026 | Overstating this misleads clients. |
| Measurement in four layers (access, citability, surfacing, rankings) | "Not crawled yet" and "crawled but not chosen" look identical. |
| Core Web Vitals as LCP, INP, CLS | INP replaced FID. |
| E-E-A-T with Israeli signals, YMYL handled by licensed professionals | Hebrew authorship, Israeli publications, +972 contact. |
| A no-code route for each check | Many users are business owners, not developers. |
| DataForSEO scripts usable for Israel: `2376` + `he`, Labs refuses `en`, sandbox, cost | Wrong defaults silently returned US English data before 2.4.0. |

## Should cover (advanced)

| Item | Why |
|---|---|
| `llms.txt` with honest framing (v2 of the proposal, August 2026) | Widely oversold. Google Search does not use it. |
| Open Knowledge Format (OKF) | Google Cloud spec, v0.2. Same caveat as llms.txt. |
| Bing/Copilot: Bing Webmaster Tools, IndexNow, AI Performance report (sampled grounding queries) | Copilot citations depend on Bing. |
| Israeli local citation directories and NAP consistency | Off-page signal specific to the market. |
| Hebrew URL slugs (UTF-8 versus transliterated) | Routine Israeli decision; Google recommends the audience's language and UTF-8. Covered in Step 4. |
| AI referral segmentation in analytics | Mentioned at referrer-domain level only; per-engine UTM conventions not verified. |
| Platform defaults (Wix, WordPress, Shopify) and accessibility overlay plugins | Common Israeli setups with known SEO traps. Not yet in the skill body. |

## Out of scope (explicit)

| Item | Rationale | Reviewed |
|---|---|---|
| Paid advertising campaigns (Google Ads, Meta Ads) | Named as an anti-trigger in the description. A separate discipline. Users do ask, and the answer is a different skill. | 2026-11-03 |
| Social media marketing and organic social | Same. | 2026-11-03 |
| Non-Hebrew international SEO beyond the he/en pair | The differentiator is the Israeli market. | 2026-11-03 |
| Link buying, PBNs, and other manipulative off-page tactics | Against Google's spam policies. | 2026-11-03 |
| Per-engine reverse-engineered ranking weights stated as fact | No vendor publishes them; earlier cycles removed untraceable figures. Still not capturable. | 2026-11-03 |
| Legal review of advertising claims and regulated-profession advertising rules | A user may ask; the answer is a lawyer or a legal skill, not SEO. | 2026-11-03 |
| Website accessibility compliance (IS 5568) | A user may ask; it is a separate compliance topic. | 2026-11-03 |
| Multi-page crawling | The free script audits one URL per run by design; a crawler (Screaming Frog free tier) covers whole-site crawls. | 2026-11-03 |

## Authoritative sources

- Google Search Central: https://developers.google.com/search
- Google AI features guidance: https://developers.google.com/search/docs/appearance/ai-features
- Google AI optimization guide: https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- Search generative AI control: https://support.google.com/webmasters/answer/16908024?hl=en
- Google documentation updates: https://developers.google.com/search/updates
- Search Console generative AI reports: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- OpenAI bots: https://developers.openai.com/api/docs/bots
- Anthropic crawlers: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity bots: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Mistral robots: https://docs.mistral.ai/robots
- Apple crawler: https://support.apple.com/en-us/119829
- Princeton GEO paper: https://arxiv.org/abs/2311.09735
- DataForSEO docs: https://docs.dataforseo.com/v3/
- llms.txt proposal: https://llmstxt.org
- Academy of the Hebrew Language: https://hebrew-academy.org.il

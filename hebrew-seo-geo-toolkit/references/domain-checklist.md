# Domain coverage checklist: Hebrew SEO and GEO

The canonical coverage list for this skill. Used by the expert-review gate to test what
is MISSING rather than what is wrong. Updated 2026-08-11 (v2.3.0).

## Must cover (core)

| Item | Why it is core |
|---|---|
| Hebrew morphological keyword variants (prefixes ha-/ve-/be-/le-/me-/she-, plural, smikhut) | A single surface form misses most Hebrew search traffic. No other SEO skill handles this. |
| `he-IL` hreflang, bidirectional, with `x-default` | Google's hreflang documentation requires reciprocal annotation; bare `he` weakens google.co.il geo-targeting. |
| `.co.il` domain and Google Search Console property setup | ISOC-IL is the registry; the `.co.il` property must be registered separately from `.com`. |
| Israeli LocalBusiness schema: Sunday-Thursday week, Friday early close, Saturday closed | Israeli business hours do not fit the Mon-Fri default that agents assume. |
| `+972` phone format and `ILS` currency in structured data | Local `0X-` formatting fails schema validation. |
| Kosher certification representation (Rabbanut, Badatz) | Domain-specific to the Israeli market and a common query intent. |
| Training vs search-index crawler split, per platform | `GPTBot` vs `OAI-SearchBot`, and `ClaudeBot` vs `Claude-SearchBot`. Allowing only the training bot leaves the site ineligible for search citations. This is the highest-consequence configuration error in the whole domain. |
| Live/user fetchers as a third bot category | `ChatGPT-User`, `Claude-User`, `Perplexity-User`. Perplexity documents that `Perplexity-User` generally ignores robots.txt. |
| `Google-Extended` as an opt-out token, not a crawler | Blocking it does not affect Search ranking or AI Overview citations. |
| Google AI Overviews AND AI Mode as two distinct surfaces | Hebrew and Israel both appear on Google's AI Mode availability list; they behave differently and are reported together but are not the same product. |
| Query fan-out and its content implication | Both surfaces may issue several related searches per query, which is the reason to answer adjacent sub-questions on-page. |
| Honest statement of what Google requires for AI surfaces | Google states no additional requirements or special optimizations are needed. Any claim of a secret AI-ranking lever contradicts the primary source. |
| Search Console generative AI reports: what they actually expose | Impressions, pages, countries, devices, dates. No clicks/CTR/position/queries in this version, subset rollout. Overstating this misleads clients. |
| Princeton GEO methods, ranked per the paper's own table | Includes that keyword stuffing scores BELOW baseline. |
| Measurement layered by latency (access, citability, surfacing, rankings) | "Not crawled yet" and "crawled but not chosen" are indistinguishable in the answer box and have opposite fixes. |
| E-E-A-T with Israeli signals, and YMYL handling in Hebrew | Israeli publications, Hebrew authorship, +972 contact, professional review for medical/financial/legal. |
| RTL rendering correctness | `dir="rtl"`, CSS logical properties. |

## Should cover (advanced)

| Item | Why |
|---|---|
| `llms.txt` with honest, evidence-calibrated framing | Widely oversold. Google Search does not use it; treat as optional protocol-layer registration only. |
| Open Knowledge Format (OKF) | Google Cloud spec, currently v0.2. Same caveat as llms.txt: nothing crawls the open web for it yet. |
| `SpeakableSpecification` | Useful for extraction framing; Google's own eligibility for speakable rich results is narrow. |
| FAQPage schema | Still useful for AI extraction and parsing even though Google restricted FAQ RICH RESULTS to authoritative government and health sites in 2023. Do not promise rich-result eligibility to an ordinary business site. |
| Bing/Copilot specifics | `bingbot`, `adidxbot`, `MicrosoftPreview`, IndexNow, Bing Webmaster Tools. |
| Israeli local citation directories and NAP consistency | Off-page signal specific to the market. |
| Hebrew vs English page pairing for AI surfaces | Hebrew-only pages are cited less; an EN alternate with hreflang serves both. |

## Out of scope (explicit)

| Item | Rationale | Reviewed |
|---|---|---|
| Paid advertising campaigns (Google Ads, Meta Ads) | Named as an anti-trigger in the description. A separate discipline with separate skills. | 2026-08-11 |
| Social media marketing and organic social | Same. The skill routes search and AI-answer surfaces only. | 2026-08-11 |
| Non-Hebrew international SEO beyond the he/en pair | The skill's whole differentiator is the Israeli market; generic multi-market hreflang strategy belongs elsewhere. | 2026-08-11 |
| Link buying, PBNs, and other manipulative off-page tactics | Against Google's spam policies. Not a coverage gap. | 2026-08-11 |
| Per-engine reverse-engineered ranking weights stated as fact | Vendor write-ups circulate untraceable percentages. Prior cycles deliberately removed these; do not reinstate without a traceable publisher. | 2026-08-11 |

## Authoritative sources

- Google Search Central: https://developers.google.com/search
- Google AI features guidance: https://developers.google.com/search/docs/appearance/ai-features
- Search Console generative AI reports: https://developers.google.com/search/blog/2026/06/gen-ai-performance-reports
- OpenAI bots: https://developers.openai.com/api/docs/bots
- Anthropic crawlers: https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler
- Perplexity bots: https://docs.perplexity.ai/docs/resources/perplexity-crawlers
- Princeton GEO paper: https://arxiv.org/abs/2311.09735
- llms.txt proposal: https://llmstxt.org
- Academy of the Hebrew Language: https://hebrew-academy.org.il

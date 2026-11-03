# AI Platforms and Crawlers: What Each Vendor Documents

Re-enumerated from each vendor's own page on 2026-11-03. This file states what the vendors publish. No vendor publishes internal ranking weights for its AI engine; write-ups that print them (citation-share percentages, "reranking layers", "visibility multipliers") could not be traced to a publisher and are deliberately left out. Do not reinstate them.

---

## Crawler list

### OpenAI (developers.openai.com/api/docs/bots)

| Token | Role | If you block it |
|-------|------|-----------------|
| `OAI-SearchBot` | Search index for ChatGPT search | "Sites that are opted out of OAI-SearchBot will not be shown in ChatGPT search answers, though can still appear as navigational links." |
| `GPTBot` | Training crawler | Content is not used to train OpenAI foundation models. Search is unaffected. |
| `ChatGPT-User` | Fetches a page when a user asks | "Because these actions are initiated by a user, robots.txt rules may not apply." It is not used to decide search inclusion. |
| `OAI-AdsBot` | Checks pages submitted as ChatGPT ads | Only relevant to advertisers. |

OpenAI says a robots.txt change can take about 24 hours to reach search results, and that if both `GPTBot` and `OAI-SearchBot` are allowed it may use one crawl for both purposes.

### Anthropic (support.claude.com article 8896518)

| Token | Role | If you block it |
|-------|------|-----------------|
| `Claude-SearchBot` | Search index | Anthropic: it "may reduce your site's visibility and accuracy in user search results." |
| `ClaudeBot` | Training crawler | The site's future materials "should be excluded from our AI model training datasets". |
| `Claude-User` | Fetches a page when a user asks | May reduce visibility for user-directed web search. |

Anthropic says its bots honor robots.txt, supports `Crawl-delay`, and asks site owners to set the rule on every subdomain they want to opt out. It publishes the tokens but no full user-agent strings. `anthropic-ai` and `Claude-Web` are older names that still circulate in examples and appear nowhere on the current page.

### Perplexity (docs.perplexity.ai, Perplexity Crawlers)

| Token | Role | Note |
|-------|------|------|
| `PerplexityBot` | Search index | "It is not used to crawl content for AI foundation models." |
| `Perplexity-User` | Fetches a page when a user asks | "Since a user requested the fetch, this fetcher generally ignores robots.txt rules." |

Perplexity says changes may take up to 24 hours to be reflected.

### Google (developers.google.com/crawling)

- `Googlebot` crawls for Search. Google's AI-features page names Googlebot's robots.txt rules as the crawl control for Search, which includes AI Overviews and AI Mode.
- `Google-Extended` is a robots.txt token, not a crawler. It governs whether crawled content may be used to train Gemini models and "for grounding" in Gemini Apps and Grounding with Google Search on Vertex AI. Google: it "does not impact a site's inclusion in Google Search nor is it used as a ranking signal".
- To leave AI Overviews, AI Mode and Discover's generative features while staying in Search, use the **Search generative AI control** in Search Console settings (all websites as of 31 August 2026). Exclusion takes effect within 1-2 days; it does not affect training.

### Apple (support.apple.com/en-us/119829)

- `Applebot` powers search in Spotlight, Siri and Safari, and its data may ground Apple's AI answers. Apple: publishers "can opt out of their content being used in these broad world knowledge answers by applying the nosnippet meta tag".
- `Applebot-Extended` is the training opt-out token.

### Mistral (docs.mistral.ai/robots)

| Token | Role |
|-------|------|
| `MistralAI-Index` | Search index for Mistral search, used to answer questions in Vibe |
| `MistralAI-Training` | Training crawler |
| `MistralAI-User` | Fetches a page when a user asks in Vibe |

### Others

- `Meta-ExternalAgent`: Meta's crawler for its AI products. Meta documents further agents on its web-crawlers page; check it before writing a Meta-specific rule.
- `CCBot`: Common Crawl, used downstream by many model trainers.
- `Bingbot`: Bing's crawler. Bing's AI Performance report covers Copilot citations, so Bing indexing matters for Copilot.

### Three categories, one rule

1. **Search-index crawlers** (`OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, `MistralAI-Index`, plus `Googlebot` and `Bingbot`) decide whether you can be cited. Allow them.
2. **Training crawlers and tokens** (`GPTBot`, `ClaudeBot`, `Applebot-Extended`, `MistralAI-Training`, `CCBot`) are a business decision. Blocking them does not remove you from AI search. **`Google-Extended` is the exception:** it also controls grounding in the Gemini app, so blocking it keeps you in Google Search, AI Overviews and AI Mode but removes your content as a grounding source in Gemini Apps.
3. **User-triggered fetchers** (`ChatGPT-User`, `Claude-User`, `Perplexity-User`, `MistralAI-User`) run when someone asks. OpenAI and Perplexity say robots.txt may not apply to theirs.

**One group per crawler.** Google's robots.txt spec: "Only one group is valid for a particular crawler." A crawler obeys the group that names it most specifically and ignores the `*` group entirely. So adding `User-agent: OAI-SearchBot` / `Allow: /` to a file whose `*` group holds Disallow rules exempts that bot from every one of those rules. Copy the `*` Disallow lines into each named group you add.

robots.txt is not the only gate. A CDN or firewall can refuse a crawler that robots.txt allows; Cloudflare announced in July 2025 that it was "changing the default to block AI crawlers". `scripts/seo_audit.py` requests the page with the search crawlers' user agents to surface this.

---

## Per platform

### Google AI Overviews and AI Mode

- Two separate surfaces, both available in Hebrew and in Israel.
- Google: "There are no additional requirements to appear in AI Overviews or AI Mode, nor other special optimizations necessary." Both may use "query fan-out", issuing several related searches behind one query.
- Google's AI optimization guide adds that this is "still SEO", that no special files, markup or chunking are needed, and that pages created for every query variation "primarily to manipulate rankings or generative AI responses" violate the scaled content abuse policy.
- Eligibility also requires the Search generative AI control to be left on.

### ChatGPT search

- Inclusion is governed by `OAI-SearchBot`. OpenAI's crawler page does not say which third-party index, if any, supplements it, so do not tell a client it "uses Bing".

### Perplexity

- Inclusion is governed by `PerplexityBot`. Perplexity's crawler page names no other index.

### Claude

- Inclusion is governed by `Claude-SearchBot`. Third-party reports attribute Claude's web search to Brave, but Anthropic's crawler documentation names no search provider. Treat it as reported, not confirmed, and do not state it to a client.

### Microsoft Copilot

- Verify the site in Bing Webmaster Tools and submit a sitemap; IndexNow speeds up discovery of new URLs.
- Bing's **AI Performance** report (public preview since February 2026) shows how often content is cited across Copilot and Bing's AI summaries, with a sample of grounding queries. A Topics Portfolio beta was added in October 2026.

---

## Classic Google ranking, briefly

What Google documents: helpful, people-first content; links as one of many signals; page experience including Core Web Vitals; mobile-friendly pages; HTTPS; spam policies. No Google documentation lists bounce rate or dwell time as ranking signals, so do not present them as such.

| Metric | Good (web.dev) |
|--------|------|
| LCP (Largest Contentful Paint) | 2.5 seconds or less |
| INP (Interaction to Next Paint, replaced FID) | 200 milliseconds or less |
| CLS (Cumulative Layout Shift) | 0.1 or less |

---

## Universal practice

1. Allow the search-index crawlers in robots.txt and check the CDN does not refuse them.
2. Keep the Search generative AI control on unless the owner chooses otherwise.
3. Server-render the page text.
4. Use structured data that Google still supports (Organization, LocalBusiness, Product, Article, BreadcrumbList).
5. Include real statistics and quotes, each with its source.
6. Update content substantively, not by changing the date.
7. Verify in Bing Webmaster Tools for Copilot.

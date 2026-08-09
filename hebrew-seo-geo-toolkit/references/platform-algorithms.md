# Platform Ranking Algorithms

Detailed ranking factors for AI search engines and traditional search engines (2025-2026).

---

## 1. ChatGPT Ranking Factors

### Core Ranking System

ChatGPT uses a **two-phase system**:
1. **Pre-training Knowledge** - Built from diverse datasets (Wikipedia, books, web)
2. **Real-time Retrieval** - Web browsing for current information

### Ranking Factor Weights

No published weighting for these factors is traceable to a named study, so treat the order as a rough priority, not a formula.

| Factor | Priority | Details |
|--------|----------|---------|
| **Authority & Credibility** | Highest | Branded domains preferred over third-party |
| **Content Quality & Utility** | High | Clear structure, comprehensive answers |
| **Platform Trust** | Moderate | Wikipedia, Reddit, Forbes prioritized |

### Directional Findings

These are directional patterns reported across industry write-ups. We could not trace them to a study we can cite, so use them to prioritise work, not as targets.

| Metric | Direction |
|--------|-----------|
| **Referring Domains** | Strongest single predictor of being cited |
| **Domain Trust Score** | Higher trust score correlates with more citations |
| **Content Recency** | Recently updated content is cited more often |
| **Branded vs Third-party** | Branded domains are cited more than third-party pages |

### ChatGPT Top Citation Sources

Ordering only. We could not trace the underlying citation-share figures to a publishable source, so they are omitted rather than guessed.

| Rank | Source |
|------|--------|
| 1 | Wikipedia |
| 2 | Reddit |
| 3 | Forbes |
| 4 | Brand Official Sites |
| 5 | Academic Sources |

### Content-Answer Fit

Ranked by observed importance. The weightings previously printed here were not traceable to a named study and have been removed.

| Factor | Importance | Note |
|--------|-----------|------|
| **Content-Answer Fit** | Most important | Match ChatGPT's response style |
| **On-Page Structure** | Secondary | Clear headings, formatting |
| **Domain Authority** | Secondary | Helps retrieval, not citation |
| **Query Relevance** | Secondary | Match user intent |
| **Content Consensus** | Minor | Agreement among sources |

### Optimization Checklist

- [ ] Build strong backlink profile (quality > quantity)
- [ ] Update content within 30 days
- [ ] Use clear H1/H2/H3 structure
- [ ] Include verifiable statistics with citations
- [ ] Write in ChatGPT's conversational style
- [ ] Ensure domain has high trust score

---

## 2. Perplexity AI Ranking Factors

### Architecture

Perplexity uses **Retrieval-Augmented Generation (RAG)** with a **3-layer reranking system**:

1. **Layer 1 (L1)**: Basic relevance retrieval
2. **Layer 2 (L2)**: Traditional ranking factors scoring
3. **Layer 3 (L3)**: ML models for quality evaluation (can discard entire result sets)

### Core Ranking Factors

| Factor | Details |
|--------|---------|
| **Authoritative Domain Lists** | Manual lists: Amazon, GitHub, academic sites get inherent boost |
| **Freshness Signals** | Time decay algorithm; new content evaluated quickly |
| **Semantic Relevance** | Content similarity to query (not keyword matching) |
| **Topical Weighting** | Tech, AI, Science topics get visibility multipliers |
| **User Engagement** | Click rates, weekly performance metrics |
| **New Post Performance** | Early clicks significantly boost visibility |

### Perplexity Sonar Model Insights

| Signal | Impact |
|--------|--------|
| **FAQ Schema (JSON-LD)** | Pages with FAQ blocks cited more often |
| **PDF Documents** | Publicly hosted PDFs prioritized |
| **Content Velocity** | Speed of publishing matters more than keyword density |
| **Semantic Payloads** | Clear, atomic paragraphs preferred |
| **YouTube Sync** | YouTube titles matching trending queries get boost |

### Technical Requirements

```
# robots.txt - Allow PerplexityBot
User-agent: PerplexityBot
Allow: /

# Provide clean sitemap
Sitemap: https://example.com/sitemap.xml
```

### Optimization Checklist

- [ ] Allow PerplexityBot in robots.txt
- [ ] Implement FAQ Schema markup
- [ ] Create publicly accessible PDF resources
- [ ] Use Article schema with timestamps
- [ ] Focus on semantic relevance, not keywords
- [ ] Build topical authority in your niche

---

## 3. Google AI Overview (SGE) Ranking Factors

### Architecture

Google AI Overviews use multiple AI models:
- **PaLM2** - Language understanding
- **MUM** - Multimodal understanding
- **Gemini** - Advanced reasoning

### 5-Stage Source Prioritization Pipeline

1. **Retrieval** - Identify candidate sources
2. **Semantic Ranking** - Evaluate topical relevance
3. **LLM Re-ranking** - Assess contextual fit (using Gemini)
4. **E-E-A-T Evaluation** - Filter for expertise/authority/trust
5. **Data Fusion** - Synthesize from multiple sources with citations

### What This Means in Practice

The percentages that used to sit here (AI Overview coverage, overlap with the traditional top ten, an SGE visibility multiplier) came from vendor write-ups we could not trace to a publisher, so they have been removed. The directional picture that survives:

- AI Overviews now appear on a large and growing share of Google queries.
- The set of pages cited in an AI Overview overlaps only partly with the traditional top ten, so a strong classic ranking does not guarantee a citation.
- Classic ranking signals still carry most of the weight, with newer AI-specific signals layered on top.
- Pages written for AI answer formats can gain substantial visibility they would not get from classic ranking alone.

### Ranking Factors

| Factor | Details |
|--------|---------|
| **E-E-A-T** | Experience, Expertise, Authoritativeness, Trustworthiness |
| **Structured Data** | Schema markup helps AI understand content |
| **Knowledge Graph** | Being in Google's Knowledge Graph = boost |
| **Topical Authority** | Content clusters + internal linking |
| **Multimedia** | Images/videos in multi-modal responses |
| **Authoritative Citations** | Trusted references are one of the strongest levers on whether you get cited |
| **Authoritative Tone** | A confident, expert voice helps, though the Princeton GEO paper found the effect small on its own |

### Content Requirements

```
Traditional SEO still matters:
- Quality backlinks
- Original, helpful content
- Fast page speed
- Mobile-friendly design
- Secure (HTTPS)
```

### Optimization Checklist

- [ ] Implement comprehensive Schema markup
- [ ] Build topical authority with content clusters
- [ ] Include authoritative citations and references
- [ ] Use E-E-A-T signals (author bios, credentials)
- [ ] Optimize for Google Merchant Center (e-commerce)
- [ ] Target informational "how-to" queries

---

## 4. Microsoft Copilot / Bing AI Ranking Factors

### Architecture

Copilot is integrated into:
- Microsoft Edge browser
- Windows 11
- Microsoft 365 apps
- Bing Search

Uses **Bing Index** as primary data source.

### Ranking Factors

| Factor | Details |
|--------|---------|
| **Bing Index** | Must be indexed by Bing to be cited |
| **Microsoft Ecosystem** | LinkedIn, GitHub mentions provide boost |
| **Crawlability** | BingBot + PermaBot must have access |
| **Page Speed** | < 2 seconds load time |
| **Schema Markup** | Helps Copilot understand content |
| **Entity Clarity** | Clear definitions of entities/concepts |

### Technical Requirements

```
# robots.txt
User-agent: Bingbot
Allow: /

User-agent: msnbot
Allow: /

# Submit to Bing Webmaster Tools
# Use IndexNow for faster indexing
```

### Optimization Checklist

- [ ] Submit site to Bing Webmaster Tools
- [ ] Ensure Bingbot can crawl all pages
- [ ] Use IndexNow for new content
- [ ] Optimize page speed (< 2 seconds)
- [ ] Clear entity definitions in content
- [ ] Build presence on LinkedIn, GitHub

---

## 5. Claude AI Ranking Factors

### Architecture

**Important:** Claude uses **Brave Search**, NOT Google or Bing!

Claude decides when to search based on:
- Query freshness requirements
- Specificity of question
- User intent

### Ranking Factors

| Factor | Details |
|--------|---------|
| **Brave Index** | Must be indexed by Brave Search |
| **Query Rewriting** | Claude reformulates queries for search |
| **Factual Density** | Data-rich content preferred |
| **Structural Clarity** | Easy to extract information |
| **Source Authority** | Trustworthy, well-sourced content |

### Key Statistic

**Crawl-to-Refer Ratio: 38,065:1**
- Claude consumes massive amounts of content
- Very selective about what it cites
- Quality and relevance are critical

### Technical Requirements

```
# robots.txt
User-agent: ClaudeBot
Allow: /

User-agent: anthropic-ai
Allow: /
```

### Optimization Checklist

- [ ] Ensure Brave Search indexing
- [ ] Allow ClaudeBot in robots.txt
- [ ] Create high factual density content
- [ ] Use clear, extractable structure
- [ ] Include verifiable data points
- [ ] Cite authoritative sources

---

## 6. Traditional Google SEO Ranking Factors (2026)

### Core Ranking Systems

| System | Purpose |
|--------|---------|
| **PageRank** | Link-based authority (still relevant) |
| **BERT** | Natural language understanding |
| **RankBrain** | Machine learning ranking |
| **Helpful Content** | Rewards people-first content |
| **Spam Detection** | Filters low-quality content |

### Top 10 Ranking Factors

| Rank | Factor | Details |
|------|--------|---------|
| 1 | **Backlinks** | Quality referring domains (core ranking system) |
| 2 | **E-E-A-T** | Experience, Expertise, Authority, Trust |
| 3 | **Content Quality** | Original, comprehensive, helpful |
| 4 | **Page Experience** | Core Web Vitals (LCP, FID, CLS) |
| 5 | **Mobile-First** | Non-mobile sites may not be indexed |
| 6 | **Search Intent Match** | Content matches user query intent |
| 7 | **Content Freshness** | Regular updates signal activity |
| 8 | **Technical SEO** | Crawlable, indexable, HTTPS |
| 9 | **User Signals** | Dwell time, bounce rate, CTR |
| 10 | **Structured Data** | Schema markup for rich results |

### Core Web Vitals

| Metric | Good | Needs Improvement | Poor |
|--------|------|-------------------|------|
| **LCP** (Largest Contentful Paint) | < 2.5s | 2.5-4s | > 4s |
| **FID** (First Input Delay) | < 100ms | 100-300ms | > 300ms |
| **CLS** (Cumulative Layout Shift) | < 0.1 | 0.1-0.25 | > 0.25 |

### E-E-A-T Guidelines

| Signal | How to Demonstrate |
|--------|-------------------|
| **Experience** | First-hand experience, case studies |
| **Expertise** | Author credentials, detailed knowledge |
| **Authoritativeness** | Backlinks, mentions, citations |
| **Trustworthiness** | Accurate info, transparent, secure site |

### Optimization Checklist

- [ ] Build quality backlinks (guest posts, PR, original research)
- [ ] Create comprehensive, original content
- [ ] Optimize Core Web Vitals
- [ ] Ensure mobile-friendly design
- [ ] Use HTTPS
- [ ] Implement Schema markup
- [ ] Match content to search intent
- [ ] Update content regularly
- [ ] Add author bios with credentials
- [ ] Include E-E-A-T signals

---

## Cross-Platform Optimization Summary

| Platform | Primary Index | Key Factor | Unique Requirement |
|----------|--------------|------------|-------------------|
| ChatGPT | Web (Bing-based) | Domain Authority | Content-Answer Fit |
| Perplexity | Own + Google | Semantic Relevance | FAQ Schema |
| Google SGE | Google | E-E-A-T | Knowledge Graph |
| Copilot | Bing | Bing Index | MS Ecosystem |
| Claude | Brave | Factual Density | Brave Indexing |
| Google (traditional) | Google | Backlinks | Core Web Vitals |

### Universal Best Practices

1. **Allow all major bots** in robots.txt
2. **Implement Schema markup** (FAQPage, Article, Organization)
3. **Build authoritative backlinks**
4. **Update content regularly** (within 30 days)
5. **Use clear structure** (H1 > H2 > H3, lists, tables)
6. **Include statistics and citations**
7. **Optimize page speed** (< 2 seconds)
8. **Ensure mobile-friendly design**

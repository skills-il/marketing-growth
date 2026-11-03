# GEO Research: Princeton Study & Optimization Methods

## Paper Overview

**Title:** GEO: Generative Engine Optimization  
**Authors:** Aggarwal, Murahari, Rajpurohit, Kalyan, Narasimhan, Deshpande (IIT Delhi, Princeton University, independent researchers)  
**Published:** November 2023 (arXiv:2311.09735)  
**Accepted:** KDD 2024 (30th ACM SIGKDD Conference)  
**Link:** https://arxiv.org/abs/2311.09735

---

## Key Findings

### What is GEO?

**Generative Engine Optimization (GEO)** is a novel framework to help content creators improve their visibility in **generative engine responses** (AI search engines like ChatGPT, Perplexity, Google AI Overviews and AI Mode).

Unlike traditional SEO (ranking in search results), GEO focuses on **being cited** by AI systems.

### Core Results

The methods below are listed in the paper's own order of effectiveness (Table 1): Quotation Addition, Statistics Addition, Fluency Optimization, Cite Sources, Technical Terms, Easy-to-Understand, Authoritative Tone, then Unique Words and Keyword Stuffing, which the paper groups as non-performing. Per-method percentage figures circulating online do not match the paper and are not reproduced here.

**Two caveats before applying this to a Hebrew site:**

1. The order above is from the Position-Adjusted Word Count metric. On the paper's Subjective Impression metric, Authoritative ranks near the top and Keyword Stuffing scores slightly above the baseline, so "keyword stuffing is worse than doing nothing" holds for word count only. Avoid it anyway: it violates Google's spam policies.
2. The experiments used English queries against 2023-era engines (a research engine and Perplexity). The effect on Hebrew content in today's engines has not been measured. Treat the methods as a sound editing checklist, not a guaranteed lift.

Google's own position, for its AI features, is that optimizing for generative AI search "is optimizing for the search experience, and thus still SEO" and that no special markup or chunking is required.

**Never invent the inputs.** Statistics Addition and Quotation Addition work only with real, attributable numbers and quotes. The examples below use placeholders on purpose.

| Metric | Result |
|--------|--------|
| **Maximum Visibility Boost** | Up to 40% overall; the best individual methods improve on the baseline by 41% on Position-Adjusted Word Count and 28% on Subjective Impression (Aggarwal et al., GEO, 2023) |
| **Low-ranking Sites Boost** | Cite Sources gave a 115.1% visibility increase for sites ranked fifth in the SERP (Aggarwal et al., GEO, 2023) |
| **GEO-bench Dataset** | 10,000+ queries across domains |
| **Tested on** | Perplexity.ai (commercial GE) |

### Why GEO Matters

1. **Traditional search engines are being replaced** by generative engines
2. **Content creators have little control** over how their content appears in AI responses
3. **GEO provides systematic methods** to improve visibility
4. **Different domains need different strategies** - no one-size-fits-all

---

## The 9 Optimization Methods

### Method 1: Cite Sources

**What:** Add authoritative citations and references to your content.

**Why it works:** AI systems prefer content that appears well-researched and credible. Citations signal authority.

**How to apply:**
```markdown
# Before
"Studies show that AI improves productivity."

# After
"According to <named study, institution, year>, <measured effect> (<link>)."
```

**Best for:** All content types, especially academic/professional topics.

---

### Method 2: Statistics Addition

**What:** Include specific numbers, data points, and quantitative information.

**Why it works:** AI systems prioritize factual, verifiable information. Numbers make content more quotable.

**How to apply:**
```markdown
# Before
"Many companies use AI for customer service."

# After
"<N>% of <population> now <do X>, according to <named source, year>."
(Fill every placeholder from a real, linkable source. Never invent the figure.)
```

**Best for:** Business, finance, technology, health content.

---

### Method 3: Quotation Addition

**What:** Add expert quotes with proper attribution.

**Why it works:** Quotes from recognized experts boost credibility and provide extractable content for AI.

**How to apply:**
```markdown
# Before
"AI will transform the workforce."

# After
"'<exact words, copied from the source>,' said <name>, <role>, in <publication, date>."
(Quote only words you can link to. Never paraphrase into quotation marks.)
```

**Best for:** Law, academic, news, thought leadership content.

---

### Method 4: Authoritative Tone

**What:** Write with confidence and expertise.

**Why it works:** AI systems assess content quality partly through linguistic signals of authority.

**How to apply:**
```markdown
# Before
"This might help with SEO, I think."

# After
"This strategy improves <outcome>. In our own data from <period>, <measured result> (<method, sample size>)."
(Use your own measured data or a cited source; never a round number you cannot show.)
```

**Best for:** Business, professional services, technical documentation.

---

### Method 5: Easy-to-Understand

**What:** Simplify complex concepts for broader accessibility.

**Why it works:** AI aims to provide helpful answers to users of all knowledge levels.

**How to apply:**
```markdown
# Before
"The RAG architecture utilizes vector embeddings for semantic retrieval 
in conjunction with LLM-based generation."

# After
"RAG (Retrieval-Augmented Generation) works like a research assistant: 
it first searches for relevant information, then uses AI to write a 
coherent answer based on what it found."
```

**Best for:** Health, education, general consumer content.

---

### Method 6: Technical Terms

**What:** Include domain-specific terminology appropriately.

**Why it works:** Technical terms signal expertise and help AI match content to specialized queries.

**How to apply:**
```markdown
# Before
"The website loads slowly."

# After
"The website suffers from poor Core Web Vitals: LCP (Largest Contentful 
Paint) exceeds 4 seconds, and CLS (Cumulative Layout Shift) scores 0.3, 
indicating significant layout instability."
```

**Best for:** Technology, science, medical, legal content.

---

### Method 7: Unique Words

**What:** Increase vocabulary diversity and use distinctive phrasing.

**Why it works:** Diverse vocabulary indicates depth of knowledge and makes content more distinguishable.

**How to apply:**
- Use synonyms and varied terminology
- Avoid repetitive phrasing
- Include industry-specific jargon where appropriate
- Add contextual variations

**Best for:** All content types.

---

### Method 8: Fluency Optimization

**What:** Improve readability, flow, and grammatical quality.

**Why it works:** Well-written content is easier for AI to parse and more likely to be selected as authoritative.

**How to apply:**
- Use clear sentence structure
- Maintain logical flow between paragraphs
- Eliminate redundancy
- Use transition words
- Keep paragraphs focused (2-3 sentences)

**Best for:** All content types.

---

### Method 9: Keyword Stuffing (non-performing) ⚠️

**What:** Overloading content with target keywords.

**Why to avoid it:** In the paper it scored below the baseline on Position-Adjusted Word Count (on Subjective Impression it was slightly above), and it violates Google's spam policies. It earns nothing reliable and risks a penalty.

**Avoid:**
```markdown
# BAD - Keyword stuffing
"SEO optimization for SEO is the best SEO strategy. Our SEO experts 
provide SEO services for all your SEO needs. SEO is important for SEO."

# GOOD - Natural writing
"Search engine optimization is essential for online visibility. Our 
experts help businesses improve their search rankings through strategic 
content development and technical improvements."
```

---

## Best Combination

The paper tested pairs of its four strongest methods (Quotation Addition, Statistics Addition, Fluency Optimization, Cite Sources) and reports one best pair: **Fluency Optimization + Statistics Addition**. It did not test combinations involving the other methods and gives no per-industry recommendations, so do not attribute any to it.

---

## GEO Metrics

The paper introduces visibility metrics for evaluating GEO effectiveness:

### Position-Adjusted Word Count

Measures how much of your content appears in AI responses, weighted by position (earlier = better).

### Subjective Impression

Seven sub-metrics (relevance, influence, uniqueness, subjective position, subjective count, click likelihood, diversity), each scored by an LLM evaluator (G-Eval with GPT-3.5), not by human raters.

### Word count and position

The two components of Position-Adjusted Word Count, also reported separately.

---

## Implementation Checklist

### Content Optimization

- [ ] Add authoritative citations where a claim needs one (house practice; the paper sets no count)
- [ ] Add real statistics, each with its source
- [ ] Add real expert quotes, each with attribution and a link
- [ ] Use confident, authoritative language
- [ ] Ensure content is accessible to general audience
- [ ] Include appropriate technical terminology
- [ ] Vary vocabulary throughout
- [ ] Improve overall fluency and readability
- [ ] Remove any keyword stuffing

### Structure Optimization

- [ ] Use "answer-first" format (direct answer at top)
- [ ] Clear H1 > H2 > H3 hierarchy
- [ ] Bullet points for lists
- [ ] Tables for comparisons
- [ ] Short, focused paragraphs (practice, not a Google requirement)
- [ ] Logical flow between sections

### Schema Optimization

- [ ] Q&A sections on the page for common questions (FAQPage markup gives no Google rich result since 7 May 2026)
- [ ] Add Article schema with author info
- [ ] Include datePublished and dateModified
- [ ] Do not add SpeakableSpecification for a Hebrew site (Google limits it to English-language news publishers in the US)

---

## Validation on Commercial Platforms

The researchers validated GEO methods on **Perplexity.ai**, a commercial generative engine:

The paper reports that on Perplexity.ai the best-performing methods improved on the baseline by 22% on Position-Adjusted Word Count and 37% on Subjective Impression, with Statistics Addition and Quotation Addition strongest. An earlier per-method table printed here did not match the paper and has been removed.

This shows the methods moved results on one commercial engine in 2023. It does not establish the same effect on today's engines or on Hebrew content.

---

## Future of GEO

The paper argues that GEO matters for:

1. **Content creators** - Maintain visibility in AI-dominated search
2. **Businesses** - Ensure brand presence in AI responses
3. **Publishers** - Adapt to the citation economy
4. **SEO professionals** - Evolve practices for generative search

Google's own view, for its AI features, is that this is still SEO; treat GEO as an extension of good SEO practice rather than a separate discipline.

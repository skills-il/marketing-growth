# AI/AEO Considerations

Answer Engine Optimization (AEO) prepares content to be selected as authoritative answers by AI systems like ChatGPT, Perplexity, Google AI Overviews, and Bing Copilot.

## How AI Selects Answers

No AI search vendor publishes its selection criteria. The list below is a practitioner working model, not a documented algorithm; use it to review content, not to promise outcomes:

1. **Clarity:** Is the answer direct and easy to extract?
2. **Authority:** Is the source trustworthy?
3. **Comprehensiveness:** Does it fully address the question?
4. **Recency:** Is the information up to date?
5. **Structure:** Can the AI parse and understand it?

## Content Structure for AI

### Direct Answers First
Lead with the answer, then explain.

**Bad:**
> The history of JavaScript dates back to 1995 when Brendan Eich... [500 words later] ...JavaScript runs in the browser.

**Good:**
> JavaScript is a programming language that runs in web browsers. It was created in 1995 by Brendan Eich...

### Clear Headings
Use descriptive H2/H3 headings that match user questions.

**Bad:** "Overview" → "Details" → "More Information"
**Good:** "What is X?" → "How does X work?" → "When should you use X?"

### Lists and Tables
AI extracts structured information more easily than prose.

```markdown
## Benefits of Structured Content

- **Reusability:** Use content across channels
- **Flexibility:** Change presentation without changing content
- **Scalability:** Manage large content volumes
```

### FAQ Format
Question-answer pairs on the page are easy to extract. (FAQPage markup no longer produces a Google rich result; the visible Q&A is what matters.)

```typescript
// Schema for AI-friendly FAQs
defineType({
  name: 'faq',
  type: 'document',
  fields: [
    defineField({ name: 'question', type: 'string' }),
    defineField({ name: 'answer', type: 'text' }),
    defineField({ name: 'category', type: 'reference', to: [{ type: 'faqCategory' }] }),
  ]
})
```

## Technical Implementation

### Structured Data (useful, not required)
Google's AI optimization guide says structured data "isn't required for generative AI search", while still recommending it for rich-result eligibility. Use the types Google still supports (Organization, LocalBusiness, Product, Article). The FAQ example below is valid schema.org but earns no Google rich result since 7 May 2026.

```typescript
// FAQ structured data
const faqSchema = {
  "@context": "https://schema.org",
  "@type": "FAQPage",
  mainEntity: faqs.map(faq => ({
    "@type": "Question",
    name: faq.question,
    acceptedAnswer: {
      "@type": "Answer",
      text: faq.answer
    }
  }))
}
```

### Canonical Content
Ensure AI finds your authoritative version, not copies.

- Set canonical URLs
- Avoid duplicate content across pages
- Use `rel="canonical"` for syndicated content

### Freshness Signals
Keep content genuinely current (practice; no vendor publishes a freshness threshold).

- Display publish and update dates prominently
- Update content regularly with substantive changes (superficial updates like changing dates without meaningful edits can be counterproductive)
- Use `dateModified` in structured data

## Content Quality Signals

### Author Credentials
Named, credentialed authors support E-E-A-T (practice; no AI vendor documents an author check).

- Display author name and credentials
- Link to author profiles
- Include author structured data

### Citations and Sources
Linking to authoritative sources increases trust.

- Cite primary sources
- Link to studies, documentation, official sources
- Avoid circular citations (sites citing each other)

### Comprehensive Coverage
Answer the question fully, including the adjacent sub-questions (Google documents query fan-out for AI Overviews and AI Mode).

- Cover related questions users might have
- Include definitions for technical terms
- Address common misconceptions

## Google AI Overviews and AI Mode

These are two distinct surfaces. AI Overviews appear inside ordinary results pages; AI Mode is a separate conversational experience, and Hebrew and Israel both appear on Google's AI Mode availability list. Google states there are no additional requirements or special optimizations needed to appear in either, so the entry ticket is ordinary indexable, helpful content rather than a new file format or markup.

- **Be the cited source:** both surfaces link out to specific pages. Concise, authoritative answers increase citation likelihood.
- **Structure for extraction:** Use clear headings, direct answers, and lists that AI can easily parse.
- **Cover follow-up questions:** both may use a "query fan-out" technique, issuing several related searches behind one user query. Answering the adjacent sub-questions on the same page is therefore a direct optimization, not a nice-to-have.
- **Monitor in Search Console:** Google launched dedicated Search Generative AI performance reports on 3 June 2026, covering AI Overviews, AI Mode, and generative AI in Discover. They expose **impressions, pages, countries, devices and dates only**. There is no click, CTR, position or query data in this version. The reports reached all websites as of 31 August 2026. Generative-AI activity also remains counted inside the overall performance report.

## AI Crawler Management

Make conscious decisions about which AI systems can crawl your content:

- **Separate training from search.** OpenAI and Anthropic both run distinct bots for each: `GPTBot` vs `OAI-SearchBot`, and `ClaudeBot` vs `Claude-SearchBot`. Allowing only the training crawler leaves you ineligible for search citations on that platform. This is the most common misconfiguration in the whole area.
- **Live fetchers are a third category:** `ChatGPT-User`, `Claude-User`, `Perplexity-User`. Perplexity documents that `Perplexity-User` generally ignores robots.txt because a human requested the fetch, and OpenAI says robots.txt rules "may not apply" to `ChatGPT-User`. Indexing for search is done by `PerplexityBot` and `OAI-SearchBot`, not by these fetchers.
- **`Google-Extended` is an opt-out token, not a crawler.** It governs Gemini training and grounding in Gemini Apps, and does not affect Google Search ranking or AI Overview citations.
- **Search generative AI control** (Search Console settings) is the switch for AI Overviews, AI Mode and Discover's generative features. A site must be included there to be eligible; it does not affect training.
- **Search-index crawlers beyond OpenAI and Anthropic:** `PerplexityBot`, and `MistralAI-Index` for Mistral search. See `platform-algorithms.md` for the full list.
- **Allowing crawlers** increases chances of being cited as a source in AI responses.
- Review your policy regularly. This is one of the most actively evolving areas of SEO.

## Measuring AEO Success

### Monitor AI Mentions
Track when AI assistants cite your content. Check crawler ACCESS before judging content quality: "not crawled yet" and "crawled but not chosen" look identical in the answer box and have opposite fixes.
- Use Search Console's generative AI reports for impressions (no click data in the current version)
- Monitor referral traffic from AI platforms (Perplexity, ChatGPT, Bing Copilot)
- Search for your brand + "according to" in AI assistants
- Consider third-party AEO tracking tools for comprehensive monitoring

### Track Zero-Click Queries
If AI answers questions directly, traditional rankings matter less.

### Featured Snippet Capture
Track which featured snippets you own; they are a classic-search win in their own right. No vendor documents that they feed AI answers.

## AEO vs SEO Balance

AEO and SEO largely align: quality content serves both. Key differences:

| Aspect | SEO Focus | AEO Focus |
|--------|-----------|-----------|
| Goal | Rank on page 1 | Be THE answer |
| Format | Varies | Direct, structured |
| Length | Often longer | Concise + comprehensive |
| Links | Link building | Source citations |

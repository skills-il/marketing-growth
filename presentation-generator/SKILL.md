---
name: presentation-generator
description: Generate RTL-first Hebrew presentations with full right-to-left support. Use when you need to create a business presentation, startup pitch deck, quarterly report, or educational slideshow in Hebrew. Produces slides with Hebrew fonts, right-aligned bullets, and bilingual support in a single deck. Prevents hours of manual formatting and RTL issues that other tools fail to solve. Do NOT use for non-Hebrew presentations, video creation, or interactive web slideshows.
license: MIT
---

## Overview

This skill generates Hebrew presentations with correct right-to-left (RTL) layout. It covers two practical output paths: Marp markdown for developers who want version-controlled, text-based slides, and python-pptx for anyone who needs a `.pptx` file compatible with PowerPoint and Google Slides.

Hebrew presentations have unique technical requirements that generic presentation tools ignore. Bullet alignment defaults to LTR. Punctuation jumps to the wrong end of a line. Number formatting in Israeli business contexts follows conventions that differ from what US-centric templates assume. This skill addresses all of those problems with working code and explicit configuration rather than workarounds.

## When to Use

- **Startup pitch deck**: Building a deck for Israeli VCs or accelerators (YotaVC, Grove, Pitango, OurCrowd) where the primary language is Hebrew.
- **Quarterly business report**: Presenting KPIs, P&L, or operational metrics in Hebrew with NIS figures and Israeli fiscal calendar.
- **Marketing campaign deck**: Internal or client-facing decks for campaigns, product launches, or brand presentations in Hebrew.
- **Educational slides**: University lectures, school materials, training sessions, or workshops delivered in Hebrew.
- **Bilingual investor materials**: Decks that mix Hebrew narrative with English technical details or financial tables.

Do not use this skill for fully English presentations (use standard Marp or PowerPoint templates), video export, or interactive web-based slideshows (use Reveal.js separately).

## Quick Start

Ask your AI agent:

```
Create a 10-slide startup pitch deck in Hebrew for a B2B SaaS company in the legal-tech space.
Include: problem, solution, product demo, market size, business model, traction, team, and ask.
Use Marp format with RTL Hebrew layout.
```

Or for a PPTX file:

```
Create a quarterly business report presentation in Hebrew (12 slides) as a .pptx file.
Include NIS financial figures, charts placeholders, and Hebrew section headers.
```

## Slide Generation Approaches

### Marp (Markdown Presentations)

Marp converts Markdown into slides. It is developer-friendly, version-controllable, and outputs PDF, HTML, or PPTX. RTL support is implemented via CSS directives embedded in the Marp theme.

Marp does not have native RTL support at the engine level. RTL is achieved by setting `direction: rtl` and `text-align: right` in the theme CSS, and using a Hebrew-capable font. This is a CSS-level workaround, but it is robust and widely used.

Install Marp CLI:
```bash
npm install -g @marp-team/marp-cli
```

Basic Marp file structure with RTL:
```markdown
---
marp: true
theme: rtl-hebrew
lang: he
dir: rtl
---

<!-- _class: title -->
# כותרת המצגת
## כותרת משנה

---

# שקף ראשון

- נקודה ראשונה
- נקודה שנייה
- נקודה שלישית
```

Export commands:
```bash
marp presentation.md --pdf          # Export to PDF
marp presentation.md --html         # Export to HTML
marp presentation.md --pptx         # Export to PPTX (requires Chromium)
```

### python-pptx (Native PPTX)

python-pptx creates `.pptx` files directly. RTL support requires XML-level patches because python-pptx's Python API does not expose the RTL paragraph attribute. You must inject `<a:rtl val="1"/>` into each paragraph element after adding text.

Install:
```bash
pip install python-pptx
```

See `scripts/create-presentation.py` for a complete working example with all RTL patches applied.

### Google Slides API

For Google Slides output, use the Slides API with `WritingDirection: RIGHT_TO_LEFT` on text runs. This is more involved and requires OAuth; use python-pptx and import into Google Slides when a programmatic Google Slides workflow is not strictly necessary.

## Hebrew RTL Configuration

### Marp CSS Theme

Save as `themes/rtl-hebrew.css` and reference it in your Marp config:

```css
/* themes/rtl-hebrew.css */
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

section {
  direction: rtl;
  text-align: right;
  font-family: 'Heebo', 'David Libre', Arial, sans-serif;
  font-size: 28px;
  background: #ffffff;
  color: #1a1a2e;
  padding: 60px 80px;
}

h1, h2, h3 {
  text-align: right;
  direction: rtl;
  font-weight: 700;
}

ul, ol {
  direction: rtl;
  text-align: right;
  padding-right: 1.5em;
  padding-left: 0;
}

/* Reverse list marker position for RTL */
ul li::marker,
ol li::marker {
  unicode-bidi: plaintext;
}

/* Override for LTR content blocks (English code, URLs) */
.ltr {
  direction: ltr;
  text-align: left;
  font-family: 'Courier New', monospace;
}
```

Reference in `.marprc.yml`:
```yaml
theme: ./themes/rtl-hebrew.css
html: true
```

### python-pptx XML Patches

python-pptx exposes the `paragraph.alignment` property but not the `rtl` XML attribute. The patch inserts the XML node directly:

```python
from pptx.oxml.ns import qn
from lxml import etree

def set_paragraph_rtl(paragraph):
    """Inject <a:rtl val="1"/> into a paragraph's pPr element."""
    pPr = paragraph._p.get_or_add_pPr()
    rtl_elem = pPr.find(qn('a:rtl'))
    if rtl_elem is None:
        rtl_elem = etree.SubElement(pPr, qn('a:rtl'))
    rtl_elem.set('val', '1')
```

Call this on every paragraph that contains Hebrew text. See `references/pptx-rtl-patches.md` for the full patch set including table cells and text frames.

### Font Recommendations

| Font | Style | Notes |
|------|-------|-------|
| Heebo | Clean, modern sans-serif | Best for business/tech decks. Available on Google Fonts. |
| David Libre | Classic serif | Formal reports, legal documents. Available on Google Fonts. |
| Assistant | Rounded, approachable | Education, consumer-facing decks. Available on Google Fonts. |
| Rubik | Geometric, strong | Startup decks, bold headers. Available on Google Fonts. |

For Marp, load fonts via `@import url(...)` in the theme CSS. For python-pptx, fonts must be installed on the system running the script, or embedded in the PPTX by specifying the font name in text run properties.

## Israeli Presentation Conventions

### Startup Pitch Deck Structure (Israeli VC Format)

Israeli VCs expect a specific ordering that differs from Silicon Valley conventions. The emphasis is on technical proof early, team credibility through military/academic context, and dual-market sizing.

Recommended 10-slide structure:
1. **כותרת וסלוגן** (Title + tagline): One sentence, no fluff.
2. **הבעיה** (Problem): Specific, quantified. Name Israeli companies or regulations affected if relevant.
3. **הפתרון** (Solution): Product screenshot or diagram on first presentation, not slide 5.
4. **הדגמה / פרודקט** (Demo/Product): Actual UI or architecture diagram. Investors expect proof early.
5. **גודל שוק** (Market Size): TAM/SAM/SOM. Show Israel TAM separately from global. Use NIS for local figures, USD for global.
6. **מודל עסקי** (Business Model): Pricing in NIS (Israeli market) and USD (export). ARR, not MRR, for B2B.
7. **מנוע צמיחה** (Growth): GTM for Israel first, then EMEA. Israeli reference customers carry disproportionate weight.
8. **טרקשן** (Traction): Numbers. Revenue, pilot customers, LOIs. Israeli VCs weight signed agreements heavily.
9. **צוות** (Team): Military unit context (8200, Mamram, Shaldag) and academic credentials (Technion, TAU, Hebrew University) are standard and expected.
10. **הבקשה** (The Ask): Amount in USD. Round in NIS equivalent at current rate is a nice touch for local VCs.

### NIS Currency Formatting

Use the shekel sign with no space before the number: `₪1,234,567`

For thousands: Israeli convention in formal documents uses comma as the thousands separator (matching international financial standards), not period. `₪1,234,567.89` is correct. `₪1.234.567,89` is German-style and incorrect for Israeli business documents.

In mixed Hebrew/English documents, place the ₪ symbol before the number even in RTL text (the symbol itself is LTR). Use Unicode bidirectional control characters if the rendering engine displaces it: `\u200e` (LRM) before the currency symbol forces correct placement.

### Israeli Fiscal Year

Israel's fiscal year runs January to December (same as calendar year), unlike the UK or US government fiscal years. Quarterly reports use Q1-Q4 with the following Hebrew labels:
- Q1: רבעון ראשון (ינואר-מרץ)
- Q2: רבעון שני (אפריל-יוני)
- Q3: רבעון שלישי (יולי-ספטמבר)
- Q4: רבעון רביעי (אוקטובר-דצמבר)

### Hebrew Date Format

Standard Israeli date format: `DD/MM/YYYY` or `DD בחודש YYYY`. For slide footers, `מרץ 2026` is cleaner than `03/2026`.

### Education Slides

For educational content, bullet formatting differs from business:
- Use `•` (U+2022) rather than `-` for bullet markers. They render more reliably in RTL.
- Numbered lists in Hebrew run right to left but numbers are still Arabic numerals (1, 2, 3), not Hebrew letters, in most modern contexts.
- Avoid putting English terms in parentheses after Hebrew terms in body text. Put them in footnotes or a separate glossary slide.

## Bilingual Slides

### Mixing Hebrew and English

When a single slide needs both Hebrew and English (common in tech decks where code, API names, or English product names appear):

In Marp, wrap LTR blocks in a `<div>` with inline style:
```markdown
# כותרת בעברית

- נקודה עברית ראשונה
- שימוש ב-<span style="direction:ltr;display:inline-block">API endpoint: /v1/users</span>

<div style="direction:ltr; text-align:left; font-family: monospace">

```python
response = client.get("/v1/users")
```

</div>
```

In python-pptx, set separate runs within the same paragraph, applying RTL to Hebrew runs and LTR to English runs:
```python
from pptx.util import Pt
from pptx.oxml.ns import qn
from lxml import etree

def add_mixed_paragraph(text_frame, hebrew_text, english_term):
    para = text_frame.add_paragraph()
    set_paragraph_rtl(para)  # RTL for the whole paragraph

    # Hebrew run
    run_he = para.add_run()
    run_he.text = hebrew_text
    run_he.font.name = 'Heebo'

    # English term run (LTR within RTL paragraph)
    run_en = para.add_run()
    run_en.text = f' {english_term}'
    run_en.font.name = 'Calibri'
    # Bidi override for inline LTR in RTL paragraph
    rPr = run_en._r.get_or_add_rPr()
    rtl_attr = rPr.find(qn('a:rtl'))
    if rtl_attr is None:
        rtl_attr = etree.SubElement(rPr, qn('a:rtl'))
    rtl_attr.set('val', '0')
```

### Title Slides with Both Languages

A common Israeli business pattern: Hebrew title on line one, English subtitle on line two. Both are handled correctly if you set the text frame to RTL and override alignment for the English line.

## Gotchas

**1. Hebrew punctuation displacement in PPTX exports**

When exporting to PPTX from tools that do not set RTL at the XML level, periods and commas jump to the opposite end of the line. A sentence like `הפתרון שלנו.` renders as `.הפתרון שלנו` visually. The fix is `<a:rtl val="1"/>` on every paragraph element in the XML, not just at the text-frame level. The text-frame-level `txBody` attribute is insufficient; each `<a:pPr>` needs it.

**2. Default bullet alignment is LTR**

Both Marp (without custom CSS) and python-pptx (without XML patches) default all bullet lists to LTR. You will see bullets flush to the left margin with text flowing left-to-right. This is the single most common Hebrew presentation bug. It must be overridden explicitly: CSS `direction: rtl; text-align: right` for Marp, and the `a:rtl` paragraph attribute for PPTX. There is no global toggle in either tool.

**3. Number formatting ambiguity**

Israeli convention uses comma as the thousands separator for financial figures (matching the English-language standard). However, some Israeli government and academic documents use a period for thousands. Before generating slides with large numbers, confirm which convention the audience expects. For business and VC presentations, always use comma: `₪1,234,567`. For government reports, ask explicitly.

**4. Font fallback silently degrades quality**

If Heebo or David Libre are not installed on the rendering machine, Marp and PPTX viewers fall back to Arial or Times New Roman. Both support Hebrew but are visually inferior and may have different line-height metrics that break slide layouts. Always verify font availability before presenting. For Marp PDF export, fonts are embedded via Chromium, so the export is safe. For PPTX shared to other machines, embed fonts via File > Options > Save > Embed fonts in the file (PowerPoint). python-pptx 1.0.x does not expose a high-level `EmbedTrueTypeFonts` property; embedding via the library still requires direct XML edits to the .pptx package.

**5. Mixed-direction tables flip column order**

In RTL mode, table columns are displayed right to left. A table with columns [Date, Revenue, Growth] in a LTR Python array will render as [Growth, Revenue, Date] visually on an RTL slide. You must reverse the column order in your data structure before populating the table, so the visual left-to-right order matches what the reader expects. This is counterintuitive: in RTL, column index 0 is the rightmost column visually.

## Output Formats

| Tool | Input | Output formats | RTL quality |
|------|-------|---------------|-------------|
| Marp CLI | `.md` | PDF, HTML, PPTX | Good (CSS-level) |
| python-pptx | Python script | `.pptx` | Excellent (XML-level) |
| Google Slides API | API calls | Google Slides, PDF | Good (WritingDirection property) |
| LibreOffice Impress | `.odp` / `.pptx` | PDF, PPTX | Partial (varies by version) |

For maximum compatibility with Israeli business recipients (who almost universally use Windows + PowerPoint or Google Slides), prefer python-pptx output. Marp PDF export is best for read-only sharing (email attachments, pitch email).


## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| pptxgenjs (JavaScript PPTX generator) | https://gitbrent.github.io/PptxGenJS/ | Node.js library for creating PowerPoint files, RTL support |
| python-pptx | https://python-pptx.readthedocs.io/en/latest/ | Python library for PowerPoint generation, shape and text API |
| Reveal.js | https://revealjs.com | HTML-based presentations, keyboard shortcuts, RTL layouts |
| Marp (Markdown presentations) | https://marp.app | Markdown-to-slides CLI, themes, PDF export |
| Google Slides API | https://developers.google.com/slides/api | Slides REST API, batchUpdate, placeholders, text direction |

## Troubleshooting

**Text appears mirrored or reversed**: The font is rendering but direction is not set. Add `dir="rtl"` to the HTML element (Marp HTML export) or verify `<a:rtl val="1"/>` is present on each `<a:pPr>` in the PPTX XML.

**Bullet markers appear on the wrong side**: CSS `list-style-position: inside` combined with `direction: rtl` fixes Marp. For PPTX, the bullet marker follows paragraph direction, so setting paragraph RTL is sufficient.

**Mixed Hebrew/English line breaks poorly**: Long English words in RTL paragraphs can cause unusual line breaks. Use `word-break: break-word` in Marp CSS, or break long English strings manually in PPTX.

**Exported PDF has blank slides**: Marp PDF requires Chromium. Run `marp --allow-local-files presentation.md --pdf` if fonts are local. Check `marp --version` confirms Chromium is bundled.

**PPTX opens with font substitution warning**: The Hebrew font named in the PPTX is not installed on the recipient's machine. Either embed fonts or instruct recipients to install Heebo from Google Fonts before opening.

**Currency symbol renders on wrong side**: Insert `\u200e` (Left-to-Right Mark) immediately before `₪` in Hebrew text to anchor it correctly in the bidi algorithm.

## References

- [Marp documentation](https://marp.app/)
- [python-pptx documentation](https://python-pptx.readthedocs.io/)
- [Unicode Bidirectional Algorithm (UAX #9)](https://unicode.org/reports/tr9/)
- [Google Fonts: Heebo](https://fonts.google.com/specimen/Heebo)
- [Google Fonts: David Libre](https://fonts.google.com/specimen/David+Libre)
- [OOXML spec (ECMA-376)](https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/)
- `references/marp-rtl-guide.md` in this skill folder
- `references/pptx-rtl-patches.md` in this skill folder

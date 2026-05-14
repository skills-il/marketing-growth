---
name: presentation-generator
description: Generate RTL-first Hebrew presentations with full right-to-left support. Use when you need to create a business presentation, startup pitch deck, quarterly report, or educational slideshow in Hebrew. Produces slides with Hebrew fonts, right-aligned bullets, and bilingual support in a single deck. Prevents hours of manual formatting and RTL issues that other tools fail to solve. Do NOT use for non-Hebrew presentations, video creation, or interactive web slideshows.
license: MIT
---

## Overview

This skill generates Hebrew presentations with correct right-to-left (RTL) layout. It covers two practical output paths: Marp markdown for developers who want version-controlled, text-based slides, and python-pptx for anyone who needs a `.pptx` file compatible with PowerPoint and Google Slides.

Hebrew presentations have unique technical requirements that generic presentation tools ignore. Bullet alignment defaults to LTR. Punctuation jumps to the wrong end of a line. Number formatting in Israeli business contexts follows conventions that differ from what US-centric templates assume. This skill addresses all of those problems with working code and explicit configuration rather than workarounds.

## Instructions

Follow these steps to produce a correct RTL Hebrew deck:

1. **Choose the output path**: Marp markdown for version-controlled, text-based slides, or python-pptx for a `.pptx` file that opens cleanly in PowerPoint and Google Slides. For Israeli business recipients, prefer python-pptx (XML-level RTL is reliable); use Marp PDF for read-only sharing.
2. **Pick the font**: Heebo for business and tech decks, David Libre for formal reports, Assistant for education, Rubik for bold startup decks. Load via `@import` in Marp CSS, or ensure the font is installed on the machine running python-pptx.
3. **Generate the content**: write the slide text in Hebrew. Structure pitch decks per the Israeli VC ordering below; use NIS formatting and the Israeli fiscal calendar.
4. **Apply the RTL patches**: for Marp, set `direction: rtl; text-align: right` in the theme CSS. For python-pptx, call `set_paragraph_rtl()` on every paragraph that holds Hebrew text, plus the table-cell and run-level helpers in `references/pptx-rtl-patches.md`. For charts, speaker notes, and the slide master, see the dedicated sections below.
5. **Export**: run `marp presentation.md --pptx` (or `--pdf`/`--html`), or `prs.save(output_path)` in python-pptx.
6. **Verify**: open the file and confirm bullets align right, punctuation sits at the correct end of each line, the currency symbol is placed correctly, and tables read right-to-left. Inspect the XML if a paragraph still renders LTR (each `<a:pPr>` must contain `<a:rtl val="1"/>`).

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

## Native Charts in python-pptx

Quarterly reports and pitch decks need real charts, not image placeholders. python-pptx creates native, editable PowerPoint charts via `slide.shapes.add_chart`. The chart object stays editable in PowerPoint, which Israeli recipients expect.

```python
from pptx.chart.data import CategoryChartData
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION
from pptx.util import Inches, Pt

def add_revenue_chart(slide):
    chart_data = CategoryChartData()
    # Category labels are Hebrew. Reverse the order so the axis reads
    # right-to-left visually (Q1 on the right, Q4 on the left).
    chart_data.categories = ['רבעון 4', 'רבעון 3', 'רבעון 2', 'רבעון 1']
    chart_data.add_series('הכנסות (מיליוני ש"ח)', (4.8, 3.9, 3.1, 2.4))

    graphic_frame = slide.shapes.add_chart(
        XL_CHART_TYPE.COLUMN_CLUSTERED,
        Inches(0.6), Inches(1.6), Inches(8.8), Inches(4.0),
        chart_data,
    )
    chart = graphic_frame.chart
    chart.has_legend = True
    chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    chart.legend.include_in_layout = False

    # Set the category axis font to a Hebrew font so the labels render.
    category_axis = chart.category_axis
    category_axis.tick_labels.font.name = 'Heebo'
    category_axis.tick_labels.font.size = Pt(12)
    chart.value_axis.tick_labels.font.name = 'Heebo'
    return chart
```

### Hebrew Chart Quirks

- **Category-axis labels**: python-pptx does not expose an RTL toggle for the chart plot area. Reverse the `categories` list so the visual left-to-right order matches the reader's right-to-left expectation (the first item appears on the right of the axis). This mirrors the table column-order rule.
- **Hebrew labels need a Hebrew font**: set `chart.category_axis.tick_labels.font.name` and `chart.value_axis.tick_labels.font.name` explicitly. The chart does not inherit the slide theme font, and the default falls back to a non-Hebrew face that renders boxes.
- **Series names**: a Hebrew series name in the legend renders correctly with a Hebrew font set, but mixed Hebrew/Latin series names (for example `הכנסות ARR`) can show the Latin token displaced. Keep series names in one script where possible.
- **Useful `XL_CHART_TYPE` values**: `COLUMN_CLUSTERED` and `BAR_CLUSTERED` for comparisons (bar charts read naturally in RTL since the bars grow from the right baseline if you reverse categories), `LINE` for trends, `PIE` and `DOUGHNUT` for share-of-total. For a KPI grid, several small `COLUMN_CLUSTERED` charts read better than one dense chart.
- **Number formatting**: set `chart.value_axis.tick_labels.number_format` to a NIS-aware format string (for example `'₪#,##0'`) and `number_format_is_linked = False` so the comma thousands separator shows.

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

### Mixed Hebrew and Latin Inside a Single Word or Tight Token

The paragraph-level and run-level direction overrides above handle Hebrew sentences with separate English words. The harder, and far more common, real-world bug is a single token that mixes scripts with no whitespace boundary: `B2B-חברות`, `חברת-SaaS`, a version string like `גרסה-2.0`, or a hashtag like `#עברית2026`. The bidi algorithm reorders the run at every script boundary inside the token, so `B2B-חברות` can display as `חברות-B2B` even though it is one visual word.

This happens because a run break is a *direction* boundary, not a *word* boundary. Splitting `B2B-חברות` into an LTR run and an RTL run lets the bidi algorithm place each run independently, and the hyphen (a neutral character) attaches to whichever side the algorithm prefers, not where you typed it.

Fixes, in order of reliability:

1. **Anchor neutrals with bidi marks**. Wrap the Latin fragment in directional isolates so it cannot leak into the surrounding Hebrew: `⁦` (LRI, Left-to-Right Isolate) before and `⁩` (PDI, Pop Directional Isolate) after. For a single Latin run inside an RTL paragraph, `‎` (LRM) immediately after the Latin fragment pins the trailing neutral. Example: `f'⁦B2B⁩-חברות'`.
2. **Keep the whole token in one run** with the paragraph direction set correctly, and let the marks above do the ordering, rather than splitting at the script change. One run with embedded isolates reorders predictably; two runs do not.
3. **For version strings and identifiers**, treat the entire token as LTR: put `‎` before it and `‏` (RLM) after it so it sits as an LTR island inside the RTL line. `‏‎Ver 2.0‏` keeps `Ver 2.0` intact and correctly placed.

```python
def add_intratoken_run(paragraph, hebrew_part, latin_part, sep='-'):
    """Add a token like 'B2B-חברות' with the Latin fragment bidi-isolated.

    Embeds LRI/PDI around the Latin fragment so the script boundary
    does not let the bidi algorithm reorder the token.
    """
    run = paragraph.add_run()
    # ⁦ = LRI, ⁩ = PDI. The separator stays on the Hebrew side.
    run.text = f'⁦{latin_part}⁩{sep}{hebrew_part}'
    run.font.name = 'Heebo'
    return run
```

In Marp, wrap the Latin fragment in `<span dir="ltr">` (requires `html: true`), or use the same `⁦`/`⁩` characters directly in the Markdown. CSS `unicode-bidi: isolate` on an inline span achieves the same effect without literal control characters.

### Speaker Notes, Slide Master, and Image Placement

- **Speaker notes RTL**: notes have their own text frame, reached via `slide.notes_slide.notes_text_frame`. They are not patched by slide-body RTL helpers. Call `set_text_frame_rtl(slide.notes_slide.notes_text_frame)` after writing notes, or Hebrew notes render LTR in the presenter view.
- **Slide master and layout defaults**: setting RTL on each paragraph is reliable but repetitive. To make RTL the default for a layout, patch the `<a:lstStyle>` (list style) inside the placeholder's `<p:txBody>` on the slide layout (`prs.slide_layouts[i]`) or slide master (`prs.slide_masters[0]`), adding `<a:rtl val="1"/>` to each level's `<a:defRPr>`/`<a:lvlNpPr>`. New placeholders that inherit from that layout then start RTL. This does not retroactively fix existing slides; it only changes the default for placeholders created afterward.
- **Image and logo placement in RTL**: `add_picture` positions images by absolute EMU coordinates, so RTL does not move them automatically. By Israeli convention, the company logo sits in the top-right corner (the start of the reading flow). Compute the right-edge position as `prs.slide_width - Inches(logo_width) - Inches(margin)` rather than hardcoding a left offset, so the logo stays anchored to the visual start of the slide regardless of slide width.

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

## Examples

### Example 1: Startup Pitch Deck with python-pptx

Input: "Create a 5-slide Hebrew pitch deck for a B2B SaaS legal-tech company. Include title, problem, solution, technical integration, and a Q1 metrics table. Output a .pptx file."

Process:
1. Choose python-pptx (recipient is an Israeli VC who will open it in PowerPoint).
2. Pick Heebo (business/tech deck).
3. Write Hebrew content per the Israeli VC 10-slide ordering, trimmed to 5 slides.
4. Build each slide with `scripts/create-presentation.py` patterns: `set_paragraph_rtl()` on every title and bullet, `add_english_run()` for inline Latin product names, an RTL table with reversed column order for the metrics slide.
5. Export via `prs.save('pitch-deck.pptx')`.
6. Open in PowerPoint, confirm bullets align right, `₪3.4M` shows the symbol on the correct side, and the table reads right-to-left.

Output: a `.pptx` where slide 2 ("הבעיה") shows four right-aligned Hebrew bullets, slide 4 mixes `הפלטפורמה שלנו מתחברת ישירות ל-Salesforce CRM` with the Latin product name as an LTR island, and slide 5 renders a metrics table with `מדד` as the rightmost column. Running `python scripts/create-presentation.py --output pitch-deck.pptx --title "שם החברה"` produces exactly this deck.

### Example 2: Quarterly Report with a Native Chart in Marp

Input: "Build a Hebrew quarterly business report. Slide 1 is a title, slide 2 shows Q1-Q4 revenue as a chart, slide 3 is a financial table. Marp format, export to PDF."

Process:
1. Choose Marp (text-based, version-controlled, PDF export for email distribution).
2. Pick Heebo, loaded via `@import` in `themes/rtl-hebrew.css`.
3. Write the deck markdown with `marp: true`, `theme: rtl-hebrew`, `dir: rtl`, `lang: he`.
4. Apply RTL via the theme CSS (`direction: rtl; text-align: right`). For the revenue chart, Marp has no native chart engine, so either embed a pre-rendered chart image or generate the chart slide with python-pptx and the `add_revenue_chart` pattern, then merge. Write the financial table with columns in right-to-left visual order in the Markdown source.
5. Export via `marp report.md --pdf --allow-local-files -o report.pdf`.
6. Open the PDF, confirm Hebrew renders with Heebo (fonts embed via Chromium), bullets and table columns flow right-to-left, and no slides are blank.

Output: a 3-slide PDF where the title slide is right-aligned, the revenue slide shows רבעון 1 through רבעון 4 with the first quarter on the right, and the financial table reads `מדד | ממוצע ענף | החברה שלנו | שינוי` from right to left.

## Bundled Resources

- `scripts/create-presentation.py` - Working python-pptx script that builds a complete 5-slide RTL Hebrew pitch deck (title, problem, solution, mixed-language technical slide, financial table). All RTL XML patches are applied. Run `python scripts/create-presentation.py --output deck.pptx --title "שם החברה"`. Use it as the canonical reference for the patch functions.
- `references/marp-rtl-guide.md` - Marp RTL configuration quick reference: minimum viable theme, project config, slide templates (title, content, two-column, code block, financial table), export commands, font loading options, a full business-grade theme, and known limitations.
- `references/pptx-rtl-patches.md` - The complete python-pptx RTL patch set: paragraph, text-frame, run-level, table-cell, and table patches, the full slide-building pattern, reversed-column table helper, font embedding, and XML debugging snippets.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| python-pptx | https://python-pptx.readthedocs.io/en/latest/ | Python library for PowerPoint generation, shape, text, and chart API |
| Marp | https://marp.app | Markdown-to-slides CLI, themes, PDF/HTML/PPTX export |
| pptxgenjs (JavaScript PPTX generator) | https://gitbrent.github.io/PptxGenJS/ | Node.js library for creating PowerPoint files, RTL support |
| Reveal.js | https://revealjs.com | HTML-based presentations, keyboard shortcuts, RTL layouts |
| Google Slides API | https://developers.google.com/slides/api | Slides REST API, batchUpdate, placeholders, text direction |
| Unicode Bidirectional Algorithm (UAX #9) | https://unicode.org/reports/tr9/ | Bidi reordering rules, isolates (LRI/PDI), directional marks |
| Google Fonts: Heebo | https://fonts.google.com/specimen/Heebo | Hebrew sans-serif, weights, download for local embedding |
| OOXML spec (ECMA-376) | https://learn.microsoft.com/en-us/openspecs/office_standards/ms-oe376/ | Office Open XML text and paragraph property elements |

## Troubleshooting

**Text appears mirrored or reversed**: The font is rendering but direction is not set. Add `dir="rtl"` to the HTML element (Marp HTML export) or verify `<a:rtl val="1"/>` is present on each `<a:pPr>` in the PPTX XML.

**Bullet markers appear on the wrong side**: CSS `list-style-position: inside` combined with `direction: rtl` fixes Marp. For PPTX, the bullet marker follows paragraph direction, so setting paragraph RTL is sufficient.

**Mixed Hebrew/English line breaks poorly**: Long English words in RTL paragraphs can cause unusual line breaks. Use `word-break: break-word` in Marp CSS, or break long English strings manually in PPTX.

**Exported PDF has blank slides**: Marp PDF requires Chromium. Run `marp --allow-local-files presentation.md --pdf` if fonts are local. Check `marp --version` confirms Chromium is bundled.

**PPTX opens with font substitution warning**: The Hebrew font named in the PPTX is not installed on the recipient's machine. Either embed fonts or instruct recipients to install Heebo from Google Fonts before opening.

**Currency symbol renders on wrong side**: Insert `\u200e` (Left-to-Right Mark) immediately before `₪` in Hebrew text to anchor it correctly in the bidi algorithm.

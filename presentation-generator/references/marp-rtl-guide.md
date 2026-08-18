# Marp RTL Configuration Quick Reference

Marp does not ship with native RTL support. RTL is achieved entirely through CSS applied in a custom theme. This guide covers the minimum viable configuration and the most important edge cases.

## Minimum Viable RTL Theme

```css
/* themes/rtl-hebrew.css */
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&display=swap');

section {
  direction: rtl;
  text-align: right;
  font-family: 'Heebo', Arial, sans-serif;
  font-size: 28px;
  padding: 60px 80px;
}

h1, h2, h3 {
  direction: rtl;
  text-align: right;
}

ul, ol {
  direction: rtl;
  text-align: right;
  /* Push list markers to the right side */
  padding-right: 1.4em;
  padding-left: 0;
  margin-right: 0;
}
```

## Project Configuration

`.marprc.yml` at your project root:

```yaml
theme: ./themes/rtl-hebrew.css
html: true            # required for inline <div>/<span> direction overrides
allowLocalFiles: true # required if loading fonts from disk rather than CDN
```

## Front Matter Per Slide Deck

```yaml
---
marp: true
theme: rtl-hebrew
lang: he
dir: rtl
paginate: true
footer: 'Company Name | March 2026'
---
```

The `lang: he` and `dir: rtl` attributes appear in the exported HTML `<section>` elements. They are informational for screen readers but do not replace the CSS `direction` rule.

## Slide Templates

### Title Slide

```markdown
---
marp: true
theme: rtl-hebrew
---

<!-- _class: title -->

# כותרת המצגת הראשית

## כותרת משנה

**שם מציג | תאריך**
```

### Content Slide with Bullets

```markdown
---

# נושא השקף

- נקודה ראשונה עם פרט
- נקודה שנייה עם פרט
- נקודה שלישית עם פרט

> ציטוט מודגש אם צריך
```

### Two-Column Layout (Hebrew + English)

```markdown
---

# שקף דו-עמודי

<div style="display:grid; grid-template-columns:1fr 1fr; gap:40px;">

<div>

## עמודה ימנית (עברית)

- נקודה עברית
- נקודה שנייה

</div>

<div style="direction:ltr; text-align:left;">

## Left Column (English)

- English point
- Second point

</div>

</div>
```

### Slide with Code Block (LTR Override)

```markdown
---

# דוגמת קוד

ניתן לקרוא לנקודת הקצה הבאה:

<div style="direction:ltr; text-align:left; margin-top:20px;">

```python
import requests
response = requests.get("https://api.example.com/v1/data")
```

</div>
```

### Financial Table (RTL)

```markdown
---

# תוצאות כספיות - רבעון ראשון 2026

| מדד | ממוצע ענף | החברה שלנו | שינוי |
|-----|-----------|------------|-------|
| הכנסות | ₪2.1M | ₪3.4M | +62% |
| שולי גולמי | 68% | 74% | +6pp |
| לקוחות חדשים | 12 | 19 | +58% |

<!-- Table direction in Marp follows the section direction.
     Column order in the Markdown source is right-to-left in the visual output. -->
```

## Export Commands

```bash
# PDF (embeds fonts via Chromium -- safest for sharing)
marp presentation.md --pdf --allow-local-files -o output.pdf

# HTML (self-contained, opens in browser)
marp presentation.md --html --allow-local-files -o output.html

# PPTX (default: each slide is a raster IMAGE, so RTL looks correct but text is not editable)
marp presentation.md --pptx --allow-local-files -o output.pptx

# PPTX with editable text (Marp CLI 4.1.0+, experimental, routes through LibreOffice Impress).
# Text becomes editable, but RTL fidelity then depends on LibreOffice (can revert bullets to LTR).
marp presentation.md --pptx --pptx-editable --allow-local-files -o output.pptx
```

Note on the browser binary: Marp CLI 4.0+ exposes first-class `--browser`, `--browser-path`, and `--browser-protocol` flags (it also supports Firefox via WebDriver BiDi). On CI or restricted environments prefer `--browser-path /path/to/chromium` (or `--browser auto`) over the older `PUPPETEER_EXECUTABLE_PATH` env var, which is still honored but is the legacy knob.

## Font Loading Options

### Option 1: Google Fonts CDN (requires internet at render time)

```css
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;700&family=Rubik:wght@400;700&display=swap');
```

### Option 2: Local font files (reliable, works offline)

```css
@font-face {
  font-family: 'Heebo';
  src: url('./fonts/Heebo-Regular.woff2') format('woff2');
  font-weight: 400;
}
@font-face {
  font-family: 'Heebo';
  src: url('./fonts/Heebo-Bold.woff2') format('woff2');
  font-weight: 700;
}
```

Download Heebo WOFF2 files from Google Fonts or use `google-webfonts-helper.herokuapp.com`.

## Full Theme with Color Scheme

A complete business-grade theme for startup pitch decks:

```css
/* themes/startup-rtl.css */
@import url('https://fonts.googleapis.com/css2?family=Heebo:wght@300;400;600;700;900&display=swap');

:root {
  --primary: #1a1a2e;
  --accent: #4361ee;
  --light-bg: #f8f9fa;
  --text-muted: #6c757d;
}

section {
  direction: rtl;
  text-align: right;
  font-family: 'Heebo', sans-serif;
  font-size: 26px;
  background: white;
  color: var(--primary);
  padding: 50px 80px;
}

section.title {
  background: var(--primary);
  color: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-end;
}

h1 {
  font-size: 2.2em;
  font-weight: 900;
  color: var(--accent);
  border-bottom: 3px solid var(--accent);
  padding-bottom: 12px;
  margin-bottom: 30px;
}

h2 { font-size: 1.5em; font-weight: 600; }

ul { padding-right: 1.4em; padding-left: 0; }
ul li { margin-bottom: 12px; }

/* Page number */
section::after {
  color: var(--text-muted);
  font-size: 0.7em;
}

/* Footer */
footer {
  direction: rtl;
  text-align: right;
  font-size: 0.65em;
  color: var(--text-muted);
}

/* Highlight box */
blockquote {
  background: var(--light-bg);
  border-right: 4px solid var(--accent);
  border-left: none;
  padding: 16px 20px;
  margin: 20px 0;
  border-radius: 4px;
}
```

## Known Limitations

- **PPTX RTL fidelity**: by default Marp's `--pptx` export renders each slide as a raster IMAGE, so the RTL layout is baked in visually (it looks correct) but the text is not editable and carries no `rtl` paragraph attribute. With `--pptx-editable` (Marp CLI 4.1.0+, experimental, via LibreOffice Impress) you get editable text, but RTL fidelity then depends on LibreOffice and bullet alignment can revert to LTR. For an editable PPTX with guaranteed RTL, generate it with python-pptx directly (set the `rtl="1"` attribute on each `<a:pPr>`).
- **Table column order**: Marp renders tables with column order matching the Markdown source, rendered visually left-to-right even in RTL mode. Write table columns in the order you want them to appear visually from right to left.
- **Chromium required for PDF/PPTX**: Marp bundles a Chromium instance. On CI or restricted environments, point Marp at a system browser with `--browser-path /path/to/chromium` (or `--browser auto`), the documented Marp CLI 4.0+ flags; the older `PUPPETEER_EXECUTABLE_PATH` env var still works but is the legacy fallback.

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

# PPTX (requires Chromium; RTL may need post-processing in PowerPoint)
marp presentation.md --pptx --allow-local-files -o output.pptx
```

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

- **PPTX RTL fidelity**: Marp's PPTX export does not inject `<a:rtl val="1"/>` XML attributes. The exported PPTX will display Hebrew text but bullet alignment may revert to LTR when opened in PowerPoint. For PPTX with guaranteed RTL, use python-pptx directly.
- **Table column order**: Marp renders tables with column order matching the Markdown source, rendered visually left-to-right even in RTL mode. Write table columns in the order you want them to appear visually from right to left.
- **Chromium required for PDF/PPTX**: Marp bundles a Chromium instance. On CI or restricted environments, set `PUPPETEER_EXECUTABLE_PATH` to a system Chromium binary.

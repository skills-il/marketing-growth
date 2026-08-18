# python-pptx RTL Patches for Hebrew Presentations

python-pptx exposes a clean Python API for building presentations, but it does not surface the RTL attributes defined in the OOXML (Office Open XML) spec. Achieving correct Hebrew RTL in a `.pptx` file requires patching the underlying XML directly using `lxml` (which python-pptx bundles).

## Core Concepts

A `.pptx` file is a ZIP archive of XML files. The relevant XML hierarchy for text is:

```
<p:sp>                        # Shape
  <p:txBody>                  # Text body
    <a:bodyPr rtlCol="1"/>    # Body-level RTL (columns, not text direction)
    <a:p>                     # Paragraph
      <a:pPr algn="r" rtl="1"># Paragraph props: rtl="1" ATTRIBUTE (THIS is what you need)
        <a:buFont .../>       # Bullet font
      </a:pPr>
      <a:r>                   # Run
        <a:rPr lang="he-IL"/> # Run properties (language hint)
        <a:t>טקסט</a:t>      # Text content
      </a:r>
    </a:p>
  </p:txBody>
</p:sp>
```

The `rtl="1"` ATTRIBUTE on `<a:pPr>` is the critical patch (this is exactly what PowerPoint itself writes). Per OOXML (ISO/IEC 29500), text direction in DrawingML is a boolean attribute on the paragraph-properties element `<a:pPr>` (CT_TextParagraphProperties) and on the list-style levels `<a:lvl1pPr>`..`<a:lvl9pPr>`. There is NO `<a:rtl>` element anywhere in the DrawingML namespace and `<a:rPr>` (run properties) has no `rtl` attribute, so DrawingML has no run-level direction toggle (this is unlike WordprocessingML's `<w:rtl/>`, which is a common source of confusion). Setting the attribute keeps the file round-trip-clean and honored by LibreOffice and Google Slides import. The attribute must appear on every paragraph containing Hebrew text. The body-level `rtlCol` attribute controls column layout, not text direction, and is insufficient on its own.

## Patch Functions

### 1. Set a Single Paragraph to RTL

```python
from pptx.oxml.ns import qn
from lxml import etree

def set_paragraph_rtl(paragraph):
    """
    Patch a paragraph to display text right-to-left.

    Must be called on every paragraph with Hebrew text. The python-pptx
    API does not expose this attribute, so we patch the XML directly.
    Text direction in DrawingML is the `rtl` ATTRIBUTE on <a:pPr> (what
    PowerPoint writes); there is no <a:rtl> element in DrawingML at all, so
    nothing sets direction at the run level (the bidi algorithm handles it).
    """
    pPr = paragraph._p.get_or_add_pPr()
    pPr.set('rtl', '1')
    # Remove any stale child <a:rtl> a previous version may have injected;
    # no such element is valid in DrawingML, so strip it if present.
    stale = pPr.find(qn('a:rtl'))
    if stale is not None:
        pPr.remove(stale)
```

### 2. Set All Paragraphs in a Text Frame to RTL

```python
def set_text_frame_rtl(text_frame):
    """
    Set all existing paragraphs in a text frame to RTL.

    Call this after adding all text to the text frame.
    Does not affect paragraphs added afterwards (call again or use
    set_paragraph_rtl on each new paragraph).
    """
    for paragraph in text_frame.paragraphs:
        set_paragraph_rtl(paragraph)
```

### 3. Set Text Frame Alignment to Right

```python
from pptx.util import Pt
from pptx.enum.text import PP_ALIGN

def set_text_frame_right_aligned(text_frame):
    """
    Set all paragraphs in a text frame to right-aligned.

    RTL direction and right alignment are separate attributes.
    Both must be set for correct Hebrew rendering.
    """
    for paragraph in text_frame.paragraphs:
        paragraph.alignment = PP_ALIGN.RIGHT
        set_paragraph_rtl(paragraph)
```

### 4. Add Hebrew Text Run with Language Tag

```python
def add_hebrew_run(paragraph, text, font_name='Heebo', font_size_pt=24, bold=False):
    """
    Add a text run with Hebrew language tagging and RTL direction.

    The lang attribute on rPr hints to the renderer that this is Hebrew.
    It does not replace the paragraph-level RTL patch but complements it.
    """
    run = paragraph.add_run()
    run.text = text
    run.font.name = font_name
    run.font.size = Pt(font_size_pt)
    run.font.bold = bold

    # Set language hint on the run
    rPr = run._r.get_or_add_rPr()
    rPr.set('lang', 'he-IL')
    rPr.set('altLang', 'en-US')

    return run
```

### 5. Inline English (LTR) within a Hebrew paragraph

DrawingML has **no run-level direction toggle** (no `<a:rtl>` element, no `rtl`
attribute on `<a:rPr>`), so you do not force a run to LTR with XML. Inline
English terms, URLs, code, and numbers already render left-to-right inside an
RTL paragraph because of the Unicode bidi algorithm (Latin and digits are
inherently LTR). Set `lang="en-US"` only as a proofing hint.

For the genuinely hard case -- a Latin fragment glued to Hebrew with no space
(`B2B-חברות`, `חברת-SaaS`, a version string), or digits whose grouping the
bidi algorithm reorders -- fix it in the TEXT, not the XML, by wrapping the
fragment in Unicode bidi isolates: LRI (U+2066) ... PDI (U+2069), or an LRM
(U+200E) anchor.

```python
def add_english_run(paragraph, text, font_name='Calibri'):
    """Add an English run; no RTL element needed (bidi handles direction)."""
    run = paragraph.add_run()
    run.text = text
    run.font.name = font_name
    run._r.get_or_add_rPr().set('lang', 'en-US')  # proofing hint only
    return run

LRI, PDI = '⁦', '⁩'
text = f"קראתי על {LRI}B2B-SaaS{PDI} אתמול"  # isolate the mixed token
```

### 6. Set Table Cell Text to RTL

```python
def set_table_cell_rtl(cell):
    """
    Set all paragraphs in a table cell to RTL.

    Table cells have their own text frames. The column order in the
    data source must be reversed relative to visual order in RTL mode
    (column index 0 is the rightmost column visually).
    """
    set_text_frame_rtl(cell.text_frame)
    set_text_frame_right_aligned(cell.text_frame)
```

### 7. Set Entire Table to RTL

```python
def set_table_rtl(table):
    """
    Set all cells in a table to RTL.

    IMPORTANT: Also reverse the column order in your data.
    If your data is [col_a, col_b, col_c], the table columns should be
    populated as [col_c, col_b, col_a] to appear in the correct
    right-to-left visual order.
    """
    for row in table.rows:
        for cell in row.cells:
            set_table_cell_rtl(cell)
```

## Complete Slide Building Pattern

```python
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml.ns import qn
from lxml import etree

def build_content_slide(prs, title_text, bullets):
    """
    Build a standard content slide with RTL Hebrew title and bullet list.

    Args:
        prs: Presentation object
        title_text: Hebrew string for the slide title
        bullets: list of Hebrew strings for bullet points
    """
    slide_layout = prs.slide_layouts[1]  # Title and Content layout
    slide = prs.slides.add_slide(slide_layout)

    # Title
    title_shape = slide.shapes.title
    title_tf = title_shape.text_frame
    title_tf.clear()
    title_para = title_tf.paragraphs[0]
    add_hebrew_run(title_para, title_text, font_name='Heebo', font_size_pt=36, bold=True)
    title_para.alignment = PP_ALIGN.RIGHT
    set_paragraph_rtl(title_para)

    # Bullet content
    body_shape = slide.placeholders[1]
    body_tf = body_shape.text_frame
    body_tf.word_wrap = True
    body_tf.clear()

    for i, bullet_text in enumerate(bullets):
        if i == 0:
            para = body_tf.paragraphs[0]
        else:
            para = body_tf.add_paragraph()

        add_hebrew_run(para, bullet_text, font_name='Heebo', font_size_pt=24)
        para.alignment = PP_ALIGN.RIGHT
        set_paragraph_rtl(para)
        para.level = 0  # Top-level bullet

    return slide
```

## Table with Reversed Column Order

```python
def add_rtl_table(slide, headers_rtl_order, rows_data, left, top, width, height):
    """
    Add a table to a slide with RTL column ordering.

    headers_rtl_order: list of header strings ordered right-to-left visually.
                       Index 0 is the rightmost column.
    rows_data: list of lists, each inner list ordered to match headers_rtl_order.
    """
    from pptx.util import Inches, Pt

    cols = len(headers_rtl_order)
    row_count = len(rows_data) + 1  # +1 for header

    table = slide.shapes.add_table(row_count, cols, left, top, width, height).table

    # Header row
    for col_idx, header in enumerate(headers_rtl_order):
        cell = table.cell(0, col_idx)
        cell.text = header
        set_table_cell_rtl(cell)
        # Bold header
        for para in cell.text_frame.paragraphs:
            for run in para.runs:
                run.font.bold = True

    # Data rows
    for row_idx, row_data in enumerate(rows_data):
        for col_idx, cell_text in enumerate(row_data):
            cell = table.cell(row_idx + 1, col_idx)
            cell.text = str(cell_text)
            set_table_cell_rtl(cell)

    return table
```

Usage example:
```python
# Visual order right-to-left: [צמיחה, הכנסות, מדד]
# Which maps to col_index:   [0,       1,       2] in the XML
headers = ['שינוי', '₪ הכנסות', 'מדד']
rows = [
    ['+62%', '₪3.4M', 'Q1 2026'],
    ['+41%', '₪2.9M', 'Q4 2025'],
]
add_rtl_table(slide, headers, rows, ...)
```

## Saving with Embedded Fonts

python-pptx does not have a built-in embed-fonts option (it is a PowerPoint setting). However, you can set the flag in the presentation XML:

```python
def enable_font_embedding(prs):
    """
    Set the EmbedTrueTypeFonts flag in the presentation XML.

    This tells PowerPoint to embed fonts when the file is saved in PowerPoint.
    Note: python-pptx does not itself embed font binary data -- the flag
    instructs PowerPoint to embed on next Save As from the desktop application.
    For truly embedded fonts from a script, use a post-processing step with
    LibreOffice or a dedicated PPTX manipulation library.
    """
    prs_elem = prs.presentation
    # Find or create the <p:embeddedFontLst> or set the flag on the root element
    # The simpler approach: set embedTrueTypeFonts on <p:presentationPr>
    presentationPr = prs_elem.find(qn('p:presentationPr'))
    if presentationPr is None:
        presentationPr = etree.SubElement(prs_elem, qn('p:presentationPr'))
    presentationPr.set('embedTrueTypeFonts', '1')
```

## Debugging RTL Issues

To inspect the XML of a shape after building:
```python
from lxml import etree

# Print the XML of a shape's text body
shape = slide.shapes[0]
print(etree.tostring(shape.text_frame._txBody, pretty_print=True).decode())
```

Check that each `<a:pPr>` element carries the `rtl="1"` attribute. If it is missing on any paragraph, that paragraph will render LTR.

To check a specific paragraph:
```python
para = text_frame.paragraphs[0]
pPr = para._p.find(qn('a:pPr'))
if pPr is not None:
    print(f"RTL set: {pPr.get('rtl') == '1'} (rtl attribute = {pPr.get('rtl')})")
```

## Reference

- [DrawingML text schema: CT_TextParagraphProperties (a:pPr), rtl attribute](https://www.datypic.com/sc/ooxml/e-a_pPr-1.html)
- [python-pptx source: src/pptx/oxml/text.py](https://github.com/scanny/python-pptx/blob/master/src/pptx/oxml/text.py)
- [Unicode Bidirectional Algorithm](https://unicode.org/reports/tr9/)

---
name: israeli-email-sequences
description: >-
  Design email marketing sequences for the Israeli market with Hebrew RTL
  rendering, Jewish and national holiday scheduling, and anti-spam law
  compliance. Use when user asks about Israeli email marketing, Hebrew email
  campaigns, "shivuk b'email", Chok HaSpam compliance, Hebrew newsletter
  design, Israeli drip campaigns, or holiday-triggered email sequences. Covers
  Hebrew RTL email rendering across clients, Israeli holiday calendar for
  campaign timing, subject line optimization, and Amendment 40 compliance.
license: MIT
compatibility: 'No network required. Works with Claude Code, Claude.ai, Cursor.'
metadata:
  author: skills-il
  version: 1.0.0
  category: marketing-growth
  tags:
    he:
      - שיווק-באימייל
      - ניוזלטר
      - דיוור
      - אוטומציה
      - חוק-הספאם
      - קמפיינים
    en:
      - email-marketing
      - newsletter
      - mailing
      - automation
      - anti-spam-law
      - campaigns
  display_name:
    he: סדרות אימייל ישראליות
    en: Israeli Email Sequences
  display_description:
    he: עיצוב קמפיינים ואוטומציות אימייל בעברית תוך ציות לחוק הספאם הישראלי
    en: >-
      Design email marketing sequences for the Israeli market with Hebrew RTL
      rendering, holiday scheduling, and anti-spam law compliance.
  supported_agents:
    - claude-code
    - cursor
    - github-copilot
    - windsurf
    - opencode
    - codex
---

# Israeli Email Sequences

## Instructions

### Step 1: Chok HaSpam Compliance (Amendment 40)

**Legal Requirements (Amendment 40 to the Communications Law, Bezeq and Broadcasting, 1982):**

Israeli anti-spam law (commonly called "Chok HaSpam") is one of the strictest in the world. Key requirements:

| Requirement | Details |
|-------------|---------|
| Prior consent | Must have explicit, documented consent BEFORE sending commercial email |
| Consent type | "Opt-in" required (not opt-out). User must actively agree to receive emails |
| Identification | Every email must clearly identify the sender (name and contact info) |
| Unsubscribe | Must include working unsubscribe mechanism in EVERY commercial email |
| Unsubscribe timing | Must honor unsubscribe requests within 3 business days |
| Record keeping | Must maintain consent records and be able to prove consent if challenged |
| Penalties | Up to 50,000 NIS per violation without proof of damage; court can increase for intentional violations |

**What Counts as "Commercial Email" Under the Law:**
- Direct marketing emails
- Promotional newsletters
- Product announcements
- Sales and discount notifications
- Any email whose primary purpose is commercial promotion

**Exceptions (No consent needed):**
- Existing customer relationships: You may email customers about similar products/services to what they already purchased, IF you gave them opt-out opportunity at time of purchase
- Non-commercial transactional emails (order confirmations, receipts, shipping updates)

**Compliance Checklist:**
- [ ] Documented opt-in consent from every recipient
- [ ] Clear sender identification in every email
- [ ] Working unsubscribe link in every email (Hebrew label: "להסרה מרשימת הדיוור")
- [ ] Unsubscribe honored within 3 business days
- [ ] Consent records maintained and accessible
- [ ] No purchased email lists (buying lists does not constitute consent)

### Step 2: Hebrew RTL Email Rendering

**RTL Email Structure:**
```html
<!-- Base RTL template -->
<html dir="rtl" lang="he">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
    body {
      direction: rtl;
      text-align: right;
      font-family: Arial, Tahoma, sans-serif;
    }
    table {
      direction: rtl;
    }
    /* Fix for Outlook */
    .outlook-fix {
      direction: rtl !important;
      text-align: right !important;
    }
  </style>
</head>
```

**Email Client RTL Support in Israel:**
| Email Client | Market Share (Israel) | RTL Support | Notes |
|-------------|----------------------|-------------|-------|
| Gmail | ~45% | Good | Respects dir="rtl" on html/body |
| Outlook (Desktop) | ~20% | Moderate | Needs MSO conditional comments; table-based layout recommended |
| Apple Mail | ~15% | Good | Full RTL support |
| Yahoo Mail | ~5% | Good | Standard RTL handling |
| Outlook.com | ~10% | Moderate | Similar to desktop Outlook |
| Other | ~5% | Varies | Test case by case |

**Hebrew Font Stack for Email:**
```css
font-family: Arial, Tahoma, 'Segoe UI', sans-serif;
/* Do NOT use: Heebo, Rubik, or other Google Fonts in email
   (limited email client support). Arial and Tahoma have excellent
   Hebrew character rendering across all clients. */
```

**Common RTL Email Issues and Fixes:**
| Issue | Fix |
|-------|-----|
| Text alignment flips in Outlook | Add `dir="rtl"` on every `<td>` element |
| Bullet points on wrong side | Use `unicode-bidi: embed` or HTML entities |
| Numbers appear reversed | Wrap numbers in `<span dir="ltr">` |
| Logo/images misaligned | Use `align="right"` on images |
| CTA button text misaligned | Use inline styles with `direction: rtl` on button element |

### Step 3: Hebrew Subject Line Optimization

**Israeli Email Benchmarks:**
| Metric | Israeli Average | Good Performance |
|--------|----------------|-----------------|
| Open Rate | 20-25% | 30%+ |
| Click Rate | 2-4% | 5%+ |
| Unsubscribe Rate | 0.2-0.5% | < 0.2% |
| Best send day | Tuesday, Wednesday | Test per audience |
| Best send time | 9-10 AM, 7-8 PM | Test per audience |

**Hebrew Subject Line Formulas:**
```
1. Urgency: "רק היום: [הצעה]" (Today only: [offer])
2. Personal: "[שם], יש לנו משהו בשבילך" ([Name], we have something for you)
3. Curiosity: "לא תאמינו מה גילינו על [נושא]" (You won't believe what we discovered about [topic])
4. Benefit: "איך [תועלת] ב-[זמן]" (How to [benefit] in [time])
5. Social proof: "1,000+ ישראלים כבר [פעולה]" (1,000+ Israelis already [action])
6. Question: "עדיין [בעיה]?" (Still [problem]?)
7. Emoji + Hebrew: "🎉 [הודעה מרגשת]" (Exciting announcement)
```

**Subject Line Best Practices for Hebrew:**
- Keep to 40-50 characters (Hebrew takes more visual space than English)
- Preview text (preheader) is equally important; use 40-90 characters
- Personalization with first name increases open rates 15-20%
- Emojis in subject lines increase open rates but test per audience
- Avoid spam trigger words: "חינם" (free) in subject, "הזדמנות אחרונה" (last chance) overuse

### Step 4: Israeli Holiday Email Sequences

**Jewish Holiday Calendar for Email Campaigns:**
| Holiday | Timing | Email Type | Key Themes |
|---------|--------|------------|------------|
| Rosh Hashana | Sep/Oct | Greeting + sale | New beginnings, renewal, sweet themes (honey, apples) |
| Yom Kippur | Sep/Oct | Pre-holiday only | Forgiveness, reflection (NO commercial email on the day) |
| Sukkot | Sep/Oct | Sale, events | Outdoor, family, hospitality |
| Hanukkah | Nov/Dec | Gift guides, sales | Gifts, light, family, 8 days of deals |
| Tu BiShvat | Jan/Feb | Eco-friendly, renewal | Nature, trees, sustainability |
| Purim | Feb/Mar | Fun campaigns, sales | Costumes, fun, gifts (mishloach manot) |
| Pesach | Mar/Apr | Spring cleaning, sales | Freedom, cleaning, family, kosher |
| Yom HaZikaron | Apr/May | Respectful, no sales | Memorial day - absolutely NO commercial email |
| Yom Ha'atzmaut | Apr/May | Patriotic, sales | Blue-white themes, Israeli pride, BBQ |
| Shavuot | May/Jun | Dairy, learning | Cheesecake, white themes, education |

**Holiday Sequence Template:**
```
Pre-holiday (7 days before): Teaser/early access
Pre-holiday (3 days before): Main offer announcement
Holiday eve: Last-minute deals / greeting
Post-holiday (1 day after): Extended sale / welcome back
```

**Critical Rules:**
- NEVER send commercial email on Yom Kippur
- NEVER send commercial email on Yom HaZikaron (Memorial Day)
- Reduce email frequency during Shabbat (Friday sunset to Saturday sunset)
- Be culturally sensitive: Yom HaShoah (Holocaust Remembrance Day) requires solemn tone or no email

### Step 5: Email Sequence Types for Israeli Market

**Welcome Sequence (5 emails):**
```
Email 1 (Immediate): Welcome + value delivery
  Subject: "ברוכים הבאים ל[מותג]! 🎉"
  Content: Welcome message, what to expect, immediate value (guide/discount)

Email 2 (Day 2): Brand story
  Subject: "הסיפור שלנו - למה הקמנו את [מותג]"
  Content: Founder story, Israeli connection, mission

Email 3 (Day 4): Core value
  Subject: "[שם], הנה [תועלת מרכזית] שהבטחנו"
  Content: Key feature/benefit explanation, social proof

Email 4 (Day 7): Social proof
  Subject: "מה אומרים [מספר] הלקוחות שלנו"
  Content: Reviews, testimonials, case studies (Hebrew)

Email 5 (Day 10): Conversion push
  Subject: "מתנה מיוחדת רק בשבילך, [שם]"
  Content: Special offer, urgency, clear CTA
```

**Cart Abandonment Sequence (3 emails):**
```
Email 1 (1 hour): Reminder
  Subject: "שכחת משהו בעגלה 🛒"
  Content: Product image, simple reminder, link back

Email 2 (24 hours): Urgency
  Subject: "הפריטים שלך עדיין ממתינים!"
  Content: Scarcity messaging, social proof, support offer

Email 3 (72 hours): Incentive
  Subject: "הנחה מיוחדת על העגלה שלך - רק היום"
  Content: Discount code, free shipping, last chance
```

**Re-engagement Sequence (3 emails):**
```
Email 1 (30 days inactive): Check-in
  Subject: "התגעגענו אליך, [שם]!"
  Content: Warm message, what's new

Email 2 (45 days inactive): Incentive
  Subject: "מתנה מיוחדת כי חסרת לנו"
  Content: Special offer to return

Email 3 (60 days inactive): Last chance
  Subject: "נשארים בקשר? [שם], זו ההזדמנות האחרונה"
  Content: Unsubscribe warning, final offer
```

### Step 6: Testing and Optimization

**A/B Testing for Israeli Email:**
- Test Hebrew vs Hebrew+emoji subject lines
- Test formal vs informal Hebrew register
- Test send times: morning (9-10 AM) vs evening (7-8 PM)
- Test CTA button text: direct ("קנו עכשיו") vs soft ("לפרטים נוספים")
- Test sender name: brand name vs personal name (CEO/founder name works well in Israel)

**Deliverability for Israeli ISPs:**
- Israeli email is primarily Gmail, Outlook, and Yahoo
- Use authenticated sending: SPF, DKIM, DMARC
- Maintain clean lists; Israeli bounce rates affect sender reputation
- Warm up new sending domains gradually
- Monitor Israeli spam filters: "חינם" (free), "הנחה" (discount) in subject can trigger filters

## Examples

### Example 1: Welcome Sequence for Israeli SaaS
**Input**: "Create a welcome email sequence for an Israeli project management SaaS"
**Output**: 5-email sequence with Hebrew subject lines, RTL HTML templates, casual Israeli tone, progressive value delivery, social proof from Israeli companies, Chok HaSpam compliant with unsubscribe in every email.

### Example 2: Holiday Campaign for E-commerce
**Input**: "Plan email campaigns around the Jewish holiday calendar for an Israeli online store"
**Output**: Full-year email calendar mapped to Jewish and national holidays, with subject lines, content themes, and send timing. Includes blackout dates (Yom Kippur, Yom HaZikaron) and cultural sensitivity guidelines.

### Example 3: RTL Email Template
**Input**: "Build an HTML email template that renders properly in Hebrew across all email clients"
**Output**: Table-based RTL HTML template with Outlook conditional comments, Hebrew font stack, RTL-safe CTA buttons, proper number handling, tested across Gmail, Outlook, and Apple Mail.

## Troubleshooting

- **Issue**: Hebrew text renders left-to-right in some email clients
  **Solution**: Add `dir="rtl"` to every `<table>`, `<td>`, and `<div>` element, not just the outer wrapper. Use inline styles for critical direction/alignment. Test in Litmus or Email on Acid.

- **Issue**: Unsubscribe link not compliant with Chok HaSpam
  **Solution**: Unsubscribe must be in Hebrew ("להסרה מרשימת הדיוור"), clearly visible (not hidden in tiny text), and functional within 3 business days. Include sender identification (company name, address, phone).

- **Issue**: Low open rates compared to benchmarks
  **Solution**: Test send times against Israeli schedule (Sunday is workday, Friday is short). Personalize subject lines with Hebrew first names. Check that preview text is set and not showing HTML code. Verify sender name is recognizable.

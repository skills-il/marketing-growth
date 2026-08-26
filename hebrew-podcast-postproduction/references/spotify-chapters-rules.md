# Spotify Chapter Parsing Rules

Spotify parses chapters from the **episode description** you enter in your podcast host. No separate upload is needed. The parser is strict and silently refuses broken input, so every rule here must be followed exactly.

## Hard rules

| Rule | Value | Source |
|------|-------|--------|
| Minimum chapters per episode | 3 | Spotify Creators support |
| First chapter start time | `00:00` or `00:00:00` | Spotify Creators support |
| Minimum gap between chapters | 30 seconds | Spotify Creators support |
| Chapter title length | "Aim for chapter titles under 40 characters" - a recommendation under Spotify's "Tips for chapter titles", not an enforced maximum | Spotify Creators support |
| Chapter order | Chapters should be in chronological order | Spotify Creators support |
| Index prefixes | Removed by Spotify: "1 - Introduction" is reformatted | Spotify Creators support |
| Very short chapters | "If your chapters are shorter than 30 seconds, consider merging them" | Spotify Creators support |
| Timestamp formats accepted | `(MM:SS)`, `MM:SS`, `(HH:MM:SS)`, `HH:MM:SS` | Spotify Creators support |

## Formatting

Each chapter must be on its **own line** in the description. Between the timestamp and the title, one punctuation mark is allowed (a space, a dash, or a colon). No emojis, no HTML, no markdown bold or italic inside titles.

Valid examples:

```
(00:00) פתיחה
(02:30) איך זה התחיל
(08:45) הטעות שעלתה לי ביוקר
(15:20) מה למדתי
(24:00) מה הלאה
```

```
00:00 Intro
02:30 How it started
08:45 The expensive mistake
```

Invalid examples:

```
[00:00] Intro                  # brackets not accepted
(0:00) Intro                   # single-digit minutes not parsed reliably
(00:00) <b>Intro</b>           # HTML breaks parsing
(00:00) Intro 🔥               # emoji often truncates the title
```

## Reingest timing

After editing the episode description, Spotify states that "it can take a few hours for description updates to reflect across all listening platforms". No specific ceiling is published. If chapters still do not appear, verify the description format - repeatedly re-saving does not speed up the parse.

## Hebrew-specific gotchas

- **Strip nikud from titles.** Vowel points add codepoints that count against the 40-character readability target and can cause the parser to truncate mid-character.
- **Numerical digits render LTR inside RTL titles.** This is expected; do not try to wrap digits in unicode directional markers - Spotify strips them.
- **Do not wrap titles in `<div dir="rtl">`.** The description as a whole can have an RTL div, but individual chapter lines must be plain text.

## Reference

- Official Spotify Creators article on chapters (see Reference Links in SKILL.md)

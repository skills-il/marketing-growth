# Social Caption Limits and Israeli Hashtag Conventions

## Verified 2026 character limits

| Platform | Hard limit | Practical target | Truncation point |
|----------|-----------|------------------|-------------------|
| Instagram Reels | 2,200 | 100-150 | First 125 characters visible before "more" |
| TikTok | 4,000 | 150-300 | None - full caption visible when tapped |
| X (free tier) | 280 | 240-260 | None, but leave room for retweet/quote |
| X (Premium) | 25,000 | Varies | Collapses after ~280, expands on tap |
| LinkedIn (post) | 3,000 | 150-300 | First ~3 lines (210 characters) visible before "see more" |
| LinkedIn (article) | 100,000 | N/A | Articles are long-form blog posts |

Sources: platform help docs and 2026 character limit audits; verify against the current platform UI before publishing if a caption is near the limit.

## Anatomy of a podcast clip caption

Every clip caption should contain four components:

1. **Hook (first line)** - the most quotable 8-15 words from the clip, without context framing. This is what stops the scroll.
2. **Context (1 sentence)** - who is speaking and what the episode is about.
3. **CTA (1 sentence)** - where to listen to the full episode, with a link.
4. **Hashtags (3-7 tags)** - mix of broad and niche.

For Instagram and LinkedIn, pad with blank lines between sections - mobile readers scan, not read.

For X (280 characters), you usually cannot fit all four. Prioritize hook + CTA + 1 hashtag.

## Israeli hashtag conventions

Hebrew hashtags follow different rules from English:

**Do:**
- Concatenate words without spaces or underscores: `#פודקאסטישראלי`
- Mix Hebrew and English tags (TikTok indexes both, doubles the discovery surface)
- Use 3-5 tags per post on Instagram/TikTok, 1-3 on LinkedIn
- Place Hebrew tags at the end of the caption, not inline (Instagram's Hebrew RTL rendering gets confused by inline tags)

**Don't:**
- Use underscores in Hebrew tags - `#פודקאסט_ישראלי` gets parsed as two separate tags by some platforms
- Transliterate: `#startup` works globally; `#סטארטאפ` works in Israel; `#startapp` is neither
- Use more than 8 hashtags on LinkedIn - the algorithm deprioritizes over-tagged posts

## Common Israeli podcast hashtags (verified active)

Broad:
- `#פודקאסט` (1M+ posts)
- `#פודקאסטישראלי`
- `#פודקאסטעברית`
- `#podcast`

Tech/business:
- `#הייטקישראלי`
- `#יזמותישראלית`
- `#סטארטאפ`
- `#israelitech`
- `#startupnation`

Content niches:
- `#תרבותישראלית`
- `#כלכלה`
- `#חדשותטק`
- `#ראיון`

## Platform-specific formatting tips

**Instagram Reels caption:**
- Lead with the hook on its own line
- Blank line, then context
- Blank line, then CTA
- Blank line, then hashtag block (up to 5)
- Use the caption's "link in bio" convention - direct URLs do not render as links in captions

**TikTok caption:**
- Hook + context can share a line
- Hashtags inline at the end
- Use one of TikTok's native sounds if the clip has no music - non-music podcast clips perform noticeably worse
- 150-300 characters performs best (beyond this, users scroll past)

**X (Twitter):**
- Hook + "listen:" + link + 1 hashtag
- Leave 20-30 character buffer for when others quote-tweet
- Threading is better for longer context than a single post

**LinkedIn:**
- The first 3 lines must hook: avoid emoji stuffing, avoid "Excited to share..." openers
- Native document uploads outperform external links - consider uploading a PDF of the episode transcript as a separate post
- Hashtags at the very end, 3-5 maximum

## Reference

- Platform character limit audits (see Reference Links in SKILL.md)

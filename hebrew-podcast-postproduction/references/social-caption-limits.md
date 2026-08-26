# Social Caption Limits and Israeli Hashtag Conventions

## Verified 2026 character limits

| Platform | Hard limit | Practical target | Truncation point |
|----------|-----------|------------------|-------------------|
| Instagram Reels | 2,200 | 100-150 | Meta's media reference also caps a caption at 30 hashtags and 20 @-mentions. The ~125-character "more" truncation point is widely reported but is not stated on any Meta-owned page; treat it as a rule of thumb. |
| TikTok | 2,200 (UTF-16 runes) | 150-300 | The only figure TikTok publishes, in the Content Posting API (`title`, "maximum length is 2200 in UTF-16 runes"). Its help center documents no caption limit. The widely-quoted 4,000 appears on no TikTok-owned page. |
| X (free tier) | 280 | 240-260 | None, but leave room for retweet/quote |
| X (Premium) | Higher than 280, exact ceiling not confirmed on an X-owned page | Varies | Long posts collapse after roughly the standard length and expand on tap. Premium-only: do not plan a caption around it for a general audience. |
| LinkedIn (post) | 3,000 | 150-300 | Truncated after roughly three lines; the exact "see more" cutoff is not published by LinkedIn and varies by viewport, so write the hook into the first two lines rather than counting characters. |
| LinkedIn (article) | Not published by LinkedIn | N/A | The help center states only the 3,000-character post limit and says that above it you "can instead write an article using LinkedIn's Publishing Platform". Do not quote a specific article ceiling; it is not documented. |

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
- Place Hebrew tags at the end of the caption, not inline. A Latin-script `#` immediately followed by Hebrew sits on a bidi boundary, and where it lands visually inside a Hebrew sentence is unpredictable across clients. Putting tags on their own trailing lines sidesteps the question entirely.

**Don't:**
- Use underscores in Hebrew tags. Hebrew hashtags are conventionally written concatenated (`#פודקאסטישראלי`); the underscore form is not the form Israeli users search for, so it costs you the match regardless of how any given platform tokenises it.
- Transliterate: `#startup` works globally; `#סטארטאפ` works in Israel; `#startapp` is neither
- Pile on hashtags on LinkedIn. Three to five focused tags read as professional; a long tag block reads as spam to human readers, which is the effect you can actually observe. LinkedIn publishes no tag-count ranking rule, so treat any specific threshold you see quoted as folklore.

## Common Israeli podcast hashtags

Broad:
- `#פודקאסט` (the broadest Hebrew podcast tag). Per-tag post counts are not published through any citable platform page, so check volume in the app before leaning on a tag.
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
- Consider adding one of TikTok's native sounds under a talking-head clip. This is a widely-followed creator convention rather than a documented ranking factor; TikTok publishes no statement about non-music clips, so test it on your own account rather than treating it as a rule.
- Aim for 150-300 characters. This is a readability target, not a published ranking factor: the caption is collapsed in-feed, so anything past the first couple of lines is only read by someone who already tapped.

**X (Twitter):**
- Hook + "listen:" + link + 1 hashtag
- Leave 20-30 character buffer for when others quote-tweet
- Threading is better for longer context than a single post

**LinkedIn:**
- The first 3 lines must hook: avoid emoji stuffing, avoid "Excited to share..." openers
- Consider uploading a PDF of the episode transcript as a native document post. Native uploads keep the reader on-platform, which is the mechanism people cite; LinkedIn publishes no reach comparison, so treat the advantage as unquantified.
- Hashtags at the very end, 3-5 maximum

## Reference

- Platform character limit audits (see Reference Links in SKILL.md)

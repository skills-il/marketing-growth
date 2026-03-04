# Marketing & Growth Skills

AI agent skills for Israeli marketing, growth hacking, and content strategy.

Part of [Skills IL](https://github.com/skills-il) - curated AI agent skills for Israeli developers.

## Skills

| Skill | Description | Scripts | References |
|-------|-------------|---------|------------|
| [hebrew-seo-toolkit](./hebrew-seo-toolkit/) | Hebrew keyword research with morphological analysis, .co.il domain optimization, hreflang setup, and Israeli business schema markup for Google.co.il | `analyze_keywords.py` | `hebrew-seo.md` |
| [israeli-product-launch](./israeli-product-launch/) | Israeli tech ecosystem launch playbook covering media outreach (Geektime, Calcalist), VC demo day prep, 8200 alumni networks, and Hebrew press releases | -- | `tech-media.md` |
| [israeli-linkedin-strategy](./israeli-linkedin-strategy/) | Bilingual Hebrew/English LinkedIn content strategy with Israeli posting times, Hebrew hashtags, and tech ecosystem engagement patterns | -- | `linkedin-patterns.md` |

## Install

```bash
# Claude Code
claude install github:skills-il/marketing-growth/hebrew-seo-toolkit

# Or clone the full repo
git clone https://github.com/skills-il/marketing-growth.git
```

## Structure

```
marketing-growth/
├── hebrew-seo-toolkit/          # Hebrew SEO optimization and keyword research
│   ├── SKILL.md
│   ├── SKILL_HE.md
│   ├── scripts/
│   └── references/
├── israeli-product-launch/      # Israeli tech product launch playbook
│   ├── SKILL.md
│   ├── SKILL_HE.md
│   └── references/
├── israeli-linkedin-strategy/   # Israeli LinkedIn content strategy
│   ├── SKILL.md
│   ├── SKILL_HE.md
│   └── references/
├── scripts/validate-skill.sh
├── CLAUDE.md
├── LICENSE
└── README.md
```

## Contributing

See the org-level [Contributing Guide](https://github.com/skills-il/.github/blob/main/CONTRIBUTING.md).

## License

MIT

---

Built with care in Israel.

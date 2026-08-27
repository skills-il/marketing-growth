# Domain Checklist: israeli-aso

Coverage contract for a skill that optimizes an app listing for the Israeli storefront on the
Apple App Store and Google Play. Rows are split per category (device class, experiment type,
asset type, storefront) rather than summarized, because a one-row entry for a multi-row official
table is how coverage gaps hide.

Figures are deliberately NOT restated here. Each row names the requirement and its authoritative
page; the values live in `evidence.json` and in the skill body, so there is one place to correct
them.

## Must cover (core)

### A. Field inventory and limits, per store
| # | Item | Source |
|---|---|---|
| M1 | Apple app name limit, per localization | developer.apple.com/help/app-store-connect/reference/app-information |
| M2 | Apple subtitle limit, per localization, indexed | same |
| M3 | Apple keyword field: budget, comma separation, spaces permitted inside a phrase, no-repeat rule, plural/generic/filler exclusions | developer.apple.com/app-store/search/ |
| M4 | Apple promotional text: limit, editable without a build, not a ranking input | developer.apple.com/app-store/product-page/ |
| M5 | Apple editability model: which properties are version-bound vs editable any time | developer.apple.com/help/app-store-connect/reference/required-localizable-and-editable-properties |
| M6 | Play app name, short description, full description limits | support.google.com/googleplay/android-developer/answer/9859152 |

### B. Required assets, one row per asset type
| # | Item | Source |
|---|---|---|
| M7 | Play app icon: dimensions, format, ALPHA REQUIRED (inverts every other Play asset), file-size cap | support.google.com/googleplay/android-developer/answer/9866151 |
| M8 | Play feature graphic: dimensions, format, no alpha, required to publish | same |
| M9 | Play screenshots, phone: publication minimum count, min/max dimension, aspect constraint, per-device cap | same |
| M10 | Play screenshots, tablet/Chromebook: a DIFFERENT spec from phone | same |
| M11 | Play promotion-eligibility bar: distinct from and higher than the publication minimum | same |
| M12 | Apple iPhone 6.9" display class: the accepted sizes, and that there is no separate 6.7" class | developer.apple.com/help/app-store-connect/reference/screenshot-specifications |
| M13 | Apple iPhone 6.5" class: required only when 6.9" is not supplied | same |
| M14 | Apple iPad 13" class: sizes, required if the app runs on iPad | same |
| M15 | Apple app icon and screenshot formats: no alpha or transparency | same |

### C. Locale mechanics for the Israeli storefront
| # | Item | Source |
|---|---|---|
| M16 | Apple Hebrew localization code, and that keyword field / subtitle / description / screenshots are all per-localization | developer.apple.com/help/app-store-connect/manage-app-information/localize-app-information |
| M17 | Play Hebrew locale code (legacy ISO alias, not the modern one) | support.google.com/googleplay/android-developer/answer/9844778 |
| M18 | A localized listing is served by the user's LANGUAGE preference, not by country. Israeli users on English devices see the default listing, so it must also be optimized | same |
| M19 | Apple documented text-relevance inputs, and that the description is not among them | developer.apple.com/app-store/search/ |
| M20 | Play publishes no field-index list; treat the usual three-field claim as practitioner consensus, not documented rule | support.google.com/googleplay/android-developer/answer/9859152 |

### D. Pre-publication compliance gates
| # | Item | Source |
|---|---|---|
| M21 | Apple App Privacy details required to submit new apps and updates; Privacy Policy URL required | developer.apple.com/app-store/app-privacy-details/ |
| M22 | Play App content: privacy policy, content rating questionnaire, target-audience and content declarations, ads and sensitive-permission declarations | support.google.com/googleplay/android-developer/answer/9859455 |
| M23 | Play metadata policy scope: covers title, icon, developer name, description, screenshots and promotional images. Hebrew equivalents count, including text baked into an image | support.google.com/googleplay/android-developer/answer/9898842 |
| M24 | Apple App Review Guidelines apply to the Hebrew localization on the same terms | developer.apple.com/app-store/review/guidelines/ |

### E. Runnable workflow
| # | Item | Source |
|---|---|---|
| M25 | A numbered end-to-end procedure with named inputs and outputs (structural) | n/a |
| M26 | A stated method for producing Hebrew keyword candidates without a paid tool, explicitly excluding scraping and rate-limit or bot-detection evasion (structural) | n/a |
| M27 | Post-publish measurement loop naming where the data lives, so "test it" resolves somewhere | developer.apple.com/help/app-store-connect/view-app-analytics/ ; Play Console acquisition reports |

## Should cover (advanced)
| # | Item | Source |
|---|---|---|
| S1 | Apple Product Page Optimization: treatment cap, duration, testable elements, iOS/iPadOS only, not available on custom product pages, treatments localizable to selected languages | developer.apple.com/help/app-store-connect/create-product-page-optimization-tests/create-a-test |
| S2 | Statistical reality of testing on Israel-only volume inside the duration cap | developer.apple.com/app-store/product-page-optimization/ |
| S3 | Play store-listing A/B tests, per type: default graphics (cannot test text) vs localized (can test descriptions); concurrency budget and variant cap | support.google.com/googleplay/android-developer/answer/9859351 |
| S4 | Apple Custom Product Pages: per-app cap, and keyword assignment surfacing them in search | developer.apple.com/app-store/custom-product-pages/ |
| S5 | Play custom store listings as the Play-side analogue, and which fields are shared across versions. NOT YET VERIFIED against the source; verify before stating any cap | support.google.com/googleplay/android-developer/answer/9867158 |
| S6 | Apple app previews and Play preview video: different mechanisms, per-store constraints | developer.apple.com/help/app-store-connect/reference/app-preview-specifications ; support.google.com/googleplay/android-developer/answer/9866151 |
| S7 | Play alt text on screenshots and graphic assets, localized to Hebrew | support.google.com/googleplay/android-developer/answer/9866151 |
| S8 | Hebrew orthography strategy, budget-ranked: ktiv maleh/chaser first, plurals as a hypothesis, attached prefixes last or never | developer.apple.com/app-store/search/ |
| S9 | Mixed-script and transliterated Israeli queries; when the English brand name outranks its Hebrew transliteration | practitioner; verify in IL-storefront autocomplete |
| S10 | ILS pricing display and the fact that a price baked into an Apple screenshot is version-bound | developer.apple.com/help/app-store-connect/manage-app-pricing/ |
| S11 | Ratings and reviews as a documented App Store ranking input; responding in Hebrew | developer.apple.com/app-store/search/ |
| S12 | Localized "What's New" release notes each release | developer.apple.com/help/app-store-connect/reference/required-localizable-and-editable-properties |

## Out of scope (explicit)
Each row states the question and its answer. Reviewed 2026-08-27.

- **Paid user acquisition** (Apple Search Ads, Google App Campaigns, bidding, ad creative). Would a user ask? Yes, but it is a different discipline with its own budget owner, and `israeli-paid-ads` covers it. Stays out.
- **Scraping, automated store querying, or rate-limit / bot-detection evasion.** Would a user ask? Yes, for keyword volume data. The answer is a refusal plus the manual route in "Sourcing Hebrew keyword candidates", not silence. Stays out permanently.
- **Buying, incentivizing or soliciting ratings; review-gating.** Prohibited by both stores. Stays out permanently.
- **Keyword stuffing, competitor-brand keywords, metadata that violates Apple 2.3 or the Play metadata policy.** Stays out permanently.
- **In-app UI localization and RTL implementation in code.** This skill covers the listing, not the app. A user may well ask; route them to a localization skill rather than answering here.
- **App Store Connect API / Play Developer API automation.** Capturable in principle, but it is a build-pipeline concern, not a listing-content one. Revisit if the skill ever gains a scripted upload step.
- **Non-Israeli storefronts and non-Hebrew localizations.** Out by scope.
- **App Store "app tags" as an Israeli lever.** US storefront only, derived from en_US metadata. Kept as an explicit negative in Gotchas so agents stop chasing it.
- **Legal advice on Israeli consumer, privacy or advertising law.** Out; the listing-level compliance gates are covered, the legal analysis is not.

## Authoritative sources
Apple: /app-store/search/, /app-store/product-page/, /app-store/custom-product-pages/,
/app-store/product-page-optimization/, /app-store/app-privacy-details/, /app-store/review/guidelines/,
App Store Connect Help (app-information, screenshot-specifications, app-preview-specifications,
required-localizable-and-editable-properties, localize-app-information), HIG Right-to-Left.

Google Play: answer/9859152 (store listing), answer/9866151 (preview assets), answer/9844778
(translations and locale codes), answer/9859455 (App content), answer/9898842 (metadata policy),
answer/9859351 (store-listing A/B tests), answer/9867158 (custom store listings), topic/9858052
(policy centre).

Market: gs.statcounter.com/os-market-share/mobile/israel, datareportal.com Digital Israel report.

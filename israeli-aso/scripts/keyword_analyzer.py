#!/usr/bin/env python3
"""Analyze a Hebrew Apple App Store keyword field for Israeli ASO.

The Apple keyword field is a single comma-separated list of terms, max 100
characters PER LOCALIZATION. Apple separates TERMS with commas and no spaces, but
spaces are allowed WITHIN a multi-word phrase; Apple's own documented example is
"Property,House,Real Estate". The common advice that Apple auto-combines single
words into phrases is practitioner convention, not something Apple documents, so
this tool neither requires nor forbids phrases.

What this tool does:
  - de-duplicates your base keywords,
  - builds the comma-no-space Apple field and reports the exact character budget,
  - WARNS (does not silently truncate) when you exceed 100 characters, and tells
    you how many characters and which trailing keywords to cut.

The Hebrew morphology worth budget is SPELLING variance: ktiv maleh vs ktiv chaser
(e.g. משלוח / מישלוח) produces genuinely different strings and cannot be
auto-generated reliably, so supply those yourself.

Plurals are a different matter. Apple documents that plurals of words you already
included are treated as DUPLICATES ("climbs" and "climb") and waste the limit.
That is stated for English, and Apple does not publish how its stemmer handles
Hebrew, where משלוח and משלוחים are unrelated strings. Do not assume a Hebrew
plural is free budget; treat it as a hypothesis to test against your own ranking
data. This tool flags them rather than encouraging them.

Attached stop-word prefixes (ה=the, ו=and, ב=in, ל=to, מ=from, ש=that) are NOT
real user queries and usually waste the 100-char budget; the optional --prefixes
flag will show them only so you can see the cost, with a warning.

Usage:
    python keyword_analyzer.py --keywords "דליברי,משלוחים,אוכל"
    python keyword_analyzer.py --keywords "דליברי,משלוחים,אוכל" --prefixes
    python keyword_analyzer.py --help
"""

import argparse

MAX_FIELD = 100
LOW_VALUE_PREFIXES = {"ה": "the", "ו": "and", "ב": "in", "ל": "to", "מ": "from", "ש": "that"}


def build_field(keywords):
    """De-dupe (preserving order) and join as Apple expects: comma, no space."""
    seen = []
    for k in keywords:
        if k and k not in seen:
            seen.append(k)
    return seen, ",".join(seen)


def main():
    parser = argparse.ArgumentParser(description="Hebrew ASO Apple keyword-field budget analyzer")
    parser.add_argument("--keywords", required=True, help="Comma-separated Hebrew base keywords")
    parser.add_argument("--prefixes", action="store_true",
                        help="Also show attached stop-word-prefix forms (usually budget-wasteful)")
    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",")]
    deduped, field = build_field(keywords)

    print("Hebrew ASO Keyword-Field Analysis")
    print("=" * 50)
    print(f"Base keywords (deduped): {len(deduped)}")
    print("  " + ", ".join(deduped))

    length = len(field)
    print(f"\nApple keyword field: {length}/{MAX_FIELD} characters")
    print(f"  {field}")
    if length > MAX_FIELD:
        over = length - MAX_FIELD
        # figure out which trailing keywords push it over budget
        running, fit = 0, []
        for k in deduped:
            add = len(k) + (1 if fit else 0)
            if running + add > MAX_FIELD:
                break
            running += add
            fit.append(k)
        cut = [k for k in deduped if k not in fit]
        print(f"  OVER BUDGET by {over} characters. Cut to fit (~{MAX_FIELD} chars): drop {', '.join(cut)}")
    else:
        print(f"  OK, {MAX_FIELD - length} characters to spare.")

    print("\nReminders:")
    print("  - Multi-word phrases are allowed: commas separate TERMS, spaces may sit inside a phrase.")
    print("  - Do not repeat words already in the app name, subtitle, or primary category.")
    print("  - Add ktiv maleh/chaser spelling variants yourself; they are genuinely different strings.")
    print("  - Apple treats plurals of included words as duplicates (documented for English, unpublished")
    print("    for Hebrew). Do not spend budget on a Hebrew plural without evidence it ranks separately.")
    print("  - Skip generic terms (app, game), filler words, and special characters unless brand.")
    print("  - Fill the Hebrew (he) localization field with Hebrew terms only; it is separate from English.")

    if args.prefixes:
        print("\nAttached stop-word-prefix forms (usually NOT worth the budget):")
        for kw in deduped:
            forms = [p + kw for p in LOW_VALUE_PREFIXES]
            print(f"  {kw}: {', '.join(forms)}")
        print("  WARNING: forms like ו+word (and-) or ה+word (the-) are not real searches; include only if you have spare budget and evidence users search them.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Analyze a Hebrew Apple App Store keyword field for Israeli ASO.

The Apple keyword field is a single comma-separated list of BASE words, no
spaces, max 100 characters PER LOCALIZATION. Apple's algorithm automatically
combines the single words into phrases and ranks you on each word, so you should
NOT pre-build phrases and you should NOT waste budget on low-value forms.

What this tool does:
  - de-duplicates your base keywords,
  - builds the comma-no-space Apple field and reports the exact character budget,
  - WARNS (does not silently truncate) when you exceed 100 characters, and tells
    you how many characters and which trailing keywords to cut.

The Hebrew morphology that actually matters for the keyword field is SPELLING and
INFLECTION variants you choose deliberately: ktiv maleh vs ktiv chaser (e.g.
משלוח / מישלוח), singular vs plural (משלוח / משלוחים), and gender. Those cannot be
auto-generated reliably, so supply them yourself as additional base keywords.

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
    print("  - Use single base words; Apple auto-combines them, do NOT include phrases.")
    print("  - Add ktiv maleh/chaser spelling and plural/gender variants yourself as base keywords.")
    print("  - Fill the Hebrew (he) localization field with Hebrew terms only; it is separate from English.")

    if args.prefixes:
        print("\nAttached stop-word-prefix forms (usually NOT worth the budget):")
        for kw in deduped:
            forms = [p + kw for p in LOW_VALUE_PREFIXES]
            print(f"  {kw}: {', '.join(forms)}")
        print("  WARNING: forms like ו+word (and-) or ה+word (the-) are not real searches; include only if you have spare budget and evidence users search them.")


if __name__ == "__main__":
    main()

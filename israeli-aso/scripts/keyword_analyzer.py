#!/usr/bin/env python3
"""Analyze Hebrew app store keywords for Israeli ASO.

Generates keyword variants with morphological analysis for Hebrew
app store optimization on Apple App Store and Google Play.

Usage:
    python keyword_analyzer.py --keywords "דליברי,משלוחים,אוכל"
    python keyword_analyzer.py --help
"""

import argparse

PREFIXES = {"ה": "the", "ו": "and", "ב": "in", "ל": "to", "מ": "from", "ש": "that"}

def generate_variants(keyword):
    variants = [keyword]
    for prefix in PREFIXES:
        variants.append(prefix + keyword)
    return variants

def main():
    parser = argparse.ArgumentParser(description="Hebrew ASO keyword analyzer")
    parser.add_argument("--keywords", required=True, help="Comma-separated Hebrew keywords")
    args = parser.parse_args()

    keywords = [k.strip() for k in args.keywords.split(",")]

    print("Hebrew ASO Keyword Analysis")
    print("=" * 50)

    all_variants = []
    for kw in keywords:
        variants = generate_variants(kw)
        all_variants.extend(variants)
        print(f"\n{kw}:")
        for v in variants:
            print(f"  - {v}")

    apple_field = ",".join(all_variants)
    print(f"\nApple keyword field ({len(apple_field)} chars / 100 max):")
    print(apple_field[:100])

if __name__ == "__main__":
    main()

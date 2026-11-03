#!/usr/bin/env python3
"""
Keyword ideas with Google Ads search volume (DataForSEO, paid).
Endpoint: keywords_data/google_ads/keywords_for_keywords/live

Defaults to Israel (2376) and Hebrew (he). Google Ads returns paid-search
competition (LOW/MEDIUM/HIGH and a 0-100 index), NOT an organic keyword
difficulty score; for organic difficulty use related_keywords.py (Labs).
Google Ads live endpoints accept at most 12 requests per minute per account.
The Google Ads docs say language codes follow ISO 639-1 (Hebrew = he) but the
published list is truncated; confirm with GET /v3/keywords_data/google_ads/languages.

Usage: python3 scripts/keyword_research.py "נדל\"ן,דירה להשכרה" --limit 20
"""
import argparse
from dataforseo_api import add_market_args, api_post, format_count, get_result


def main():
    parser = argparse.ArgumentParser(description="Keyword ideas with search volume (paid)")
    parser.add_argument("keywords", help="Seed keyword(s), comma-separated, up to 20")
    add_market_args(parser)
    parser.add_argument("--limit", "-l", type=int, default=20, help="Max rows to print")
    args = parser.parse_args()

    seeds = [k.strip() for k in args.keywords.split(",") if k.strip()][:20]
    data = [{
        "keywords": seeds,
        "location_code": args.location,
        "language_code": args.language,
    }]
    response = api_post("keywords_data/google_ads/keywords_for_keywords/live", data)
    results = get_result(response)

    print(f"seeds: {', '.join(seeds)}")
    print(f"location: {args.location} language: {args.language}")
    if not results:
        print("No results found")
        return
    rows = sorted(results, key=lambda r: r.get("search_volume") or 0, reverse=True)[:args.limit]
    print(f"keywords[{len(rows)}]{{keyword,volume,ads_competition,ads_competition_index}}:")
    for kw in rows:
        print(f"  {kw.get('keyword', 'N/A')},{format_count(kw.get('search_volume'))},"
              f"{kw.get('competition', 'N/A')},{kw.get('competition_index', 'N/A')}")


if __name__ == "__main__":
    main()

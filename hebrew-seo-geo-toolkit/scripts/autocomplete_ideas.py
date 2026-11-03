#!/usr/bin/env python3
"""
Google Autocomplete suggestions (DataForSEO, paid).
Endpoint: serp/google/autocomplete/live/advanced

Defaults to Israel (2376) and Hebrew (he). Each item has type "autocomplete"
and the text in its "suggestion" field.

Usage: python3 scripts/autocomplete_ideas.py "הנהלת חשבונות"
"""
import argparse
from dataforseo_api import add_market_args, api_post, get_result


def main():
    parser = argparse.ArgumentParser(description="Google Autocomplete suggestions (paid)")
    parser.add_argument("keyword", help="Seed keyword")
    add_market_args(parser)
    args = parser.parse_args()

    data = [{
        "keyword": args.keyword,
        "location_code": args.location,
        "language_code": args.language,
    }]
    response = api_post("serp/google/autocomplete/live/advanced", data)
    results = get_result(response)

    print(f"keyword: {args.keyword}")
    print(f"location: {args.location} language: {args.language}")
    suggestions = []
    for result in results:
        for item in result.get("items") or []:
            if item.get("type") == "autocomplete" and item.get("suggestion"):
                suggestions.append(item["suggestion"].strip())
    if not suggestions:
        print("No suggestions found")
        return
    print(f"autocomplete_suggestions[{len(suggestions)}]:")
    for i, suggestion in enumerate(suggestions, 1):
        print(f"  {i}. {suggestion}")


if __name__ == "__main__":
    main()

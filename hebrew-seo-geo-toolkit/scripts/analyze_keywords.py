#!/usr/bin/env python3
"""Hebrew keyword variants, and which of them real searchers actually use.

Israelis search in Hebrew script, so keywords are expected in Hebrew letters
("נדל\"ן", "דירה להשכרה"). The script generates:
  * prefix forms on the first word: ה ו ב כ ל מ ש and common clusters
    (וה, וב, ול, ומ, וש, שה, שב, מה, כש). After ב / כ / ל the definite
    article ה is not written (בבית, not בהבית), so "in the X" and "in X" are the
    same string and are listed once.
  * spelling variants for acronyms: with ", with ״ (gershayim), and without any
    mark (נדל"ן / נדל״ן / נדלן). People type all three.
It does NOT generate plurals, construct-state (smikhut) forms, or ktiv male /
ktiv haser alternatives: those depend on the word and need a human or the agent.

With --gsc-queries, it reads a Google Search Console "Queries" export (CSV) and
reports which generated forms appear in real queries, with their impressions.
That is the actual coverage check: generated forms nobody searches for are not
worth a page.

Usage:
    python3 scripts/analyze_keywords.py --keywords 'נדל"ן,דירה להשכרה'
    python3 scripts/analyze_keywords.py --file keywords.txt --json
    python3 scripts/analyze_keywords.py --keywords 'נדל"ן' --gsc-queries Queries.csv
"""

import argparse
import csv
import json
import re
import sys

HEBREW_RE = re.compile(r"[א-ת]")
SINGLE = ["ה", "ו", "ב", "כ", "ל", "מ", "ש"]
CLUSTERS = ["וה", "וב", "ול", "ומ", "וש", "שה", "שב", "מה", "כש"]
MEANING = {
    "ה": "the", "ו": "and", "ב": "in / in the", "כ": "as / as the", "ל": "to / to the",
    "מ": "from", "ש": "that", "וה": "and the", "וב": "and in", "ול": "and to",
    "ומ": "and from", "וש": "and that", "שה": "that the", "שב": "that in",
    "מה": "from the", "כש": "when",
}
ACRONYM_MARKS = "\"״'׳"

# Transliteration fallback: be/ke/le absorb the article (ba-, ka-, la-).
LATIN_PREFIXES = ["ha", "ve", "be", "ba", "ke", "ka", "le", "la", "me", "mi", "she", "veha", "meha", "sheha"]


def spelling_variants(word: str) -> list:
    """Acronym spellings: ASCII quote, gershayim, and no mark."""
    if not any(m in word for m in ACRONYM_MARKS):
        return [word]
    plain = re.sub(f"[{ACRONYM_MARKS}]", "", word)
    ascii_q = re.sub("[״]", '"', re.sub("[׳]", "'", word))
    gersh = re.sub('"', "״", re.sub("'", "׳", word))
    out = []
    for v in (word, ascii_q, gersh, plain):
        if v not in out:
            out.append(v)
    return out


def variants(keyword: str) -> list:
    """All generated forms of a keyword, each with how it was formed."""
    keyword = keyword.strip()
    if not HEBREW_RE.search(keyword):
        rows = [{"variant": keyword, "form": "base", "meaning": "base form"}]
        rows += [{"variant": f"{p}{keyword}", "form": f"{p}-", "meaning": "transliterated prefix"}
                 for p in LATIN_PREFIXES]
        return rows
    first, _, rest = keyword.partition(" ")
    tail = f" {rest}" if rest else ""
    rows = []
    for spelled in spelling_variants(first):
        label = "base" if spelled == first else "spelling"
        rows.append({"variant": spelled + tail, "form": label, "meaning": "base form"})
        for p in SINGLE + CLUSTERS:
            rows.append({"variant": f"{p}{spelled}{tail}", "form": p, "meaning": MEANING[p]})
    seen, unique = set(), []
    for r in rows:
        if r["variant"] not in seen:
            seen.add(r["variant"])
            unique.append(r)
    return unique


def _norm(text: str) -> str:
    return re.sub(f"[{ACRONYM_MARKS}]", "", text).strip().lower()


def read_gsc_queries(path: str) -> list:
    """Read a Search Console Queries export: (query, clicks, impressions).

    The export's first three columns are the query, clicks and impressions, in
    English or Hebrew headers, so columns are read by position and the header
    row is reported back for the user to confirm.
    """
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader, [])
        rows = []
        for row in reader:
            if len(row) < 3 or not row[0].strip():
                continue
            try:
                clicks = int(float(row[1].replace(",", "") or 0))
                impressions = int(float(row[2].replace(",", "") or 0))
            except ValueError:
                continue
            rows.append((row[0].strip(), clicks, impressions))
    print(f"[gsc] columns used: query='{header[0] if header else '?'}', "
          f"clicks='{header[1] if len(header) > 1 else '?'}', "
          f"impressions='{header[2] if len(header) > 2 else '?'}' ({len(rows)} rows)",
          file=sys.stderr)
    return rows


def coverage(keyword: str, forms: list, queries: list) -> dict:
    """Per prefix form (spellings merged), the queries containing it as whole
    word(s), with the spellings searchers actually typed."""
    norm_forms = []
    for row in forms:
        n = _norm(row["variant"])
        if n not in norm_forms:
            norm_forms.append(n)
    seen = {}
    for n in norm_forms:
        width = len(n.split())
        hits, spellings = [], {}
        for q, clicks, imps in queries:
            raw = q.split()
            for k in range(len(raw) - width + 1):
                window = " ".join(raw[k:k + width])
                if _norm(window) == n:
                    hits.append((q, clicks, imps))
                    spellings[window] = spellings.get(window, 0) + imps
                    break
        if hits:
            seen[n] = {
                "queries": len(hits),
                "clicks": sum(h[1] for h in hits),
                "impressions": sum(h[2] for h in hits),
                "spellings_typed": spellings,
                "examples": [h[0] for h in sorted(hits, key=lambda h: -h[2])[:3]],
            }
    return {"keyword": keyword, "forms_generated": len(norm_forms),
            "forms_seen_in_queries": len(seen),
            "seen": dict(sorted(seen.items(), key=lambda kv: -kv[1]["impressions"]))}


def main():
    parser = argparse.ArgumentParser(description="Hebrew keyword variants and real-query coverage")
    parser.add_argument("--keywords", help="Comma-separated keywords, in Hebrew letters")
    parser.add_argument("--file", help="File with one keyword per line")
    parser.add_argument("--gsc-queries", help="Search Console Queries export (CSV) to check coverage against")
    parser.add_argument("--audit", action="store_true", help="Deprecated: use --gsc-queries")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    if args.audit and not args.gsc_queries:
        print("error: a keyword audit needs real query data. Export Performance > Queries "
              "from Google Search Console as CSV and pass it with --gsc-queries.", file=sys.stderr)
        sys.exit(2)

    if args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]
    elif args.file:
        try:
            with open(args.file, encoding="utf-8") as f:
                keywords = [line.strip() for line in f if line.strip()]
        except FileNotFoundError:
            print(f"error: file not found: {args.file}", file=sys.stderr)
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)

    latin = [k for k in keywords if not HEBREW_RE.search(k)]
    if latin:
        print(f"warning: {', '.join(latin)} not in Hebrew letters. Israelis search in Hebrew "
              "script; transliterated forms are listed but are rarely real queries.", file=sys.stderr)

    results = [{"keyword": k, "variants": variants(k)} for k in keywords]
    if args.gsc_queries:
        queries = read_gsc_queries(args.gsc_queries)
        results = [coverage(r["keyword"], r["variants"], queries) for r in results]

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
        return
    for r in results:
        print(f"\nKeyword: {r['keyword']}")
        if "seen" in r:
            print(f"  {r['forms_seen_in_queries']} of {r['forms_generated']} forms appear in your Search Console queries:")
            for form, s in r["seen"].items():
                typed = ", ".join(f"{sp} ({n})" for sp, n in s["spellings_typed"].items())
                print(f"    {form:24s} queries={s['queries']} impressions={s['impressions']} "
                      f"clicks={s['clicks']}  typed as: {typed}")
            if not r["seen"]:
                print("    none: this keyword family does not show up in your queries yet")
        else:
            print(f"  {len(r['variants'])} forms:")
            for v in r["variants"]:
                print(f"    {v['variant']:28s} [{v['form']}] {v['meaning']}")


if __name__ == "__main__":
    main()

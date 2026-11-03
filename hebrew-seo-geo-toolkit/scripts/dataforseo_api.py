#!/usr/bin/env python3
"""
DataForSEO v3 API wrapper (paid, optional).

Credentials come from the environment only (DATAFORSEO_LOGIN and
DATAFORSEO_PASSWORD, the API password from app.dataforseo.com/api-access,
which differs from the account password). They are sent as a Basic auth header
and are never printed, logged, or accepted as command-line arguments.

Set DATAFORSEO_SANDBOX=1 to send every call to sandbox.dataforseo.com instead.
The sandbox is free for registered users and returns dummy data in the real
response structure, so it proves a request is well formed without spending
credit. It does not return real Israeli search data.
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

from credential import get_dataforseo_credentials

LIVE_BASE = "https://api.dataforseo.com/v3"
SANDBOX_BASE = "https://sandbox.dataforseo.com/v3"

# Israel and Hebrew, per the official DataForSEO locations and languages lists.
ISRAEL = 2376
HEBREW = "he"
# DataForSEO Labs lists only these languages for Israel. Any other pair
# (for example 2376 with "en") is not a supported Labs combination.
LABS_LANGUAGES_FOR_ISRAEL = ("he", "ar")


def api_base() -> str:
    return SANDBOX_BASE if os.environ.get("DATAFORSEO_SANDBOX") == "1" else LIVE_BASE


def add_market_args(parser: argparse.ArgumentParser) -> None:
    """Location and language flags, defaulting to Israel and Hebrew."""
    parser.add_argument("--location", "-loc", type=int, default=ISRAEL,
                        help=f"DataForSEO location_code (default: {ISRAEL} = Israel)")
    parser.add_argument("--language", "-lang", default=HEBREW,
                        help=f"DataForSEO language_code (default: {HEBREW} = Hebrew)")


def check_labs_market(location: int, language: str) -> None:
    """Refuse a Labs request for Israel in a language Labs does not hold."""
    if location == ISRAEL and language not in LABS_LANGUAGES_FOR_ISRAEL:
        print(
            f"error: DataForSEO Labs has no '{language}' data for Israel "
            f"({ISRAEL}); use --language he or --language ar",
            file=sys.stderr,
        )
        sys.exit(2)


def api_post(endpoint: str, data: list) -> dict:
    """POST one task to a DataForSEO endpoint and return the parsed JSON."""
    login, password = get_dataforseo_credentials()
    if not login or not password:
        print("error: DATAFORSEO_LOGIN and DATAFORSEO_PASSWORD are not set.", file=sys.stderr)
        print("Set them as environment variables (never as arguments):", file=sys.stderr)
        print("  export DATAFORSEO_LOGIN=<api login>", file=sys.stderr)
        print("  export DATAFORSEO_PASSWORD=<api password>", file=sys.stderr)
        sys.exit(1)

    url = f"{api_base()}/{endpoint}"
    auth = base64.b64encode(f"{login}:{password}".encode()).decode()
    req = urllib.request.Request(
        url,
        data=json.dumps(data).encode(),
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:500]
        print(f"error: HTTP {e.code} from {endpoint}: {body}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"error: network error calling {endpoint}: {e.reason}", file=sys.stderr)
        sys.exit(1)


def format_count(n) -> str:
    """Format numbers (1234567 -> 1.2M)."""
    if n is None:
        return "0"
    n = int(n)
    if n >= 1_000_000_000:
        return f"{n/1_000_000_000:.1f}B"
    if n >= 1_000_000:
        return f"{n/1_000_000:.1f}M"
    if n >= 1_000:
        return f"{n/1_000:.1f}K"
    return str(n)


def get_result(response: dict) -> list:
    """Return tasks[0].result, reporting any non-20000 status on stderr.

    Checks the top-level status first: an auth or balance error (e.g. 40100,
    40210) arrives there with no usable task.
    """
    if response.get("status_code") not in (None, 20000):
        print(f"error: {response.get('status_code')} {response.get('status_message', '')}",
              file=sys.stderr)
        return []
    tasks = response.get("tasks") or []
    if not tasks:
        return []
    task = tasks[0]
    if task.get("status_code") != 20000:
        print(f"error: {task.get('status_code')} {task.get('status_message', 'Unknown error')}",
              file=sys.stderr)
        return []
    return task.get("result") or []


def print_serp_list(items: list):
    """Print organic SERP results."""
    organic = [i for i in items if i.get("type") == "organic"]
    print(f"serp[{len(organic)}]{{position,title,domain}}:")
    for item in organic[:20]:
        pos = item.get("rank_absolute", "N/A")
        title = (item.get("title") or "")[:50]
        domain = item.get("domain", "N/A")
        print(f"  {pos},{title},{domain}")


def print_backlinks_list(items: list):
    """Print backlinks (rank is on DataForSEO's default 0-1000 scale)."""
    print(f"backlinks[{len(items)}]{{from,to,rank_0_1000,dofollow}}:")
    for item in items:
        url_from = (item.get("url_from") or "")[:50]
        url_to = (item.get("url_to") or "")[:30]
        rank = item.get("rank", "N/A")
        dofollow = item.get("dofollow", False)
        print(f"  {url_from},{url_to},{rank},{dofollow}")

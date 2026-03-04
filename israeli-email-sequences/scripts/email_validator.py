#!/usr/bin/env python3
"""Validate Hebrew email content for RTL rendering and compliance.

Checks email HTML for proper RTL attributes, Chok HaSpam compliance,
and common Hebrew rendering issues.

Usage:
    python email_validator.py --input email.html
    python email_validator.py --help
"""

import argparse
import re
import sys

REQUIRED_ELEMENTS = {
    'dir="rtl"': "RTL direction attribute on html or body",
    "unsubscribe": "Unsubscribe link (Chok HaSpam requirement)",
}

def validate_email(html_content):
    issues = []
    warnings = []

    # Check RTL
    if 'dir="rtl"' not in html_content.lower():
        issues.append("MISSING: dir=\"rtl\" attribute (required for Hebrew emails)")

    # Check unsubscribe
    if "unsubscribe" not in html_content.lower() and "הסרה" not in html_content:
        issues.append("MISSING: Unsubscribe mechanism (Chok HaSpam violation, up to 50,000 NIS fine)")

    # Check sender identification
    if not re.search(r'<address|footer|class="?sender', html_content, re.I):
        warnings.append("WARNING: No visible sender identification found")

    # Check for inline LTR spans around numbers
    numbers_in_hebrew = re.findall(r'[\u0590-\u05FF]\s*\d+', html_content)
    if numbers_in_hebrew and 'dir="ltr"' not in html_content:
        warnings.append("WARNING: Numbers in Hebrew text may need dir=\"ltr\" spans")

    # Check font stack
    if "google fonts" in html_content.lower() or "googleapis.com/css" in html_content:
        warnings.append("WARNING: Google Fonts may not load in all email clients. Use Arial, Tahoma, sans-serif")

    return issues, warnings

def main():
    parser = argparse.ArgumentParser(description="Validate Hebrew email HTML")
    parser.add_argument("--input", required=True, help="HTML email file to validate")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        content = f.read()

    issues, warnings = validate_email(content)

    print("Hebrew Email Validation Report")
    print("=" * 40)

    if issues:
        print(f"\nERRORS ({len(issues)}):")
        for issue in issues:
            print(f"  - {issue}")

    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if not issues and not warnings:
        print("\nAll checks passed.")

    sys.exit(1 if issues else 0)

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate Hebrew email content for RTL rendering and Chok HaSpam structure.

Checks email HTML for RTL attributes and for the structural elements section 30A
of the Communications Law requires in a commercial email. It checks structure
only. It cannot tell you whether your consent record is valid, whether an
exception applies, or whether the message is lawful.

Usage:
    python email_validator.py --input email.html --subject "פרסומת | ..."
    python email_validator.py --help
"""

import argparse
import re
import sys

# Section 30A(e)(1) opener. Only these three words satisfy it.
AD_TAGS = ("\u05e4\u05e8\u05e1\u05d5\u05de\u05ea", "\u05d1\u05e7\u05e9\u05ea \u05ea\u05e8\u05d5\u05de\u05d4", "\u05ea\u05e2\u05de\u05d5\u05dc\u05d4")


def validate_subject(subject):
    """Section 30A(e)(1)(a): the tag word must open the subject line."""
    if subject is None:
        return ["WARNING: no --subject given, so the mandatory subject-line tag was not checked"]
    stripped = subject.lstrip("\ufeff \t\"'\u200f\u200e")
    if not any(stripped.startswith(t) for t in AD_TAGS):
        return ['MISSING: subject line must OPEN with "\u05e4\u05e8\u05e1\u05d5\u05de\u05ea" '
                '(or "\u05d1\u05e7\u05e9\u05ea \u05ea\u05e8\u05d5\u05de\u05d4" / "\u05ea\u05e2\u05de\u05d5\u05dc\u05d4") '
                "per section 30A(e)(1)(a)"]
    return []


def validate_email(html_content):
    issues = []
    warnings = []
    reminders = []

    # Section 30A(e)(1)(a) also requires the tag at the START of the message body,
    # not only in the subject. The subject check lives in validate_subject().
    body_text = re.sub(r"<[^>]+>", " ", html_content)
    if not any(t in body_text for t in AD_TAGS):
        issues.append('MISSING: the word "\u05e4\u05e8\u05e1\u05d5\u05de\u05ea" does not appear in the message body. '
                      "Section 30A(e)(1)(a) requires it at the start of the ad, not only in the subject line.")

    # Check RTL
    if not re.search(r"""dir\s*=\s*['"]?rtl""", html_content, re.I):
        issues.append("MISSING: dir=\"rtl\" attribute (required for Hebrew emails)")

    # Check unsubscribe
    if "unsubscribe" not in html_content.lower() and "הסרה" not in html_content:
        issues.append("MISSING: refusal/unsubscribe route. Section 30A(e)(1)(c) requires a simple "
                      "and reasonable way to refuse plus a valid internet address for it. A court may "
                      "award up to 1,000 NIS per message under section 30A(j)(1). That is the statutory "
                      "ceiling, discretionary and requiring knowledge; it is not an assessment of your exposure.")

    # Check sender identification
    if not re.search(r'<address|footer|class="?sender', html_content, re.I):
        warnings.append("WARNING: no visible sender identification found. Section 30A(e)(1)(b) "
                        "requires the advertiser name, ADDRESS, and contact details. "
                        "(SMS is the carve-out in 30A(e)(2), where the address is not required.)")

    # RFC 8058 one-click unsubscribe lives in the message HEADERS, which an ESP emits and
    # which are not present in template HTML. Checking the body for it produces a false
    # warning on every correctly built email, so it is reported as a reminder, not a finding.
    reminders.append("REMINDER: List-Unsubscribe and List-Unsubscribe-Post are message headers "
                     "set at the ESP account/domain level, not in this HTML. Verify there that "
                     "RFC 8058 one-click is enabled for marketing mail and honoured within 48 hours.")

    # The statutory refusal route must be a real link, not the word "הסרה" sitting in prose.
    if not re.search(r'<a\b[^>]*href=', html_content, re.I):
        warnings.append("WARNING: no <a href> found, so the refusal route may not be clickable. "
                        "Section 30A(e)(1)(c) requires a simple and reasonable way to refuse.")

    # Check for inline LTR spans around numbers
    numbers_in_hebrew = re.findall(r'[\u0590-\u05FF]\s*\d+|\d+\s*[\u0590-\u05FF]', html_content)
    if numbers_in_hebrew and not re.search(r"""dir\s*=\s*['"]?ltr""", html_content, re.I):
        warnings.append("WARNING: Numbers in Hebrew text may need dir=\"ltr\" spans")

    # Check font stack
    if "google fonts" in html_content.lower() or "googleapis.com/css" in html_content:
        warnings.append("WARNING: Google Fonts may not load in all email clients. Use Arial, Tahoma, sans-serif")

    return issues, warnings, reminders

def main():
    parser = argparse.ArgumentParser(description="Validate Hebrew email HTML")
    parser.add_argument("--input", required=True, help="HTML email file to validate")
    parser.add_argument("--subject", help="Subject line, checked for the mandatory 30A(e)(1)(a) tag")
    args = parser.parse_args()

    with open(args.input, "r", encoding="utf-8") as f:
        content = f.read()

    issues, warnings, reminders = validate_email(content)
    for finding in validate_subject(args.subject):
        (warnings if finding.startswith("WARNING") else issues).append(finding)

    print("Hebrew Email Validation Report")
    print("=" * 40)
    print("Structural checks only. Not legal advice, and not a compliance certificate.")

    if issues:
        print(f"\nERRORS ({len(issues)}):")
        for issue in issues:
            print(f"  - {issue}")

    if warnings:
        print(f"\nWARNINGS ({len(warnings)}):")
        for w in warnings:
            print(f"  - {w}")

    if reminders:
        print(f"\nREMINDERS ({len(reminders)}):")
        for r in reminders:
            print(f"  - {r}")

    if not issues and not warnings:
        print("\nAll structural checks passed. This is not a legal opinion.")
        print("Checked: RTL attributes, LTR wrapping of numbers, the subject-line and body "
              "\u05e4\u05e8\u05e1\u05d5\u05de\u05ea tag, a clickable refusal route, and a sender block.")
        print("NOT checked: whether your consent record is valid, whether an exception applies, "
              "whether the sender block carries a real ADDRESS, the section 17\u05d5 registration "
              "number, or any message header.")

    sys.exit(1 if issues else 0)

if __name__ == "__main__":
    main()

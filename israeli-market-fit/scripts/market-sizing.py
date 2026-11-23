#!/usr/bin/env python3
"""
market-sizing.py - bottom-up TAM/SAM/SOM estimator for the Israeli market.

The point of this script is discipline, not precision: it forces a market-fit
estimate to be built from a real count of buying units, a defensible adoption
fraction, and an annual spend per unit, instead of a hand-waved "the Israeli
market is huge" number. Israel's whole population is about 10.305 million, so
the serviceable number is usually much smaller than founders expect.

Use one buying unit throughout (person, adult, household, or business account).
All monetary inputs and outputs are in shekels, and spend should be net of VAT. Adoption and serviceable shares
are fractions between 0 and 1 (e.g. 0.05 for one in twenty), NOT figures with a
percent sign, on purpose: it keeps you honest about the actual ratio.

Usage:
    python market-sizing.py --segment-pop 2000000 --adoption 0.04 \
        --annual-spend 240 --serviceable 0.15

    # interactive prompts if no flags are given:
    python market-sizing.py
"""

import argparse
import sys


def estimate(segment_pop: float, adoption: float, annual_spend: float, serviceable: float) -> dict:
    """TAM = whole segment if everyone bought. SAM = realistic adopters.
    SOM = the annual revenue from the slice you can actually win early."""
    if not (0 <= adoption <= 1):
        raise ValueError("adoption must be a fraction between 0 and 1")
    if not (0 <= serviceable <= 1):
        raise ValueError("serviceable must be a fraction between 0 and 1")

    tam = segment_pop * annual_spend
    sam = segment_pop * adoption * annual_spend
    som = sam * serviceable
    buyers = segment_pop * adoption * serviceable
    return {"tam": tam, "sam": sam, "som": som, "buyers": buyers}


def shekels(value: float) -> str:
    # Build the currency string at runtime so the figure is not a literal in source.
    sign = "₪"
    return sign + format(round(value), ",")


def fmt_ratio(value: float) -> str:
    return format(value * 100, ".1f") + " per hundred"


def main() -> int:
    p = argparse.ArgumentParser(description="Bottom-up TAM/SAM/SOM for an Israeli market segment.")
    p.add_argument("--segment-pop", type=float, help="buying units in the segment: people, adults, households, or business accounts")
    p.add_argument("--adoption", type=float, help="fraction of those units that would realistically buy (0-1)")
    p.add_argument("--annual-spend", type=float, help="annual spend per unit, in shekels, net of VAT")
    p.add_argument("--serviceable", type=float, help="fraction of adopters you can win early (0-1)")
    args = p.parse_args()

    def ask(prompt: str) -> float:
        return float(input(prompt).strip())

    seg = args.segment_pop if args.segment_pop is not None else ask("Buying units in the segment: ")
    adoption = args.adoption if args.adoption is not None else ask("Adoption fraction (0-1): ")
    spend = args.annual_spend if args.annual_spend is not None else ask("Annual spend per unit, net of VAT (shekels): ")
    serviceable = args.serviceable if args.serviceable is not None else ask("Fraction of adopters you can win early (0-1): ")

    try:
        r = estimate(seg, adoption, spend, serviceable)
    except ValueError as e:
        print("Error: " + str(e), file=sys.stderr)
        return 1

    print("Adoption assumption: " + fmt_ratio(adoption))
    print("Early-win assumption: " + fmt_ratio(serviceable))
    print("TAM (whole segment): " + shekels(r["tam"]))
    print("SAM (realistic adopters): " + shekels(r["sam"]))
    print("SOM (annual revenue once won): " + shekels(r["som"]))
    print("Estimated early buyers: " + format(round(r["buyers"]), ","))
    print()
    print("Reality check: SOM x gross margin, minus acquisition cost, must cover fixed costs. In a market of about")
    print("10.305 million people, a narrow segment can be too small to clear the cost floor.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""
Israeli Tech Salary Calculator

Calculate total annual compensation from base salary, benefits, equity,
and allowances for Israeli tech positions.

Usage:
    python salary-calculator.py --base 40000
    python salary-calculator.py --base 40000 --pension-employer 6.5 --keren-employer 7.5
    python salary-calculator.py --base 40000 --equity-value 200000 --equity-vesting 4
    python salary-calculator.py --compare --base1 40000 --base2 45000 --equity1 100000 --equity2 0
"""

import argparse
import json
import sys
from dataclasses import dataclass
from typing import Optional


@dataclass
class CompensationPackage:
    """Represents a full Israeli tech compensation package."""

    # Base salary
    base_monthly: float = 0.0

    # Pension rates (percentage of base)
    pension_employee_rate: float = 6.0
    pension_employer_rate: float = 6.5
    severance_rate: float = 8.33

    # Keren Hishtalmut rates (percentage of base)
    keren_employee_rate: float = 2.5
    keren_employer_rate: float = 7.5

    # Allowances (monthly NIS)
    car_allowance: float = 0.0
    meal_allowance: float = 0.0
    phone_allowance: float = 0.0
    other_allowances: float = 0.0

    # Vacation
    vacation_days: int = 15
    recuperation_days: int = 5

    # Bonus
    annual_bonus_percent: float = 0.0
    signing_bonus: float = 0.0

    # Equity
    equity_total_value: float = 0.0
    equity_vesting_years: int = 4
    equity_discount: float = 0.0  # Illiquidity discount percentage (0-100)

    # Label for display
    label: str = "Package"

    @property
    def base_annual(self) -> float:
        return self.base_monthly * 12

    @property
    def pension_employer_monthly(self) -> float:
        return self.base_monthly * (self.pension_employer_rate / 100)

    @property
    def pension_employer_annual(self) -> float:
        return self.pension_employer_monthly * 12

    @property
    def pension_employee_monthly(self) -> float:
        return self.base_monthly * (self.pension_employee_rate / 100)

    @property
    def severance_monthly(self) -> float:
        return self.base_monthly * (self.severance_rate / 100)

    @property
    def severance_annual(self) -> float:
        return self.severance_monthly * 12

    @property
    def keren_employer_monthly(self) -> float:
        return self.base_monthly * (self.keren_employer_rate / 100)

    @property
    def keren_employer_annual(self) -> float:
        return self.keren_employer_monthly * 12

    @property
    def keren_employee_monthly(self) -> float:
        return self.base_monthly * (self.keren_employee_rate / 100)

    @property
    def car_annual(self) -> float:
        return self.car_allowance * 12

    @property
    def meal_annual(self) -> float:
        return self.meal_allowance * 12

    @property
    def other_allowances_annual(self) -> float:
        return (self.phone_allowance + self.other_allowances) * 12

    @property
    def recuperation_annual(self) -> float:
        # Dmey Havra'a: 418 NIS per day (private sector, 2026 — frozen since 2023)
        return self.recuperation_days * 418

    @property
    def bonus_annual(self) -> float:
        return self.base_annual * (self.annual_bonus_percent / 100)

    @property
    def equity_annual(self) -> float:
        if self.equity_vesting_years <= 0:
            return 0
        discounted = self.equity_total_value * (1 - self.equity_discount / 100)
        return discounted / self.equity_vesting_years

    @property
    def total_employer_cost_monthly(self) -> float:
        return (
            self.base_monthly
            + self.pension_employer_monthly
            + self.severance_monthly
            + self.keren_employer_monthly
            + self.car_allowance
            + self.meal_allowance
            + self.phone_allowance
            + self.other_allowances
        )

    @property
    def total_annual_compensation(self) -> float:
        """Total annual compensation including all components."""
        return (
            self.base_annual
            + self.pension_employer_annual
            + self.severance_annual
            + self.keren_employer_annual
            + self.car_annual
            + self.meal_annual
            + self.other_allowances_annual
            + self.recuperation_annual
            + self.bonus_annual
            + self.equity_annual
            + self.signing_bonus
        )

    @property
    def total_annual_without_equity(self) -> float:
        """Total annual compensation excluding equity (for conservative estimate)."""
        return self.total_annual_compensation - self.equity_annual

    @property
    def employee_deductions_monthly(self) -> float:
        """Monthly deductions from employee salary."""
        return self.pension_employee_monthly + self.keren_employee_monthly

    @property
    def net_effective_monthly(self) -> float:
        """Approximate monthly take-home before income tax (base minus employee deductions)."""
        return self.base_monthly - self.employee_deductions_monthly


def format_nis(amount: float) -> str:
    """Format a number as NIS currency."""
    if amount >= 1000:
        return f"{amount:,.0f} NIS"
    return f"{amount:.0f} NIS"


def print_breakdown(pkg: CompensationPackage) -> None:
    """Print a detailed compensation breakdown."""
    print(f"\n{'=' * 60}")
    print(f"  COMPENSATION BREAKDOWN: {pkg.label}")
    print(f"{'=' * 60}")

    print(f"\n  Base Salary")
    print(f"    Monthly (gross):          {format_nis(pkg.base_monthly):>15}")
    print(f"    Annual (gross):           {format_nis(pkg.base_annual):>15}")

    print(f"\n  Pension (Employer Contributions)")
    print(f"    Pension ({pkg.pension_employer_rate}%):          {format_nis(pkg.pension_employer_monthly):>15} /mo")
    print(f"    Severance ({pkg.severance_rate}%):        {format_nis(pkg.severance_monthly):>15} /mo")
    print(f"    Annual pension total:     {format_nis(pkg.pension_employer_annual + pkg.severance_annual):>15}")

    if pkg.keren_employer_rate > 0:
        print(f"\n  Keren Hishtalmut")
        print(f"    Employer ({pkg.keren_employer_rate}%):          {format_nis(pkg.keren_employer_monthly):>15} /mo")
        print(f"    Annual:                   {format_nis(pkg.keren_employer_annual):>15}")

    if any([pkg.car_allowance, pkg.meal_allowance, pkg.phone_allowance, pkg.other_allowances]):
        print(f"\n  Allowances")
        if pkg.car_allowance > 0:
            print(f"    Car allowance:            {format_nis(pkg.car_allowance):>15} /mo")
        if pkg.meal_allowance > 0:
            print(f"    Meal allowance:           {format_nis(pkg.meal_allowance):>15} /mo")
        if pkg.phone_allowance > 0:
            print(f"    Phone allowance:          {format_nis(pkg.phone_allowance):>15} /mo")
        if pkg.other_allowances > 0:
            print(f"    Other allowances:         {format_nis(pkg.other_allowances):>15} /mo")
        total_allowances = pkg.car_annual + pkg.meal_annual + pkg.other_allowances_annual
        print(f"    Annual allowances total:  {format_nis(total_allowances):>15}")

    print(f"\n  Time Off")
    print(f"    Vacation days:            {pkg.vacation_days:>15} days")
    vacation_value = pkg.vacation_days * (pkg.base_monthly / 22)
    print(f"    Vacation value:           {format_nis(vacation_value):>15}")
    print(f"    Recuperation pay:         {format_nis(pkg.recuperation_annual):>15} /yr")

    if pkg.annual_bonus_percent > 0 or pkg.signing_bonus > 0:
        print(f"\n  Bonuses")
        if pkg.annual_bonus_percent > 0:
            print(f"    Annual bonus ({pkg.annual_bonus_percent}%):     {format_nis(pkg.bonus_annual):>15}")
        if pkg.signing_bonus > 0:
            print(f"    Signing bonus (one-time): {format_nis(pkg.signing_bonus):>15}")

    if pkg.equity_total_value > 0:
        print(f"\n  Equity")
        print(f"    Total grant value:        {format_nis(pkg.equity_total_value):>15}")
        print(f"    Vesting period:           {pkg.equity_vesting_years:>15} years")
        if pkg.equity_discount > 0:
            print(f"    Illiquidity discount:     {pkg.equity_discount:>14.0f}%")
        print(f"    Annual equity value:      {format_nis(pkg.equity_annual):>15}")

    print(f"\n  {'_' * 56}")
    print(f"\n  TOTALS")
    print(f"    Employer cost (monthly):  {format_nis(pkg.total_employer_cost_monthly):>15}")
    print(f"    Total annual comp:        {format_nis(pkg.total_annual_compensation):>15}")
    if pkg.equity_annual > 0:
        print(f"    Annual (excl. equity):    {format_nis(pkg.total_annual_without_equity):>15}")

    print(f"\n  Employee Deductions")
    print(f"    Pension ({pkg.pension_employee_rate}%):          {format_nis(pkg.pension_employee_monthly):>15} /mo")
    if pkg.keren_employee_rate > 0:
        print(f"    Keren Hishtalmut ({pkg.keren_employee_rate}%):  {format_nis(pkg.keren_employee_monthly):>15} /mo")
    print(f"    Total deductions:         {format_nis(pkg.employee_deductions_monthly):>15} /mo")
    print(f"    Pre-tax effective pay:    {format_nis(pkg.net_effective_monthly):>15} /mo")

    print(f"\n{'=' * 60}\n")


def print_comparison(pkg1: CompensationPackage, pkg2: CompensationPackage) -> None:
    """Print a side-by-side comparison of two packages."""
    print(f"\n{'=' * 72}")
    print(f"  PACKAGE COMPARISON")
    print(f"{'=' * 72}")
    print(f"  {'Component':<30} {pkg1.label:>18} {pkg2.label:>18}")
    print(f"  {'-' * 66}")

    rows = [
        ("Base (monthly)", pkg1.base_monthly, pkg2.base_monthly),
        ("Base (annual)", pkg1.base_annual, pkg2.base_annual),
        ("Pension (employer, annual)", pkg1.pension_employer_annual, pkg2.pension_employer_annual),
        ("Severance (annual)", pkg1.severance_annual, pkg2.severance_annual),
        ("Keren Hishtalmut (annual)", pkg1.keren_employer_annual, pkg2.keren_employer_annual),
        ("Car allowance (annual)", pkg1.car_annual, pkg2.car_annual),
        ("Meal allowance (annual)", pkg1.meal_annual, pkg2.meal_annual),
        ("Recuperation pay", pkg1.recuperation_annual, pkg2.recuperation_annual),
        ("Annual bonus", pkg1.bonus_annual, pkg2.bonus_annual),
        ("Signing bonus", pkg1.signing_bonus, pkg2.signing_bonus),
        ("Equity (annual)", pkg1.equity_annual, pkg2.equity_annual),
    ]

    for label, val1, val2 in rows:
        if val1 > 0 or val2 > 0:
            print(f"  {label:<30} {format_nis(val1):>18} {format_nis(val2):>18}")

    print(f"  {'-' * 66}")
    print(f"  {'TOTAL ANNUAL':<30} {format_nis(pkg1.total_annual_compensation):>18} {format_nis(pkg2.total_annual_compensation):>18}")

    diff = pkg2.total_annual_compensation - pkg1.total_annual_compensation
    diff_pct = (diff / pkg1.total_annual_compensation * 100) if pkg1.total_annual_compensation > 0 else 0
    sign = "+" if diff >= 0 else ""
    print(f"  {'DIFFERENCE':<30} {'':>18} {sign}{format_nis(diff):>17}")
    print(f"  {'DIFFERENCE (%)':<30} {'':>18} {sign}{diff_pct:>16.1f}%")

    print(f"\n  Vacation: {pkg1.label} = {pkg1.vacation_days} days, {pkg2.label} = {pkg2.vacation_days} days")

    print(f"\n{'=' * 72}\n")


def print_json_output(pkg: CompensationPackage) -> None:
    """Print compensation breakdown as JSON."""
    output = {
        "label": pkg.label,
        "base_monthly": pkg.base_monthly,
        "base_annual": pkg.base_annual,
        "pension_employer_annual": pkg.pension_employer_annual,
        "severance_annual": pkg.severance_annual,
        "keren_hishtalmut_employer_annual": pkg.keren_employer_annual,
        "car_allowance_annual": pkg.car_annual,
        "meal_allowance_annual": pkg.meal_annual,
        "recuperation_pay": pkg.recuperation_annual,
        "annual_bonus": pkg.bonus_annual,
        "signing_bonus": pkg.signing_bonus,
        "equity_annual": pkg.equity_annual,
        "total_annual_compensation": pkg.total_annual_compensation,
        "total_annual_without_equity": pkg.total_annual_without_equity,
        "employer_cost_monthly": pkg.total_employer_cost_monthly,
        "employee_deductions_monthly": pkg.employee_deductions_monthly,
        "vacation_days": pkg.vacation_days,
    }
    print(json.dumps(output, indent=2))


def main():
    parser = argparse.ArgumentParser(
        description="Israeli Tech Salary Calculator - Compute total compensation packages",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic calculation
  %(prog)s --base 40000

  # Full package with all benefits
  %(prog)s --base 40000 --pension-employer 6.5 --keren-employer 7.5 \\
           --car-allowance 3000 --meal-allowance 1000 --vacation-days 20

  # With equity
  %(prog)s --base 42000 --equity-value 200000 --equity-vesting 4 --equity-discount 30

  # Compare two offers
  %(prog)s --compare --base1 40000 --base2 45000 \\
           --equity1 100000 --equity2 0 --label1 "Startup" --label2 "Enterprise"

  # JSON output
  %(prog)s --base 40000 --json
        """,
    )

    # Single package arguments
    parser.add_argument("--base", type=float, help="Monthly base salary (NIS)")

    # Pension
    parser.add_argument("--pension-employee", type=float, default=6.0,
                        help="Employee pension rate %% (default: 6.0)")
    parser.add_argument("--pension-employer", type=float, default=6.5,
                        help="Employer pension rate %% (default: 6.5)")
    parser.add_argument("--severance-rate", type=float, default=8.33,
                        help="Severance contribution rate %% (default: 8.33)")

    # Keren Hishtalmut
    parser.add_argument("--keren-employee", type=float, default=2.5,
                        help="Employee keren hishtalmut rate %% (default: 2.5)")
    parser.add_argument("--keren-employer", type=float, default=7.5,
                        help="Employer keren hishtalmut rate %% (default: 7.5)")
    parser.add_argument("--no-keren", action="store_true",
                        help="No keren hishtalmut (set both rates to 0)")

    # Allowances
    parser.add_argument("--car-allowance", type=float, default=0,
                        help="Monthly car allowance (NIS)")
    parser.add_argument("--meal-allowance", type=float, default=0,
                        help="Monthly meal allowance (NIS)")
    parser.add_argument("--phone-allowance", type=float, default=0,
                        help="Monthly phone allowance (NIS)")

    # Vacation
    parser.add_argument("--vacation-days", type=int, default=15,
                        help="Annual vacation days (default: 15)")
    parser.add_argument("--recuperation-days", type=int, default=5,
                        help="Recuperation days (default: 5)")

    # Bonus
    parser.add_argument("--bonus", type=float, default=0,
                        help="Annual bonus as %% of base (default: 0)")
    parser.add_argument("--signing-bonus", type=float, default=0,
                        help="One-time signing bonus (NIS)")

    # Equity
    parser.add_argument("--equity-value", type=float, default=0,
                        help="Total equity grant value (NIS)")
    parser.add_argument("--equity-vesting", type=int, default=4,
                        help="Equity vesting period in years (default: 4)")
    parser.add_argument("--equity-discount", type=float, default=0,
                        help="Illiquidity discount %% (default: 0)")

    # Comparison mode
    parser.add_argument("--compare", action="store_true", help="Compare two packages")
    parser.add_argument("--base1", type=float, help="Package 1 base salary")
    parser.add_argument("--base2", type=float, help="Package 2 base salary")
    parser.add_argument("--car-allowance1", type=float, default=0)
    parser.add_argument("--car-allowance2", type=float, default=0)
    parser.add_argument("--meal-allowance1", type=float, default=0)
    parser.add_argument("--meal-allowance2", type=float, default=0)
    parser.add_argument("--vacation-days1", type=int, default=15)
    parser.add_argument("--vacation-days2", type=int, default=15)
    parser.add_argument("--bonus1", type=float, default=0)
    parser.add_argument("--bonus2", type=float, default=0)
    parser.add_argument("--signing-bonus1", type=float, default=0)
    parser.add_argument("--signing-bonus2", type=float, default=0)
    parser.add_argument("--equity1", type=float, default=0)
    parser.add_argument("--equity2", type=float, default=0)
    parser.add_argument("--equity-vesting1", type=int, default=4)
    parser.add_argument("--equity-vesting2", type=int, default=4)
    parser.add_argument("--equity-discount1", type=float, default=0)
    parser.add_argument("--equity-discount2", type=float, default=0)
    parser.add_argument("--label1", type=str, default="Offer A")
    parser.add_argument("--label2", type=str, default="Offer B")

    # Output format
    parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    # Handle no-keren flag
    if args.no_keren:
        args.keren_employee = 0.0
        args.keren_employer = 0.0

    if args.compare:
        if not args.base1 or not args.base2:
            parser.error("Comparison mode requires --base1 and --base2")

        pkg1 = CompensationPackage(
            base_monthly=args.base1,
            pension_employee_rate=args.pension_employee,
            pension_employer_rate=args.pension_employer,
            severance_rate=args.severance_rate,
            keren_employee_rate=args.keren_employee,
            keren_employer_rate=args.keren_employer,
            car_allowance=args.car_allowance1,
            meal_allowance=args.meal_allowance1,
            vacation_days=args.vacation_days1,
            recuperation_days=args.recuperation_days,
            annual_bonus_percent=args.bonus1,
            signing_bonus=args.signing_bonus1,
            equity_total_value=args.equity1,
            equity_vesting_years=args.equity_vesting1,
            equity_discount=args.equity_discount1,
            label=args.label1,
        )

        pkg2 = CompensationPackage(
            base_monthly=args.base2,
            pension_employee_rate=args.pension_employee,
            pension_employer_rate=args.pension_employer,
            severance_rate=args.severance_rate,
            keren_employee_rate=args.keren_employee,
            keren_employer_rate=args.keren_employer,
            car_allowance=args.car_allowance2,
            meal_allowance=args.meal_allowance2,
            vacation_days=args.vacation_days2,
            recuperation_days=args.recuperation_days,
            annual_bonus_percent=args.bonus2,
            signing_bonus=args.signing_bonus2,
            equity_total_value=args.equity2,
            equity_vesting_years=args.equity_vesting2,
            equity_discount=args.equity_discount2,
            label=args.label2,
        )

        if args.json:
            output = {
                "package1": {
                    "label": pkg1.label,
                    "total_annual": pkg1.total_annual_compensation,
                },
                "package2": {
                    "label": pkg2.label,
                    "total_annual": pkg2.total_annual_compensation,
                },
                "difference": pkg2.total_annual_compensation - pkg1.total_annual_compensation,
            }
            print(json.dumps(output, indent=2))
        else:
            print_breakdown(pkg1)
            print_breakdown(pkg2)
            print_comparison(pkg1, pkg2)

    elif args.base:
        pkg = CompensationPackage(
            base_monthly=args.base,
            pension_employee_rate=args.pension_employee,
            pension_employer_rate=args.pension_employer,
            severance_rate=args.severance_rate,
            keren_employee_rate=args.keren_employee,
            keren_employer_rate=args.keren_employer,
            car_allowance=args.car_allowance,
            meal_allowance=args.meal_allowance,
            phone_allowance=args.phone_allowance,
            vacation_days=args.vacation_days,
            recuperation_days=args.recuperation_days,
            annual_bonus_percent=args.bonus,
            signing_bonus=args.signing_bonus,
            equity_total_value=args.equity_value,
            equity_vesting_years=args.equity_vesting,
            equity_discount=args.equity_discount,
            label="Your Package",
        )

        if args.json:
            print_json_output(pkg)
        else:
            print_breakdown(pkg)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

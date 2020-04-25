from texttable import Texttable
from operator import attrgetter
from typing import List
from .tax import Tax, Tax2019Regime, Tax2020Regime, Deductions


YEAR_TAX_MAP = {
    2019: Tax2019Regime,
    2020: Tax2020Regime,
}


def _get_taxes(
    income: int,
    sec80c: int,
    sec80d: int,
    sec24b: int,
    years: set = set(YEAR_TAX_MAP.keys())
) -> List[Tax]:
    return [
        YEAR_TAX_MAP[y](
            gross_income=income,
            deductions=Deductions(sec80c, sec80d, sec24b)
        )
        for y in years
    ]


def get_user_tax_interactive() -> tuple:
    years = set(YEAR_TAX_MAP.keys())

    try:
        income = int(input("\nEnter income: ") or 0)
        sec80c = int(input(
            "Enter expenses under section 80C "
            "(investments & payments): "
        ) or 0)
        sec80d = int(input(
            "Enter expenses under section 80D "
            "(health insurance): "
        ) or 0)
        sec24b = int(input(
            "Enter expenses under section 24(b) "
            "(housing loan): "
        ) or 0)

        return income, sec80c, sec80d, sec24b, years
    except Exception:
        raise Exception("Invalid input value")


def lowest(
    income: int,
    sec80c: int,
    sec80d: int,
    sec24b: int,
    years: set = set(YEAR_TAX_MAP.keys()),
    display: bool = False
) -> int:
    taxes = _get_taxes(income, sec80c, sec80d, sec24b, years)
    least_tax = min(taxes, key=attrgetter('total_tax'))

    if not display:
        return least_tax

    for tax in taxes:
        print(tax.tabular())

    t = Texttable()
    t.add_rows([
        ["Lowest Tax Regime", f'✨{least_tax.YEAR}✨'],
        ["Tax to be paid", f'{least_tax.total_tax}']
    ], header=False)
    print(f'\n\nResult: \n{t.draw()}')
    return least_tax


def lowest_interactive() -> None:
    print("\nIndian Tax Regime Comparison\n(All units are in INR)")
    years, income, sec80c, sec80d, sec24b = get_user_tax_interactive()
    lowest(years, income, sec80c, sec80d, sec24b, display=True)

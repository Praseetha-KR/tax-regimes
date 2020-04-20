import attr
from texttable import Texttable
from .utils import percentage


@attr.s
class Deductions:
    sec80c = attr.ib(default=0)
    sec80d = attr.ib(default=0)
    sec24b = attr.ib(default=0)


@attr.s
class Slab:
    lower = attr.ib(default=0)
    upper = attr.ib(default=None)
    percent = attr.ib(default=0)


@attr.s
class Tax:
    SLABS = [Slab()]
    DEDUCTIONS = Deductions()
    CESS = 4
    YEAR = 0

    gross_income = attr.ib(default=0)
    deductions = attr.ib(default=Deductions())

    def __attrs_post_init__(self):
        self.deductions.sec80c = self._normalize(
            self.deductions.sec80c,
            self.DEDUCTIONS.sec80c
        )
        self.deductions.sec80d = self._normalize(
            self.deductions.sec80d,
            self.DEDUCTIONS.sec80d
        )
        self.deductions.sec24b = self._normalize(
            self.deductions.sec24b,
            self.DEDUCTIONS.sec24b
        )

    def _normalize(self, value: int, limit: int) -> int:
        return limit if value > limit else value

    def _slab_rate(
        self, income: int, percent: float, lower: int, upper: int = 0
    ) -> int:
        up = upper if upper and income >= upper else income
        taxable = up - lower
        return percentage(taxable, percent)

    def taxable_income(self) -> int:
        return self.gross_income - self.total_deductions()

    def total_deductions(self) -> int:
        return sum([v for _, v in self.deductions.__dict__.items()])

    def slab_tax(self) -> int:
        tax = 0
        income = self.taxable_income()
        for s in self.SLABS:
            tax += self._slab_rate(income, s.percent, s.lower, s.upper)
            if s.upper and income <= s.upper:
                return tax
        return tax

    def income_tax(self) -> int:
        tax = self.slab_tax()
        return tax if tax > 0 else 0

    def cess(self) -> int:
        return percentage(self.income_tax(), 4)

    @property
    def total_tax(self) -> int:
        return self.income_tax() + self.cess()

    def _deduction_str(self, label: str, val: int, limit: int) -> str:
        _v = " (upto " + str(limit) + "):\t" + str(val) if limit else ":\tNA"
        return f'{label}{_v}'

    def tabular(self) -> str:
        slabs = '\n'.join([
            f'({s.lower}-{s.upper if s.upper else "∞"}) '
            f'{"NIL" if not s.percent else "@" + str(s.percent) + "%"}'
            for s in self.SLABS
        ])
        _d80c = self._deduction_str(
            "80C",
            self.deductions.sec80c,
            self.DEDUCTIONS.sec80c
        )
        _d80d = self._deduction_str(
            "80D",
            self.deductions.sec80d,
            self.DEDUCTIONS.sec80d
        )
        _d24b = self._deduction_str(
            "24(b)",
            self.deductions.sec24b,
            self.DEDUCTIONS.sec24b
        )
        deductions = f'{_d80c}\n{_d80d}\n{_d24b}'

        table = Texttable()
        table.add_rows([
            ["Gross Income", f'{self.gross_income}'],
            ["Deductions", f'{deductions}'],
            ["Tax Rate for Slabs", f'{slabs}'],
            ["Income Tax", f'{self.income_tax()}'],
            ["Cess@4%", f'{self.cess()}'],
            ["Total Tax", f'{self.total_tax}']
        ], header=False)
        return f'\n{self.YEAR} Tax Regime:\n{table.draw()}\n'


@attr.s
class Tax2019Regime(Tax):
    YEAR = 2019
    SLABS = [
        Slab(upper=250000, percent=0),
        Slab(lower=250000, upper=500000, percent=5),
        Slab(lower=500000, upper=1000000, percent=20),
        Slab(lower=1000000, percent=30),
    ]
    DEDUCTIONS = Deductions(
        sec80c=150000,
        sec80d=25000,
        sec24b=75000
    )


@attr.s
class Tax2020Regime(Tax):
    YEAR = 2020
    SLABS = [
        Slab(upper=250000, percent=0),
        Slab(lower=250000, upper=500000, percent=5),
        Slab(lower=500000, upper=750000, percent=10),
        Slab(lower=750000, upper=1000000, percent=15),
        Slab(lower=1000000, upper=1250000, percent=20),
        Slab(lower=1250000, upper=1500000, percent=25),
        Slab(lower=1500000, percent=30),
    ]

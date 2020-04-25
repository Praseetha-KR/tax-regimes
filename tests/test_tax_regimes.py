from tax_regimes import __version__, Tax2019Regime, Tax2020Regime
from tax_regimes.tax import Deductions


def test_version():
    assert __version__ == '0.0.1'


def test_tax_regime_should_give_default_values_if_args_not_passed():
    t = Tax2019Regime()
    assert t.gross_income == 0
    assert t.deductions.sec80c == 0
    assert t.deductions.sec80d == 0
    assert t.deductions.sec24b == 0
    assert t.income_tax == 0
    assert t.total_deductions == 0
    assert t.cess == 0
    assert t.total_tax == 0


def test_tax_regime_should_give_no_tax_for_below_lower_bound():
    t = Tax2019Regime(250000)
    assert t.gross_income == 250000
    assert t.total_tax == 0


def test_2019_regime_should_give_calculated_tax_based_on_slabs():
    t = Tax2019Regime(10000000)
    _t = 0
    _t += (5_00_000 - 2_50_000) * 5//100
    _t += (10_00_000 - 5_00_000) * 20//100
    _t += (10000000 - 10_00_000) * 30//100
    _c = _t * 4/100
    assert t.gross_income == 10000000
    assert t.total_deductions == 0
    assert t.income_tax == _t
    assert t.cess == _c
    assert t.total_tax == _t + _c


def test_2020_regime_should_give_calculated_tax_based_on_slabs():
    t = Tax2020Regime(10000000)
    _t = 0
    _t += (500000 - 250000) * 5//100
    _t += (750000 - 500000) * 10//100
    _t += (1000000 - 750000) * 15//100
    _t += (1250000 - 1000000) * 20//100
    _t += (1500000 - 1250000) * 25//100
    _t += (10000000 - 1500000) * 30//100
    _c = _t * 4/100
    assert t.gross_income == 10000000
    assert t.total_deductions == 0
    assert t.income_tax == _t
    assert t.cess == _c
    assert t.total_tax == _t + _c


def test_tax_regime_should_consider_deductions():
    t = Tax2019Regime(
        10000000,
        Deductions(sec80c=10000, sec80d=10000, sec24b=10000)
    )
    _d = 3 * 10000
    _t = 0
    _t += (5_00_000 - 2_50_000) * 5//100
    _t += (10_00_000 - 5_00_000) * 20//100
    _t += ((10000000 - _d) - 10_00_000) * 30//100
    _c = _t * 4/100
    assert t.gross_income == 10000000
    assert t.total_deductions == _d
    assert t.income_tax == _t
    assert t.cess == _c
    assert t.total_tax == _t + _c


def test_tax_regime_should_consider_deductions_below_the_allowed_limits():
    t = Tax2019Regime(
        10000000,
        Deductions(sec80c=1000000, sec80d=1000000, sec24b=1000000)
    )
    _d = 150000 + 25000 + 75000
    _t = 0
    _t += (5_00_000 - 2_50_000) * 5//100
    _t += (10_00_000 - 5_00_000) * 20//100
    _t += ((10000000 - _d) - 10_00_000) * 30//100
    _c = _t * 4/100
    assert t.gross_income == 10000000
    assert t.total_deductions == _d
    assert t.income_tax == _t
    assert t.cess == _c
    assert t.total_tax == _t + _c

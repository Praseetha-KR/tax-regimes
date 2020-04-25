from .tax import Tax2019Regime, Tax2020Regime
from .compare import lowest, lowest_interactive

__version__ = '0.0.1'
__all__ = [
    Tax2019Regime.__name__,
    Tax2020Regime.__name__,
    lowest.__name__,
    lowest_interactive.__name__,
]

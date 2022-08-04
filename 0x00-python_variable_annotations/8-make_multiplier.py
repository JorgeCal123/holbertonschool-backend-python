from typing import Callable
"""takes a float multiplier as argument
returns a function that multiplies a float by multiplier"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that multiplies a float by multiplier"""
    def mul(multiplier2: float) -> float:
        return multiplier * multiplier2
    return mul

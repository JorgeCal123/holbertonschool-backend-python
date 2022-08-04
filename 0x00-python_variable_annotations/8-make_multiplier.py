#!/usr/bin/env python3
"""takes a float multiplier as argument
returns a function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """function that multiplies a float by multiplier"""
    def mul(multiplier2: float) -> float:
        return multiplier * multiplier2
    return mul

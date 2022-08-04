#!/usr/bin/env python3
"""function that takes a string k and an int OR float v as arguments
returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple string k and square of the int/float v"""
    return (k, v ** 2)

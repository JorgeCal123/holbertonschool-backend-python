#!/usr/bin/env python3
"""function’s parameters
return values with the appropriate types"""
from typing import Iterable, Tuple, Sequence, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """return values with the appropriate types"""
    return [(i, len(i)) for i in lst]

#!/usr/bin/env python3
"""which takes a list mxd_lst of integers and floats
returns their sum as a float."""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """returns their sum as a float."""
    return sum(mxd_lst)

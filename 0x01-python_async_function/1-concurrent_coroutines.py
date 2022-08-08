#!/usr/bin/env python3
"""async routine called"""
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """list of all the delays (float values)"""
    i = 0
    list: List[float] = []
    while (i < n):
        value = await (wait_random(max_delay))
        list.append(value)
        i += 1
    list = sorted(list)
    return list

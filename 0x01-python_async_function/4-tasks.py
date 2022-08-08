#!/usr/bin/env python3
"""async routine called"""
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """list of all the delays (float values)"""
    i = 0
    list: List[float] = []
    while (i < n):
        value = await (task_wait_random(max_delay))
        list.append(value)
        i += 1
    list = sorted(list)
    return list

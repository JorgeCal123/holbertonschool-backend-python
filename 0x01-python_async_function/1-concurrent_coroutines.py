#!/usr/bin/env python3
"""async routine called"""
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """list of all the delays (float values)"""
    i = 0
    list = []
    while (i < n):
        value = await (wait_random(max_delay))
        list.append(value)
        i += 1
    return list

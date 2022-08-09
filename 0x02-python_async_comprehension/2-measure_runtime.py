#!/usr/bin/env python3
"""asynchronous coroutine"""
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    async_comprehension four times in parallel.
    Returns: The total runtime.
    """
    inicio = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    fin = time.time()
    return fin - inicio
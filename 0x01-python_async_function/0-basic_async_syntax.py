#!/usr/bin/env python3
"""asynchronous coroutine that takes in an integer argument"""
import random
import asyncio


async def wait_random(max_delay: int = 10):
    """wait_random that waits for a random delay
    between 0 and max_delay"""
    await asyncio.sleep(max_delay)
    return random.uniform(0, max_delay)

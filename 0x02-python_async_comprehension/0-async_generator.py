#!/usr/bin/env python3
"""The coroutine will loop 10 times, each time asynchronously wait 1 second"""
import asyncio
import random
from typing import Float

async def async_generator() -> Float:
    """return random number between 0 and 10"""
    i = 0
    while (i < 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
        i += 1

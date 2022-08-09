#!/usr/bin/env python3
"""The coroutine will collect 10 random numbers using an async
comprehensing ove"""

import asyncio
import random
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers"""
    return [num async for num in async_generator()]

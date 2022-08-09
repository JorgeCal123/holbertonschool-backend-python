import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This is an asynchronous coroutine that takes no
    arguments. The coroutine will execute async_comprehension
    four times in parallel using asyncio.gather.
    Returns:
        The total runtime.
    """
    inicio = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    fin = time.time()
    return inicio - fin
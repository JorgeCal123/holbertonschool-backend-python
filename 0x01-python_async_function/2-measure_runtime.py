#!/usr/bin/env python3
wait_n = __import__('1-concurrent_coroutines').wait_n
import time
import asyncio

def measure_time(n, max_delay):
    inicio = time.time()
    asyncio.run(wait_n(n, max_delay))
    fin = time.time()
    measuretime = (fin - inicio) / n
    return measuretime

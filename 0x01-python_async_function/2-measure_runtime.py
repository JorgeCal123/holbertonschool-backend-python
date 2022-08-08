#!/usr/bin/env python3
""" function that measures the total execution time"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n, max_delay):
    """total_time / n return a float."""
    inicio = time.time()
    asyncio.run(wait_n(n, max_delay))
    fin = time.time()
    measuretime = (fin - inicio) / n
    return measuretime

#!/usr/bin/env python3
"""
Executing multiple coroutines simultaneosly with async
"""
import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for the wait_n function
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n

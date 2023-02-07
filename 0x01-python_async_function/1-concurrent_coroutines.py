#!/usr/bin/env python3
'''
Executing multiple coroutines simultaneosly with async
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    an async routine called wait_n that takes in 2 int arguments
    (in this order): n and max_delay
    wait_random will be spawned n times with the specified max_delay
    Returns the list of all the delays (float values), in ascending order
    """
    delay_times = await asyncio.gather(
        *tuple(map(lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(delay_times)

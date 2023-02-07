#!/usr/bin/env python3
'''
Creating and Executing multiple coroutines simultaneosly with async
'''
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    task_wait_random will be spawned n times with the specified max_delay
    Returns the list of all the delays (float values), in ascending order
    """
    delay_times = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n)))
    )
    return sorted(delay_times)

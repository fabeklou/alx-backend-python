#!/usr/bin/env python3

"""This module contains a function that waits for
a given number of random delays and returns
the sorted list of the delays
"""

import asyncio
from typing import List
import heapq
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a given number of random delays and returns
    the sorted list of the delays.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay time.

    Returns:
        List[float]: A sorted list of the delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    resps = await asyncio.gather(*tasks)

    heapq.heapify(resps)
    return [heapq.heappop(resps) for _ in range(n)]

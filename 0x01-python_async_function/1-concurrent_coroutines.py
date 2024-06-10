#!/usr/bin/env python3

"""
This module contains an asynchronous function that waits for a
given number of random delays and returns the sorted list of the delays.

Functions:
    - wait_n(n: int, max_delay: int) -> List[float]:
    An asynchronous function that takes in the number of delays to wait for
    and the maximum delay time, and returns a sorted list of the delays.
"""

import asyncio
from typing import List
import heapq
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously waits for a given number of random delays and returns
    the sorted list of the delays.

    Args:
        n (int): The number of delays to wait for.
        max_delay (int): The maximum delay time.

    Returns:
        List[float]: A sorted list of the delays.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    resps = await asyncio.gather(*tasks)

    heapq.heapify(resps)
    return [heapq.heappop(resps) for _ in range(n)]

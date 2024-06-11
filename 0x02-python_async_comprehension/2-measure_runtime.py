"""
This module contains a function to measure the runtime
of an asynchronous comprehension.
"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of an asynchronous comprehension.

    Returns:
        The total runtime in seconds (floating-point value).

    """
    tasks = asyncio.gather(*[async_comprehension() for _ in range(4)])
    started_at = time.time()
    await tasks
    ended_at = time.time()
    return ended_at - started_at

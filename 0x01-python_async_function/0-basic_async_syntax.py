#!/usr/bin/env python3

"""
This module contains an asynchronous function that generates
a random delay and waits for that amount of time.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous function that generates a random delay
    and waits for that amount of time.

    Args:
        max_delay (int): The maximum delay in seconds (default is 10).

    Returns:
        float: The generated random delay.

    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

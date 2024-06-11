#!/usr/bin/env python3

"""This module contains an async_generator function
that yields random values
"""

import asyncio
import random


async def async_generator():
    """
    Asynchronous generator that yields random values.

    This generator yields random floating-point values between 0 and 10.
    It uses asyncio.sleep to introduce a delay of 1 second between each yield.

    Yields:
        float: A random floating-point value between 0 and 10.

    """
    for _ in range(10):
        await asyncio.sleep(1)
        random_value: float = random.uniform(0, 10)
        yield random_value

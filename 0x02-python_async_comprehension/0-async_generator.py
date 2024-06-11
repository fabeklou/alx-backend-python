#!/usr/bin/env python3

"""This module contains an async_generator function
that yields random values
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None]:
    """
    Asynchronous generator that yields random values.

    This generator yields random floating-point values
    between 0 and 10.
    It uses asyncio.sleep to introduce a delay of 1 second
    between each yield.

    Yields:
        float: A random floating-point value between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10

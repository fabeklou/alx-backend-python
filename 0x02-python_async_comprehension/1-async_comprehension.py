#!/usr/bin/env python3

"""
This module contains a function for generating a list
of random floats using async comprehension.
"""

from typing import Any, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Generate a list of random floats using async comprehension.

    Returns:
        A list of random floats.
    """
    random_floats: List[float] = [flt async for flt in async_generator()]
    return random_floats

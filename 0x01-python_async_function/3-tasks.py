#!/usr/bin/env python3

"""This module contains a function that creates and returns
an asyncio task that calls the wait_random function.
"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio task that calls the
    wait_random function.

    Args:
        max_delay (int): The maximum delay for the
            wait_random function.

    Returns:
        asyncio.Task: An asyncio task that calls the
            wait_random function.
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task

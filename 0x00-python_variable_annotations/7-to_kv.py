#!/usr/bin/env python3

"""This module contains a to_kv function that
takes a str and a Union[int, float] and returns
a Tuple[str, float] as argument
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes a str and a Union[int, float] and returns
    a Tuple[str, float] as argument

    Args:
        k (str): the string argument
        v (Union[int, float]): the numeric argument

    Returns:
        Tuple[str, float]: the result made of the given string
            and the numeric argument raised to the power of 2
    """
    return k, v**2

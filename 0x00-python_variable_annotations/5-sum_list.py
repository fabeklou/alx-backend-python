#!/usr/bin/env python3

"""This module contains a sum_list  function which
takes a List[float] as argument and
returns their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a List[float] as argument and
    returns their sum as a float

    Args:
        input_list (List[float]): the list of floats
            to sum

    Returns:
        float: sum of floating point numbers in the
            the given list
    """
    return sum(input_list)

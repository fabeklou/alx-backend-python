#!/usr/bin/env python3

"""This module contains a sum_mixed_list function
that takes a List[Union[int, float]] and returns
their sum as a float
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """takes a List[Union[int, float]] and returns
    their sum as a float

    Args:
        mxd_lst (List[Union[float, int]]): the mixed list
            and integer and floating point number to sum

    Returns:
        float: sum of all numbers in the given mixed list
    """
    return sum(mxd_lst)

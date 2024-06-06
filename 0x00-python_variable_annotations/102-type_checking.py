#!/usr/bin/env python3

"""This module contains a zoom_array function
that receives a Tuple and returns a list which is
factor time larger than the Tuple"
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """receives a Tuple and returns a list which is
    factor time larger than the Tuple

    Args:
        lst (Tuple): the Tuple to enlarge
        factor (int, optional): the factor. Defaults to 2.

    Returns:
        List: the List generated from the given Tuple
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)
zoom_2x: List = zoom_array(array)
zoom_3x: List = zoom_array(array, 3)

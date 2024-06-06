#!/usr/bin/env python3

"""This module contains a make_multiplier function
that takes a floating-point number and returns
a function that multiplies a float by his argument
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """takes a floating-point number and returns a
    function that multiplies a float by his argument

    Args:
        multiplier (float): the multiplicator

    Returns:
        Collable[float, float]: a referance to the multiplicate
            function
    """

    def multiplicate(number: float) -> float:
        """Takes in a floating-point number, myltiply it
        with multiplier and returns the result as a
        floating-point number

        Args:
            mul (float): the floating-point number to multiply
                multiplier with

        Returns:
            float: the result of the multiplication
        """
        return multiplier * number

    return multiplicate

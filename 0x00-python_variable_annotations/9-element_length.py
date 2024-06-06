#!/usr/bin/env python3

"""This module contains a element_length function that
takes an Iterable sequence and returns a List
of Tuple, made of a Sequance and his length (integer)
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """takes an Iterable sequence and returns a List
    of Tuple, made of a Sequance and his length (integer)

    Args:
        lst (Iterable[Sequence]): the Iterable sequence to process

    Returns:
        List[Tuple[Sequence, int]]: a Tuple made of a Sequance
        and the length (integer) of this sequence
    """
    return [(i, len(i)) for i in lst]

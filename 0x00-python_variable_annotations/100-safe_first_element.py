#!/usr/bin/env python3

"""This module contains a safe_first_element function
that receives a Sequence Object and returns either
the first member or None
"""

from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """receives a Sequence and returns his first
    member or None if its empty

    Args:
        lst (Sequence): the Sequence, possibly a List/Tuple

    Returns:
        Any: the first member of the Sequence or
            None if it is empty

    """
    if lst:
        return lst[0]
    else:
        return None

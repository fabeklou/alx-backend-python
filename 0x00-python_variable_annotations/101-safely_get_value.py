#!/usr/bin/env python3

"""This module contains a safely_get_value function
that returns the value associeted to a key in a
dictionary if it exists, a default value otherwise
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """returns the value associeted to a key in a
    dictionary if it exists, a default value otherwise

    Args:
        dct (Mapping): The Map Object
        key (Any): The key to get in the Map Object
        default (Union[T, None], optional): The deault vlaue
            to return if the key is not in dct. Defaults to None.

    Returns:
        Union[Any, T]: The value associeted with the key (Any) or
            The default value (T)
    """
    if key in dct:
        return dct[key]
    else:
        return default

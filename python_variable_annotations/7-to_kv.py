#!/usr/bin/env python3
"""
Module 7-to_kv
Provides a function to return a tuple with a string and
the square of an int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Returns a tuple with the string and the square of the int or float
    as a float.

    Args:
        k (str): The key string.
        v (Union[int, float]): A number to be squared.

    Returns:
        Tuple[str, float]: A tuple where the first element is the string and
        the second is v squared.
    """
    return (k, float(v ** 2))

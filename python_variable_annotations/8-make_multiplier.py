#!/usr/bin/env python3
"""
Module 8-make_multiplier
Provides a function that returns a multiplier function using type annotations.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The multiplier value.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of the multiplication.
    """
    return lambda x: x

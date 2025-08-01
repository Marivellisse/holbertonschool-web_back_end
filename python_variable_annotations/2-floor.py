#!/usr/bin/env python3
"""
Module 2-floor
Provides a function to compute the floor of a float with type annotations.
"""

import math


def floor(n: float) -> int:
    """
    Returns the floor of a floating-point number.

    Args:
        n (float): A floating-point number.

    Returns:
        int: The largest integer less than or equal to n.
    """
    return math.floor(n)

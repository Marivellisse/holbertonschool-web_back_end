#!/usr/bin/env python3
"""
Module 5-sum_list
Provides a function to sum a list of floats using type annotations.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Returns the sum of a list of floating-point numbers.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The total sum of all numbers in the list.
    """
    return sum(input_list)

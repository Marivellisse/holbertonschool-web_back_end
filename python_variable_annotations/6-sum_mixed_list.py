#!/usr/bin/env python3
"""
Module 6-sum_mixed_list
Provides a function to sum a list of integers and floats
using type annotations.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Returns the sum of a list containing integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
        float: The total sum as a float.
    """
    return sum(mxd_lst)

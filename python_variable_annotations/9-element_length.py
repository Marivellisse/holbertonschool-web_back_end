#!/usr/bin/env python3
"""
Module 9-element_length
Provides a function that returns a list of tuples with each element
and its length.
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Returns a list of tuples, each containing an element and its length.

    Args:
        lst (Iterable[Sequence]): An iterable containing sequence-like
        elements (e.g., str, list, tuple).

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples with each element and
        its length.
    """
    return [(i, len(i)) for i in lst]

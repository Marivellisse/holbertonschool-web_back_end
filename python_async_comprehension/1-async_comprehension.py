#!/usr/bin/env python3
"""
Module 1-async_comprehension
Defines a coroutine that collects 10 random numbers from an async generator.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers from async_generator using async comprehension.

    Returns:
        List[float]: A list containing 10 random float values between 0 and 10.
    """
    return [i async for i in async_generator()]

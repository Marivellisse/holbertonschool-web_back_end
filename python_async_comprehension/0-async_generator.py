#!/usr/bin/env python3
"""
Module 0-async_generator
Defines an asynchronous generator that yields random floats from 0 to 10.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Loops 10 times, waiting 1 second each time, and yields
    a random float between 0 and 10.

    Returns:
        AsyncGenerator[float, None]: An asynchronous generator yielding floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

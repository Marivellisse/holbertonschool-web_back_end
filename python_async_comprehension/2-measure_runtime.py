#!/usr/bin/env python3
"""
Module 2-measure_runtime
Measures the total runtime of executing async_comprehension
four times in parallel using asyncio.gather.
"""

import asyncio
import time
from typing import Callable
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of running async_comprehension 4 times in parallel.

    Returns:
        float: Total time taken to run all comprehensions concurrently.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time

#!/usr/bin/env python3
"""
Module 2-measure_runtime
Measures the average runtime of executing wait_n asynchronously.
"""

import time
import asyncio
from typing import Callable
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time of wait_n(n, max_delay).

    Args:
        n (int): Number of coroutines.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average time per coroutine.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    return total_time / n

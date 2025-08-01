#!/usr/bin/env python3
"""
Module 4-tasks
Executes multiple asyncio tasks using task_wait_random
and returns a list of delays in ascending order.
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns n tasks using task_wait_random and returns a list of the delays
    in ascending order.

    Args:
        n (int): Number of tasks to spawn.
        max_delay (int): Maximum delay for each task.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays: List[float] = []
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays

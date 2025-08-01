#!/usr/bin/env python3
"""
Module 3-tasks
Provides a function that returns an asyncio.Task
for executing an asynchronous coroutine.
"""

import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: A coroutine task that will wait for a random delay.
    """
    return asyncio.create_task(wait_random(max_delay))

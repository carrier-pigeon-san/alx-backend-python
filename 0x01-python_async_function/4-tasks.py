#!/usr/bin/env python3
"""This module contsins a function task_wait_n that takes an integer max_delay
and returns a asyncio.Task."""

import asyncio
import random
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """This function waits for a random number of seconds and returns it."""
    delays = [task_wait_random(max_delay) for _ in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]

#!/usr/bin/env python3
"""This module contains the coroutine measure_runtime."""
import asyncio
import time
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This coroutine will measure the runtime of async_comprehension."""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end = time.time()
    return end - start

#!/usr/bin/env python3
"""This module contsins an async function measure_time that measures the total
execution time for wait_n(n, max_delay), and returns total_time / n."""

import asyncio
import random
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 10, max_delay: int = 0) -> float:
    """
    This function measures the total execution time for wait_n(n, max_delay),
    and returns total_time / n."""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n

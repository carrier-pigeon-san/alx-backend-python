#!/usr/bin/env python3
"""This module contsins an async routine wait_n that takes in 2 int arguments
(n and max_delay) and returns a list of delays in ascending order."""

import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """This function waits for a random number of seconds and returns it."""
    delays = [wait_random(max_delay) for i in range(n)]
    return [await delay for delay in asyncio.as_completed(delays)]

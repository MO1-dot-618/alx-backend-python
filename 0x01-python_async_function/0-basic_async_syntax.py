#!/usr/bin/env python3
"""
0-basic_async_syntax.py
"""

import asyncio
import random


async def wait_random(max_delay: float = 10.0) -> float:
    """
    functions that waits a random delay and returns it
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

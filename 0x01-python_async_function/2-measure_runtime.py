#!/usr/bin/env python3
"""
2-measure_runtime.py
"""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """
    functions that measures the time of wait_n
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return ((end - start) / n)

#!/usr/bin/env python3
""" Modify Execute multiple coroutines at the same time """
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Execute multiple coroutines """
    results = []
    delays = [task_wait_random(max_delay) for i in range(n)]
    for val in asyncio.as_completed(delays):
        value.append(await res)
    return value

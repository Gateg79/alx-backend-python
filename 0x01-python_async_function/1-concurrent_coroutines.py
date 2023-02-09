#!/usr/bin/env python3
'''Executes multiple coroutines at the same time with async
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Executes wait_random n times with max_delay
    '''
    wait_times = await asyncio.gather(
            *tuple(map(Lambda _: wait_random(max_delay), range(n)))
    )
    return sorted(wait_times)

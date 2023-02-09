#!/usr/bin/env python3
'''asynchronous coroutine that takes in an integer
argument named wait_random
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Waits for a random number of seconds and returns it
    '''
    delay_time = random.random() * max_delay
    await asyncio.sleep(delay_time)
    return delay_time

#!/usr/bin/env python3
import random
import asyncio
'''Basic of async'''


async def wait_random(max_delay=10):
    '''random delay
    '''
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

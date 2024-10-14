#!/usr/bin/env python3
'''Basic of async'''
import random
import asyncio


async def wait_random(max_delay=10):
    '''random delay
    '''
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay

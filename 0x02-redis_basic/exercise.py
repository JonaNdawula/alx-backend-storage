#!/usr/bin/env python3
"""
This module contains redis db
"""
import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        random_key = str(uuid.uuid4())
        if isinstance(data, str):
            data = data.encode('utf-8')
        elif isinstance(data, int) or isinstance(data, float):
            data = str(data).encode('utf-8')
        self._redis.set(random_key, data)
        return random_key
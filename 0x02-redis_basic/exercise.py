#!/usr/bin/env python3
"""
Writing strings to Redis
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    a Cache class.
    """
    def __init__(self):
        """
        In the __init__ method, store an instance of the
        Redis client as a private variable named _redis (using redis.Redis())
        and flush the instance using flushdb.
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method that takes a data argument and returns a string.
        The method generate a random key (e.g. using uuid),
        store the input data in Redis using the random key and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
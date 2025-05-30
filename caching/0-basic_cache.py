#!/usr/bin/python3
"""BasicCache module"""
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """A basic cache with no limit"""

    def put(self, key, item):
        """Store item in the cache"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from cache"""
        return self.cache_data.get(key, None)

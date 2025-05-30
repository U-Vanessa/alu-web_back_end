#!/usr/bin/python3
"""LIFOCache module"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """Last-In First-Out Cache"""

    def __init__(self):
        """Initialize the LIFO cache"""
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    last = self.stack.pop()
                    del self.cache_data[last]
                    print("DISCARD:", last)
            else:
                self.stack.remove(key)
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key"""
        return self.cache_data.get(key, None)

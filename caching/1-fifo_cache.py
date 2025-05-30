#!/usr/bin/python3
"""FIFOCache module"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """First-In First-Out Cache"""

    def __init__(self):
        """Initialize the FIFO cache"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    oldest = self.queue.pop(0)
                    del self.cache_data[oldest]
                    print("DISCARD:", oldest)
                self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item by key"""
        return self.cache_data.get(key, None)

<<<<<<< HEAD
#!/usr/bin/env python3
"""LIFO Caching"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """LIFO cache"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                discard = next(reversed(list(self.cache_data)))
                print("DISCARD: {}".format(discard))
                del self.cache_data[discard]
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
=======
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
>>>>>>> be86c4174cc7bf624a1bbf333f2c36b667525ed0

<<<<<<< HEAD
#!/usr/bin/env python3
"""Basic cache"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache class"""

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
=======
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
>>>>>>> be86c4174cc7bf624a1bbf333f2c36b667525ed0

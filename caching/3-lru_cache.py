#!/usr/bin/python3
"""LRUCache module"""
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """Least Recently Used (LRU) cache system"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.use_order = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.use_order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.use_order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

        self.cache_data[key] = item
        self.use_order.append(key)

    def get(self, key):
        """Get item by key"""
        if key is None or key not in self.cache_data:
            return None

        self.use_order.remove(key)
        self.use_order.append(key)
        return self.cache_data[key]

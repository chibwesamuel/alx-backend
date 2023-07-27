#!/usr/bin/env python3
"""
LRUCache module
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize LRUCache."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache using LRU replacement policy.

        Args:
            key (any): The key to store the item.
            item (any): The item to be stored.

        Note:
            If either key or item is None, this method does nothing.
            If the number of items in self.cache_data is higher than
            BaseCaching.MAX_ITEMS, the least recently used item
            (LRU algorithm) is discarded, and the new item is added
            to the end of the queue.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.queue.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lru_key = self.queue.pop(0)
                self.cache_data.pop(lru_key)
                print("DISCARD:", lru_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an item from the cache by key.

        Args:
            key (any): The key to retrieve the item.

        Returns:
            any: The value associated with the key, or None if the
            key doesn't exist in the cache.
        """
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data.get(key)
        return None

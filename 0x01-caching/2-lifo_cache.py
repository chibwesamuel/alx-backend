#!/usr/bin/env python3
"""
LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize LIFOCache."""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache using LIFO replacement policy.

        Args:
            key (any): The key to store the item.
            item (any): The item to be stored.

        Note:
            If either key or item is None, this method does nothing.
            If the number of items in self.cache_data is higher than
            BaseCaching.MAX_ITEMS, the last item put in cache is
            discarded (LIFO algorithm).
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                last_key = self.queue.pop()
                self.cache_data.pop(last_key)
                print("DISCARD:", last_key)
            self.cache_data[key] = item
            self.queue.append(key)

    def get(self, key):
        """Get an item from the cache by key.

        Args:
            key (any): The key to retrieve the item.

        Returns:
            any: The value associated with the key, or None if the key
            doesn't exist in the cache.
        """
        return self.cache_data.get(key)

#!/usr/bin/env python3
"""
LFUCache module
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache class that inherits from BaseCaching."""

    def __init__(self):
        """Initialize LFUCache."""
        super().__init__()
        self.frequency = {}
        self.min_frequency = 0

    def put(self, key, item):
        """Add an item to the cache using LFU replacement policy.

        Args:
            key (any): The key to store the item.
            item (any): The item to be stored.

        Note:
            If either key or item is None, this method does nothing.
            If the number of items in self.cache_data is higher than
            BaseCaching.MAX_ITEMS, the least frequency used item
            (LFU algorithm) is discarded. If there are more than one
            item with the same least frequency, the least recently
            used item among them is discarded.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    lfu_keys = [k for k in self.frequency
                            if self.frequency[k] == self.min_frequency] \
                    lru_key = min(self.cache_data, key=lambda \
                            k: self.frequency[k])
                    if len(lfu_keys) > 1:
                        lru_key = min(lfu_keys, key=lambda \
                                k: self.cache_data[k])
                    self.cache_data.pop(lru_key)
                    self.frequency.pop(lru_key)
                    print("DISCARD:", lru_key)

                self.cache_data[key] = item
                self.frequency[key] = 1
                self.min_frequency = 1

    def get(self, key):
        """Get an item from the cache by key.

        Args:
            key (any): The key to retrieve the item.

        Returns:
            any: The value associated with the key, or None if the
            key doesn't exist in the cache.
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data.get(key)
        return None
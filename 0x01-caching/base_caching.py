#!/usr/bin/env python3
"""
BasicCache module
"""

from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """BasicCache class that inherits from BaseCaching."""

    def put(self, key, item):
        """Add an item to the cache.

        Args:
            key: The key to store the item.
            item: The item to be stored.

        Note:
            If key or item is None, this method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache by key.

        Args:
            key: The key to retrieve the item.

        Returns:
            The value associated with the key, or None if the key doesn't exist
            in the cache.
        """
        return self.cache_data.get(key)


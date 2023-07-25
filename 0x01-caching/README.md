---

## Title: Caching

This repository contains Python classes for different caching algorithms that inherit from the `BaseCaching` class.

### Task 0: BasicCache

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system with no limit on the number of items it can store. It implements the `put` and `get` methods to add and retrieve items from the cache.

### Task 1: FIFOCache

Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system that uses the First-In-First-Out (FIFO) replacement policy. If the number of items exceeds `BaseCaching.MAX_ITEMS`, it discards the first item that was put in the cache.

### Task 2: LIFOCache

Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system that uses the Last-In-First-Out (LIFO) replacement policy. If the number of items exceeds `BaseCaching.MAX_ITEMS`, it discards the last item that was put in the cache.

### Task 3: LRUCache

Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system that uses the Least Recently Used (LRU) replacement policy. If the number of items exceeds `BaseCaching.MAX_ITEMS`, it discards the least recently used item.

### Task 4: MRUCache

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system that uses the Most Recently Used (MRU) replacement policy. If the number of items exceeds `BaseCaching.MAX_ITEMS`, it discards the most recently used item.

### Task 5: LFUCache

Create a class `LFUCache` that inherits from `BaseCaching` and is a caching system that uses the Least Frequently Used (LFU) replacement policy. If the number of items exceeds `BaseCaching.MAX_ITEMS`, it discards the least frequently used item. If there are multiple items with the same least frequency, it uses the LRU algorithm to discard the least recently used item among them.

Each class in this repository implements the `put` and `get` methods, allowing items to be added and retrieved from the cache according to the respective replacement policy.

---

Repo:

- GitHub repository: alx-backend
- Directory: 0x01-caching

Files:

- 0-basic_cache.py
- 1-fifo_cache.py
- 2-lifo_cache.py
- 3-lru_cache.py
- 4-mru_cache.py
- 100-lfu_cache.py (Advanced)

from lru import LRUCache

class Cache:
    def __init__(self, capacity):
        self.cache = LRUCache(capacity)

    def get(self, key):
        return self.cache.get(key)

    def put(self, key, value):
        self.cache.put(key, value)

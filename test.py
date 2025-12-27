from cache import Cache

cache = Cache(2)

cache.put("a", 1)
cache.put("b", 2)
print(cache.get("a"))  # 1

cache.put("c", 3)  # evicts b
print(cache.get("b"))  # None

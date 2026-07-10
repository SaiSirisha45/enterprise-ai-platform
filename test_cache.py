from backend.cache.cache_manager import cache

cache.set("hello", {"message": "Enterprise AI"})

print(cache.get("hello")) 
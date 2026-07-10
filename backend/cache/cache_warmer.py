from backend.cache.cache_manager import cache


def warm_cache():

    cache.set(
        "system_status",
        "ready",
        ttl=86400
    )

    cache.set(
        "version",
        "Enterprise AI v1",
        ttl=86400
    )

    print("Cache Warmed Successfully") 
from backend.cache.cache_manager import cache


class EmbeddingCache:

    PREFIX = "embedding:"

    @staticmethod
    def get(text: str):

        return cache.get(
            EmbeddingCache.PREFIX + text
        )

    @staticmethod
    def save(
        text: str,
        embedding,
        ttl=86400
    ):

        cache.set(
            EmbeddingCache.PREFIX + text,
            embedding,
            ttl
        )


embedding_cache = EmbeddingCache() 
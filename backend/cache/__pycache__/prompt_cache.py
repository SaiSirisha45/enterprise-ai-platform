from backend.cache.cache_manager import cache


class PromptCache:

    PREFIX = "prompt:"

    def get(self, name):

        return cache.get(
            self.PREFIX + name
        )

    def save(
        self,
        name,
        prompt,
        ttl=86400
    ):

        cache.set(
            self.PREFIX + name,
            prompt,
            ttl
        )


prompt_cache = PromptCache() 
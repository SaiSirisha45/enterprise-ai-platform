from backend.cache.cache_manager import cache


class DocumentCache:

    PREFIX = "document:"

    def get(self, doc_id):

        return cache.get(
            self.PREFIX + str(doc_id)
        )

    def save(
        self,
        doc_id,
        document,
        ttl=3600
    ):

        cache.set(
            self.PREFIX + str(doc_id),
            document,
            ttl
        )


document_cache = DocumentCache() 
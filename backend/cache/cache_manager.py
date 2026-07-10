"""
Enterprise AI Platform
Redis Cache Manager
"""

import json
import redis
from typing import Any, Optional


class CacheManager:
    def __init__(
        self,
        host: str = "localhost",
        port: int = 6379,
        db: int = 0,
    ):
        self.redis = redis.Redis(
            host=host,
            port=port,
            db=db,
            decode_responses=True,
        )

    # -------------------------
    # Generic Cache Operations
    # -------------------------

    def set(
        self,
        key: str,
        value: Any,
        ttl: int = 3600,
    ):

        self.redis.set(
            key,
            json.dumps(value),
            ex=ttl,
        )

    def get(
        self,
        key: str,
    ) -> Optional[Any]:

        data = self.redis.get(key)

        if data is None:
            return None

        return json.loads(data)

    def delete(self, key: str):
        self.redis.delete(key)

    def exists(self, key: str):
        return self.redis.exists(key)

    def clear(self):
        self.redis.flushdb()

    # -------------------------
    # Enterprise Cache Helpers
    # -------------------------

    def cache_session(
        self,
        user_id,
        session,
        ttl=3600,
    ):
        self.set(
            f"session:{user_id}",
            session,
            ttl,
        )

    def get_session(self, user_id):
        return self.get(
            f"session:{user_id}"
        )

    def cache_user_profile(
        self,
        user_id,
        profile,
        ttl=1800,
    ):
        self.set(
            f"user:{user_id}",
            profile,
            ttl,
        )

    def get_user_profile(self, user_id):
        return self.get(
            f"user:{user_id}"
        )

    def cache_chat_history(
        self,
        user_id,
        history,
        ttl=86400,
    ):
        self.set(
            f"chat:{user_id}",
            history,
            ttl,
        )

    def get_chat_history(self, user_id):
        return self.get(
            f"chat:{user_id}"
        )

    def cache_embeddings(
        self,
        key,
        embedding,
        ttl=86400,
    ):
        self.set(
            f"embedding:{key}",
            embedding,
            ttl,
        )

    def get_embedding(self, key):
        return self.get(
            f"embedding:{key}"
        )

    def cache_rag_result(
        self,
        query,
        result,
        ttl=3600,
    ):
        self.set(
            f"rag:{query}",
            result,
            ttl,
        )

    def get_rag_result(self, query):
        return self.get(
            f"rag:{query}"
        )

    def cache_prompt(
        self,
        name,
        prompt,
        ttl=86400,
    ):
        self.set(
            f"prompt:{name}",
            prompt,
            ttl,
        )

    def get_prompt(self, name):
        return self.get(
            f"prompt:{name}"
        )

    def cache_document(
        self,
        doc_id,
        document,
        ttl=86400,
    ):
        self.set(
            f"document:{doc_id}",
            document,
            ttl,
        )

    def get_document(self, doc_id):
        return self.get(
            f"document:{doc_id}"
        )


cache = CacheManager() 
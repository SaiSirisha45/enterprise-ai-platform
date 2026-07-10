from fastapi import APIRouter
from pydantic import BaseModel

from backend.rag.embedding_service import EmbeddingService
from backend.rag.vector_store import search_documents

router = APIRouter(
    prefix="/retrieve",
    tags=["Semantic Retrieval"]
)

embedding_service = EmbeddingService()


class RetrievalRequest(BaseModel):
    query: str
    department: str
    top_k: int = 5


@router.post("/")
def retrieve_documents(request: RetrievalRequest):

    query_embedding = embedding_service.generate_embedding(
        request.query
    )

    results = search_documents(
        department=request.department,
        query_embedding=query_embedding["vector"],
        top_k=request.top_k
    )

    return {
        "documents": results.get("documents", []),
        "similarity_score": results.get("distances", []),
        "sources": results.get("metadatas", [])
    }
from fastapi import APIRouter, UploadFile, File

from backend.cache.cache_manager import cache
from backend.performance.api_profiler import profiler

router = APIRouter(
    prefix="/knowledge",
    tags=["Knowledge"]
)

documents = [
    {
        "id": "1",
        "title": "Enterprise AI Guide"
    },
    {
        "id": "2",
        "title": "RAG Documentation"
    }
]


# ==========================================================
# Get Documents
# ==========================================================

@router.get("/")
@profiler.profile
def get_documents():

    cached_docs = cache.get("documents")

    if cached_docs:
        return {
            "source": "redis",
            "documents": cached_docs
        }

    cache.set(
        "documents",
        documents,
        ttl=3600
    )

    return {
        "source": "memory",
        "documents": documents
    }


# ==========================================================
# Upload Document
# ==========================================================

@router.post("/upload")
@profiler.profile
async def upload_document(file: UploadFile = File(...)):

    new_doc = {
        "id": str(len(documents) + 1),
        "title": file.filename
    }

    documents.append(new_doc)

    # Refresh cache
    cache.set(
        "documents",
        documents,
        ttl=3600
    )

    return {
        "message": f"{file.filename} uploaded successfully",
        "cached": True
    }


# ==========================================================
# Delete Document
# ==========================================================

@router.delete("/{id}")
@profiler.profile
def delete_document(id: str):

    global documents

    documents = [
        doc for doc in documents
        if doc["id"] != id
    ]

    # Refresh cache
    cache.set(
        "documents",
        documents,
        ttl=3600
    )

    return {
        "message": f"Document {id} deleted",
        "cached": True
    } 
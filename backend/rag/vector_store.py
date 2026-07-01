import chromadb

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CHROMA_PATH = os.path.join(BASE_DIR, "storage", "chroma_db")

client = chromadb.PersistentClient(path=CHROMA_PATH)

COLLECTIONS = [
    "hr_docs",
    "payroll_docs",
    "projects_docs",
    "engineering_docs",
    "support_docs"
]


def get_collection(department: str):
    if department not in COLLECTIONS:
        raise ValueError("Invalid collection name")

    return client.get_or_create_collection(name=department)


def insert_document(
    department: str,
    document_id: str,
    chunk_id: str,
    chunk_text: str,
    embedding: list,
    metadata: dict
):
    collection = get_collection(department)

    collection.add(
        ids=[chunk_id],
        documents=[chunk_text],
        embeddings=[embedding],
        metadatas=[metadata]
    )

    return {
        "message": "Inserted into vector store",
        "collection": department,
        "document_id": document_id,
        "chunk_id": chunk_id
    }


def search_documents(
    department: str,
    query_embedding: list,
    top_k: int = 5,
    metadata_filter: dict | None = None
):
    collection = get_collection(department)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k,
        where=metadata_filter
    )

    return results


def update_document(
    department: str,
    chunk_id: str,
    chunk_text: str,
    embedding: list,
    metadata: dict
):
    collection = get_collection(department)

    collection.update(
        ids=[chunk_id],
        documents=[chunk_text],
        embeddings=[embedding],
        metadatas=[metadata]
    )

    return {
        "message": "Updated vector record",
        "chunk_id": chunk_id
    }


def delete_document(department: str, chunk_id: str):
    collection = get_collection(department)

    collection.delete(ids=[chunk_id])

    return {
        "message": "Deleted from vector store",
        "chunk_id": chunk_id
    }
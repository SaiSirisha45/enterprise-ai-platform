from fastapi import APIRouter, Query
from typing import Optional

router = APIRouter(
    prefix="/documents",
    tags=["Knowledge Base"]
)

documents = [
    {
        "id": 1,
        "title": "Leave Policy",
        "department": "HR",
        "owner": "Admin",
        "status": "Approved"
    },
    {
        "id": 2,
        "title": "Payroll Guide",
        "department": "Payroll",
        "owner": "Finance",
        "status": "Pending"
    }
]


@router.get("/")
def get_documents(
    department: Optional[str] = None,
    owner: Optional[str] = None,
    status: Optional[str] = None,
    page: int = Query(1, ge=1),
    size: int = Query(10, ge=1)
):
    result = documents

    if department:
        result = [
            d for d in result
            if d["department"] == department
        ]

    if owner:
        result = [
            d for d in result
            if d["owner"] == owner
        ]

    if status:
        result = [
            d for d in result
            if d["status"] == status
        ]

    start = (page - 1) * size
    end = start + size

    return result[start:end]


@router.get("/{doc_id}")
def get_document(doc_id: int):
    for doc in documents:
        if doc["id"] == doc_id:
            return doc

    return {"error": "Document not found"}


@router.put("/{doc_id}")
def update_document(doc_id: int, updated_doc: dict):
    for doc in documents:
        if doc["id"] == doc_id:
            doc.update(updated_doc)
            return {
                "message": "Updated",
                "document": doc
            }

    return {"error": "Document not found"}


@router.delete("/{doc_id}")
def delete_document(doc_id: int):
    global documents

    documents = [
        d for d in documents
        if d["id"] != doc_id
    ]

    return {"message": "Deleted"}


@router.post("/search")
def search_documents(query: dict):
    keyword = query.get("keyword", "").lower()

    results = [
        d for d in documents
        if keyword in d["title"].lower()
    ]

    return results
from fastapi import APIRouter
from backend.rag.vector_store import COLLECTIONS, get_collection

router = APIRouter(
    prefix="/departments",
    tags=["Department Collections"]
)

@router.get("/collections")
def list_department_collections():
    return {"collections": COLLECTIONS}

@router.post("/collections/{department}")
def create_department_collection(department: str):
    collection = get_collection(department)
    return {
        "message": "Department collection ready",
        "department": department,
        "collection": collection.name
    }
import os
import shutil
from datetime import datetime, timedelta

from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from backend.rag.document_processor import process_document
from backend.rag.embedding_service import EmbeddingService
from backend.rag.vector_store import insert_document

embedding_service = EmbeddingService()

router = APIRouter(
    prefix="/knowledge-center",
    tags=["Enterprise Knowledge Center"]
)

UPLOAD_DIR = "storage/documents"

documents = []
approval_queue = []


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    department: str = Form(...),
    owner: str = Form(...),
    expiry_days: int = Form(365)
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    if not file.filename:
        raise HTTPException(
            status_code=400,
            detail="File is required"
        )

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    processed_result = process_document(
        file_path=file_path,
        chunk_size=500,
        overlap=50
    )

    chunks = processed_result["chunks"]

    embedded_chunks = []

    for chunk in chunks:
        embedding = embedding_service.generate_embedding(
            chunk["chunk_text"]
        )

        chunk_id = f"{file.filename}_chunk_{chunk['chunk_number']}"

        insert_document(
            department=department,
            document_id=file.filename,
            chunk_id=chunk_id,
            chunk_text=chunk["chunk_text"],
            embedding=embedding["vector"],
            metadata={
                "file_name": file.filename,
                "department": department,
                "owner": owner,
                "status": "Pending Approval",
                "chunk_number": chunk["chunk_number"]
            }
        )

        embedded_chunks.append({
            "chunk_number": chunk["chunk_number"],
            "chunk_id": chunk_id,
            "embedding_id": embedding["embedding_id"],
            "model_used": embedding["model_used"],
            "vector_dimension": embedding["vector_dimension"],
            "processing_time": embedding["processing_time"]
        })

    document = {
        "file_name": file.filename,
        "department": department,
        "owner": owner,
        "status": "Pending Approval",
        "uploaded_at": datetime.now().isoformat(),
        "expires_at": (datetime.now() + timedelta(days=expiry_days)).isoformat(),
        "path": file_path,
        "total_chunks": len(chunks),
        "embedded_chunks": embedded_chunks
    }

    documents.append(document)
    approval_queue.append(document)

    return {
        "message": "Document uploaded and embedded successfully",
        "document": document
    }


@router.get("/approval-queue")
def get_approval_queue():
    return {
        "pending_documents": approval_queue
    }


@router.post("/approve/{file_name}")
def approve_document(file_name: str):
    for doc in approval_queue:
        if doc["file_name"] == file_name:
            doc["status"] = "Approved"
            approval_queue.remove(doc)

            return {
                "message": "Document approved",
                "document": doc
            }

    return {
        "error": "Document not found in approval queue"
    }


@router.get("/expired-documents")
def expired_documents():
    now = datetime.now()

    expired = [
        doc for doc in documents
        if datetime.fromisoformat(doc["expires_at"]) < now
    ]

    return {
        "expired_documents": expired
    }
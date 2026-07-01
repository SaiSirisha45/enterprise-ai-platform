import os
import shutil
import hashlib
from fastapi import APIRouter, UploadFile, File, HTTPException, Form

router = APIRouter(prefix="/documents", tags=["Document Upload"])

UPLOAD_DIR = "storage/documents"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

ALLOWED_EXTENSIONS = {
    ".pdf": "application/pdf",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    ".txt": "text/plain",
    ".md": "text/markdown",
    ".markdown": "text/markdown"
}

uploaded_hashes = set()


def calculate_file_hash(file_path: str):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for block in iter(lambda: file.read(4096), b""):
            sha256.update(block)

    return sha256.hexdigest()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    department: str = Form(...),
    owner: str = Form(...)
):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    file_ext = os.path.splitext(file.filename)[1].lower()

    if file_ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type"
        )

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file_size = os.path.getsize(file_path)

    if file_size > MAX_FILE_SIZE:
        os.remove(file_path)
        raise HTTPException(
            status_code=400,
            detail="File size exceeds 10 MB limit"
        )

    file_hash = calculate_file_hash(file_path)

    if file_hash in uploaded_hashes:
        os.remove(file_path)
        raise HTTPException(
            status_code=409,
            detail="Duplicate document detected"
        )

    uploaded_hashes.add(file_hash)

    return {
        "message": "Document uploaded successfully",
        "file_name": file.filename,
        "file_type": file_ext,
        "department": department,
        "owner": owner,
        "file_size": file_size,
        "file_hash": file_hash,
        "storage_path": file_path
    }
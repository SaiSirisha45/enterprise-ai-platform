from fastapi import APIRouter, UploadFile, File

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


@router.get("")
def get_documents():
    return documents


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    return {
        "message": f"{file.filename} uploaded successfully"
    }


@router.delete("/{id}")
def delete_document(id: str):
    return {
        "message": f"Document {id} deleted"
    } 
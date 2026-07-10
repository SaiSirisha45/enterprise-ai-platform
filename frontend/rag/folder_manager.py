import os
import shutil
from fastapi import APIRouter

router = APIRouter(
    prefix="/folders",
    tags=["Folder Management"]
)

BASE_FOLDER = "storage/folders"


@router.post("/create/{folder_name}")
def create_folder(folder_name: str):

    path = os.path.join(BASE_FOLDER, folder_name)

    os.makedirs(path, exist_ok=True)

    return {
        "message": "Folder created successfully",
        "folder": folder_name
    }


@router.get("/")
def list_folders():

    os.makedirs(BASE_FOLDER, exist_ok=True)

    folders = [
        f for f in os.listdir(BASE_FOLDER)
        if os.path.isdir(os.path.join(BASE_FOLDER, f))
    ]

    return {
        "folders": folders
    }


@router.delete("/{folder_name}")
def delete_folder(folder_name: str):

    path = os.path.join(BASE_FOLDER, folder_name)

    if os.path.exists(path):
        shutil.rmtree(path)

        return {
            "message": "Folder deleted",
            "folder": folder_name
        }

    return {
        "error": "Folder not found"
    }
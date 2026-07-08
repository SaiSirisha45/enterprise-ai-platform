from fastapi import APIRouter

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

users = [
    {
        "id": "1",
        "name": "Demo User",
        "email": "demo@gmail.com"
    }
]


@router.get("/users")
def get_users():
    return users


@router.post("/users")
def create_user(data: dict):
    users.append(data)
    return data


@router.delete("/users/{id}")
def delete_user(id: str):
    return {
        "message": f"User {id} deleted"
    } 
from fastapi import APIRouter

router = APIRouter(
    prefix="/chat",
    tags=["Chat"]
)

chat_history = [
    {
        "id": 1,
        "role": "assistant",
        "message": "Welcome to Enterprise AI Platform"
    }
]


@router.get("/history")
def get_chat_history():
    return chat_history


@router.post("")
def send_message(data: dict):
    message = data.get("message")

    chat_history.append({
        "id": len(chat_history) + 1,
        "role": "user",
        "message": message
    })

    chat_history.append({
        "id": len(chat_history) + 1,
        "role": "assistant",
        "message": f"You said: {message}"
    })

    return {
        "reply": f"You said: {message}"
    } 
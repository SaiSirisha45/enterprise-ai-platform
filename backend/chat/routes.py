from fastapi import APIRouter

from monitoring.tracing import tracer

from backend.cache.cache_manager import cache
from backend.performance.api_profiler import profiler
from backend.schemas.chat import ChatRequest

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


# ==========================================================
# Get Chat History
# ==========================================================

@router.get("/history")
@profiler.profile
def get_chat_history():

    with tracer.start_as_current_span("Get Chat History"):

        cached_history = cache.get_chat_history("default")

        if cached_history:

            return {
                "source": "redis",
                "history": cached_history
            }

        cache.cache_chat_history(
            "default",
            chat_history,
            ttl=86400
        )

        return {
            "source": "memory",
            "history": chat_history
        }


# ==========================================================
# Send Message
# ==========================================================

@router.post("/")
@profiler.profile
def send_message(data: ChatRequest):

    with tracer.start_as_current_span("Chat Request") as span:

        message = data.message

        span.set_attribute(
            "chat.user_message",
            message
        )

        chat_history.append({
            "id": len(chat_history) + 1,
            "role": "user",
            "message": message
        })

        reply = f"You said: {message}"

        chat_history.append({
            "id": len(chat_history) + 1,
            "role": "assistant",
            "message": reply
        })

        cache.cache_chat_history(
            "default",
            chat_history,
            ttl=86400
        )

        span.set_attribute(
            "chat.response_generated",
            True
        )

        return {
            "reply": reply,
            "cached": True
        } 
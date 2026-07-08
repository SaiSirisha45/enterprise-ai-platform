from fastapi import APIRouter

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)

@router.get("")
def analytics():
    return {
        "active_users": 156,
        "active_agents": 12,
        "documents": 2340,
        "queries_today": 8420
    } 
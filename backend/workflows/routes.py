from fastapi import APIRouter

router = APIRouter(
    prefix="/workflow",
    tags=["Workflow"]
)

history = [
    {
        "id": "1",
        "workflow": "Employee Onboarding",
        "status": "Completed"
    }
]


@router.get("/history")
def workflow_history():
    return history


@router.post("/retry/{id}")
def retry_workflow(id: str):
    return {
        "message": f"Workflow {id} restarted"
    } 
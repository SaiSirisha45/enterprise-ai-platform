from fastapi import APIRouter

from monitoring.tracing import tracer
from monitoring.logging import logger

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

    with tracer.start_as_current_span("Workflow History"):

        logger.info("Workflow History Requested")

        return history


@router.post("/retry/{id}")
def retry_workflow(id: str):

    with tracer.start_as_current_span("Retry Workflow") as span:

        span.set_attribute("workflow.id", id)

        logger.info(
            "Workflow Restarted",
            extra={"workflow_id": id}
        )

        return {
            "message": f"Workflow {id} restarted"
        } 
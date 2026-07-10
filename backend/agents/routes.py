from fastapi import APIRouter

from monitoring.tracing import tracer
from monitoring.logging import logger

router = APIRouter(
    prefix="/agents",
    tags=["Agents"]
)

agents = [
    {
        "id": "1",
        "name": "HR Agent",
        "status": "Running"
    },
    {
        "id": "2",
        "name": "Payroll Agent",
        "status": "Stopped"
    }
]


@router.get("")
def get_agents():

    with tracer.start_as_current_span("Get Agents"):

        logger.info("Fetching Agents")

        return agents


@router.post("/{id}/start")
def start_agent(id: str):

    with tracer.start_as_current_span("Start Agent") as span:

        span.set_attribute("agent.id", id)

        logger.info(
            "Agent Started",
            extra={"agent_id": id}
        )

        return {
            "message": f"Agent {id} started"
        }


@router.post("/{id}/stop")
def stop_agent(id: str):

    with tracer.start_as_current_span("Stop Agent") as span:

        span.set_attribute("agent.id", id)

        logger.info(
            "Agent Stopped",
            extra={"agent_id": id}
        )

        return {
            "message": f"Agent {id} stopped"
        } 
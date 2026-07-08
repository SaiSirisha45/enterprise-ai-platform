from fastapi import APIRouter

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
    return agents


@router.post("/{id}/start")
def start_agent(id: str):
    return {
        "message": f"Agent {id} started"
    }


@router.post("/{id}/stop")
def stop_agent(id: str):
    return {
        "message": f"Agent {id} stopped"
    } 
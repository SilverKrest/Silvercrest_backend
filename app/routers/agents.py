from fastapi import APIRouter, HTTPException
from app.schemas import AgentOut

router = APIRouter(prefix="/api/agents", tags=["Agents"])

DUMMY = [
    {
        "id": "agent_001",
        "name": "Elena Vasquez",
        "title": "Coastal Markets Lead",
        "location": "Miami, FL",
        "specialty": "Waterfront",
        "rating": 4.9,
        "closed_deals": 42,
    }
]


@router.get("", response_model=list[AgentOut])
async def list_agents():
    return DUMMY


@router.get("/{agent_id}", response_model=AgentOut)
async def get_agent(agent_id: str):
    for row in DUMMY:
        if row["id"] == agent_id:
            return row
    raise HTTPException(status_code=404, detail="Agent not found")

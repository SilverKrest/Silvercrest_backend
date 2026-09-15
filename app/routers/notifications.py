from fastapi import APIRouter
from app.schemas import NotificationOut

router = APIRouter(prefix="/api/notifications", tags=["Notifications"])

SAMPLE = [
    {
        "id": "ntf_001",
        "kind": "offer",
        "title": "New offer",
        "body": "Sample inbox item.",
        "read": False,
        "created_at": 1697021000,
    }
]


@router.get("", response_model=list[NotificationOut])
async def list_notifications():
    return SAMPLE

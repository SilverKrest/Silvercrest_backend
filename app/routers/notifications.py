from fastapi import APIRouter
from app.schemas import NotificationOut

router = APIRouter(prefix="/api/notifications", tags=["Notifications"])

DUMMY = [
    {
        "id": "ntf_001",
        "kind": "offer",
        "title": "New offer",
        "body": "Dummy inbox item.",
        "read": False,
        "created_at": 1697021000,
    }
]


@router.get("", response_model=list[NotificationOut])
async def list_notifications():
    return DUMMY

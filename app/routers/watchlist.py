from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/watchlist", tags=["Watchlist"])


class WatchItem(BaseModel):
    property_id: str


DUMMY = [{"property_id": "prop_001"}]


@router.get("")
async def get_watchlist():
    return DUMMY


@router.post("")
async def add_watch(item: WatchItem):
    DUMMY.append({"property_id": item.property_id})
    return item

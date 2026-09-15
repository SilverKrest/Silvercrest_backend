from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/api/watchlist", tags=["Watchlist"])


class WatchItem(BaseModel):
    property_id: str


SAMPLE = [{"property_id": "prop_001"}]


@router.get("")
async def get_watchlist():
    return SAMPLE


@router.post("")
async def add_watch(item: WatchItem):
    SAMPLE.append({"property_id": item.property_id})
    return item

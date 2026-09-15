from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.data.properties import PROPERTIES

router = APIRouter(prefix="/api/watchlist", tags=["Watchlist"])


class WatchItem(BaseModel):
    property_id: str


SAMPLE = [{"property_id": "prop_001"}]


@router.get("")
async def get_watchlist():
    return SAMPLE


@router.post("")
async def add_watch(item: WatchItem):
    if item.property_id not in PROPERTIES:
        raise HTTPException(status_code=404, detail="Property not found")
    SAMPLE.append({"property_id": item.property_id})
    return item

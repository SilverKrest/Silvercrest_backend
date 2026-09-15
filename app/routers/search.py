from fastapi import APIRouter, Query
from typing import List
from app.schemas import PropertyOut
from app.data.properties import PROPERTIES

router = APIRouter(prefix="/api/search", tags=["Search"])


@router.get("", response_model=List[PropertyOut])
async def search_properties(q: str = Query(..., min_length=1)):
    query = q.lower()
    return [
        p
        for p in PROPERTIES.values()
        if query in p["title"].lower() or query in p["location"].lower()
    ]

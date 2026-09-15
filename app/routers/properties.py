from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.schemas import PropertyOut
from app.data.properties import PROPERTIES

router = APIRouter(prefix="/api/properties", tags=["Properties"])


@router.get("", response_model=List[PropertyOut])
async def list_properties(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    items = list(PROPERTIES.values())
    return items[skip : skip + limit]


@router.get("/{property_id}", response_model=PropertyOut)
async def get_property(property_id: str):
    if property_id not in PROPERTIES:
        raise HTTPException(status_code=404, detail="Property not found")
    return PROPERTIES[property_id]

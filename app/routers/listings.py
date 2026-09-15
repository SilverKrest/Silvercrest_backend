from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from app.schemas import ListingOut
from app.data.listings import LISTINGS

router = APIRouter(prefix="/api/listings", tags=["Listings"])


@router.get("", response_model=List[ListingOut])
async def list_listings(status: Optional[str] = None, skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    items = list(LISTINGS.values())
    if status:
        items = [i for i in items if i["status"] == status]
    return items[skip : skip + limit]


@router.get("/{listing_id}", response_model=ListingOut)
async def get_listing(listing_id: str):
    if listing_id not in LISTINGS:
        raise HTTPException(status_code=404, detail="Listing not found")
    return LISTINGS[listing_id]

from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query

from app.data.listings import LISTINGS
from app.schemas import ListingOut

router = APIRouter(prefix="/api/listings", tags=["Listings"])


def _filtered(status: Optional[str], seller: Optional[str]) -> list[dict]:
    items = list(LISTINGS.values())
    if status:
        items = [item for item in items if item["status"] == status]
    if seller:
        items = [item for item in items if item["seller"] == seller]
    return items


@router.get("", response_model=List[ListingOut])
async def list_listings(
    status: Optional[str] = None,
    seller: Optional[str] = None,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
):
    return _filtered(status, seller)[skip : skip + limit]


@router.get("/property/{property_id}", response_model=List[ListingOut])
async def listings_for_property(property_id: str):
    items = [item for item in LISTINGS.values() if item["property_id"] == property_id]
    if not items:
        raise HTTPException(status_code=404, detail="No listings for property")
    return items


@router.get("/{listing_id}", response_model=ListingOut)
async def get_listing(listing_id: str):
    if listing_id not in LISTINGS:
        raise HTTPException(status_code=404, detail="Listing not found")
    return LISTINGS[listing_id]

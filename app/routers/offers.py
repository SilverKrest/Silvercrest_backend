from time import time
from typing import List
from uuid import uuid4

from fastapi import APIRouter, HTTPException, Query

from app.data.listings import LISTINGS
from app.data.offers import OFFERS
from app.schemas import OfferCreate, OfferOut
from app.stellar import is_stellar_public_key

router = APIRouter(prefix="/api/offers", tags=["Offers"])


@router.get("", response_model=List[OfferOut])
async def list_offers(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    return list(OFFERS.values())[skip : skip + limit]


@router.get("/listing/{listing_id}", response_model=List[OfferOut])
async def offers_for_listing(listing_id: str):
    if listing_id not in LISTINGS:
        raise HTTPException(status_code=404, detail="Listing not found")
    return [item for item in OFFERS.values() if item["listing_id"] == listing_id]


@router.post("", response_model=OfferOut, status_code=201)
async def create_offer(body: OfferCreate):
    if not is_stellar_public_key(body.buyer):
        raise HTTPException(status_code=422, detail="buyer must be a Stellar G... public key")
    if body.listing_id not in LISTINGS:
        raise HTTPException(status_code=404, detail="Listing not found")
    offer_id = f"offer_{uuid4().hex[:8]}"
    record = {
        "id": offer_id,
        "listing_id": body.listing_id,
        "buyer": body.buyer,
        "price": body.price,
        "status": "pending",
        "created_at": int(time()),
    }
    OFFERS[offer_id] = record
    return record


@router.get("/{offer_id}", response_model=OfferOut)
async def get_offer(offer_id: str):
    if offer_id not in OFFERS:
        raise HTTPException(status_code=404, detail="Offer not found")
    return OFFERS[offer_id]

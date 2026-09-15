from fastapi import APIRouter, HTTPException, Query
from typing import List
from app.schemas import OfferOut
from app.data.offers import OFFERS

router = APIRouter(prefix="/api/offers", tags=["Offers"])


@router.get("", response_model=List[OfferOut])
async def list_offers(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    items = list(OFFERS.values())
    return items[skip : skip + limit]


@router.get("/{offer_id}", response_model=OfferOut)
async def get_offer(offer_id: str):
    if offer_id not in OFFERS:
        raise HTTPException(status_code=404, detail="Offer not found")
    return OFFERS[offer_id]

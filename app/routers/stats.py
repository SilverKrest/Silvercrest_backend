from fastapi import APIRouter
from app.data.properties import PROPERTIES
from app.data.listings import LISTINGS
from app.data.offers import OFFERS

router = APIRouter(prefix="/api/stats", tags=["Stats"])


@router.get("")
async def market_stats():
    listings = list(LISTINGS.values())
    offers = list(OFFERS.values())
    total = sum(l["price"] for l in listings) or 0
    return {
        "total_properties": len(PROPERTIES),
        "active_listings": len([l for l in listings if l["status"] == "active"]),
        "total_volume": total,
        "pending_offers": len([o for o in offers if o["status"] == "pending"]),
        "avg_price": int(total / len(listings)) if listings else 0,
        "sold_this_month": len([l for l in listings if l["status"] == "sold"]),
    }

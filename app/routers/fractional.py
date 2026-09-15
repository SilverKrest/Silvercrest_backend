from fastapi import APIRouter

router = APIRouter(prefix="/api/fractional", tags=["Fractional"])


@router.get("")
async def list_positions():
    return [
        {
            "id": "frac_001",
            "property_id": "prop_007",
            "property_title": "Vineyard Estate",
            "shares": 40,
            "share_price": 8000,
            "dummy": True,
        }
    ]

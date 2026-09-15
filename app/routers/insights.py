from fastapi import APIRouter
from app.schemas import InsightOut

router = APIRouter(prefix="/api/insights", tags=["Insights"])

DUMMY = [
    {
        "id": "ins_001",
        "title": "Miami tokenized inventory tightens",
        "city": "Miami, FL",
        "summary": "Dummy index for oceanfront asks.",
        "change_pct": 4.2,
        "median_price": 890000,
        "published_at": 1697020000,
    }
]


@router.get("", response_model=list[InsightOut])
async def list_insights():
    return DUMMY

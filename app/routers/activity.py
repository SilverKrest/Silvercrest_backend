from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/activity", tags=["Activity"])


@router.get("")
async def list_activity(limit: int = Query(10, ge=1, le=50)):
    return [
        {
            "id": "act_api_001",
            "type": "listing_created",
            "property_title": "Sunny Beachfront Villa",
            "actor": "GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
            "timestamp": 1697000000,
        }
    ][:limit]

from fastapi import APIRouter

from app.config import CONTRACT_ID, STELLAR_HORIZON_URL, STELLAR_NETWORK
from app.schemas import HealthOut
from app.services.horizon import ping_horizon

API_VERSION = "0.3.1"

router = APIRouter(tags=["Health"])


@router.get("/", response_model=dict)
async def root():
    return {
        "service": "SilverKrest Backend",
        "version": API_VERSION,
        "network": STELLAR_NETWORK,
        "contract_id": CONTRACT_ID,
        "horizon_url": STELLAR_HORIZON_URL,
        "sample": True,
    }


@router.get("/health", response_model=HealthOut)
async def health():
    horizon_ok = await ping_horizon()
    return HealthOut(
        status="ok" if horizon_ok else "degraded",
        network=STELLAR_NETWORK,
        sample=True,
        version=API_VERSION,
        horizon_ok=horizon_ok,
        horizon_url=STELLAR_HORIZON_URL,
        contract_id=CONTRACT_ID,
    )

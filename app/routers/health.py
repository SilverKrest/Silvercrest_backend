from fastapi import APIRouter
from app.config import STELLAR_NETWORK, CONTRACT_ID
from app.schemas import HealthOut

router = APIRouter(tags=["Health"])


@router.get("/", response_model=dict)
async def root():
    return {
        "service": "SilverKrest Backend",
        "version": "0.2.0",
        "network": STELLAR_NETWORK,
        "contract_id": CONTRACT_ID,
        "dummy": True,
    }


@router.get("/health", response_model=HealthOut)
async def health():
    return HealthOut(status="ok", network=STELLAR_NETWORK, dummy=True)

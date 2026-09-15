from fastapi import APIRouter

router = APIRouter(prefix="/api/kyc", tags=["KYC"])


@router.get("")
async def get_kyc():
    return {
        "public_key": "GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        "status": "verified",
        "legal_name": "Demo Investor",
        "country": "US",
        "sample": True,
    }

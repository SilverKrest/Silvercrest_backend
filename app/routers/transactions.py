from fastapi import APIRouter

router = APIRouter(prefix="/api/transactions", tags=["Transactions"])


@router.get("")
async def list_transactions():
    return [
        {
            "id": "tx_001",
            "kind": "tokenize",
            "property_title": "Sunny Beachfront Villa",
            "hash": "abc123dummyhash0001",
            "status": "confirmed",
            "timestamp": 1697000000,
        }
    ]

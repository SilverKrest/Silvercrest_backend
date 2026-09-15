from fastapi import APIRouter, Query

router = APIRouter(prefix="/api/documents", tags=["Documents"])


@router.get("")
async def list_documents(property_id: str = Query(...)):
    return [
        {
            "id": "doc_001",
            "property_id": property_id,
            "kind": "deed",
            "title": "Sample deed",
            "uri": "ipfs://QmCatalogDeed",
        }
    ]

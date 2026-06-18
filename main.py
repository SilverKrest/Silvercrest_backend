from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="SilverKrest Backend",
    description="API & Indexer for tokenized real estate on Stellar",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Config
STELLAR_NETWORK = os.getenv("STELLAR_NETWORK", "testnet")
CONTRACT_ID = os.getenv("CONTRACT_PROPERTY_REGISTRY_ID")


# Pydantic models
class PropertyResponse(BaseModel):
    id: str
    title: str
    location: str
    price: int
    currency: str
    owner: str
    nft_contract: str
    nft_id: str
    metadata_uri: str
    created_at: int
    image: str = ""

    class Config:
        json_schema_extra = {
            "example": {
                "id": "prop_001",
                "title": "Sunny Beachfront Villa",
                "location": "Miami, FL",
                "price": 500000,
                "currency": "USD",
                "owner": "GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
                "nft_contract": "CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABSC4",
                "nft_id": "nft_001",
                "metadata_uri": "ipfs://QmExample",
                "created_at": 1697000000,
                "image": "https://images.example.com/property.jpg",
            }
        }


class ListingResponse(BaseModel):
    id: str
    property_id: str
    seller: str
    price: int
    currency: str
    status: str  # "active" | "pending" | "sold"
    created_at: int

    class Config:
        json_schema_extra = {
            "example": {
                "id": "list_001",
                "property_id": "prop_001",
                "seller": "GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
                "price": 500000,
                "currency": "USD",
                "status": "active",
                "created_at": 1697000000,
            }
        }


class OfferResponse(BaseModel):
    id: str
    listing_id: str
    buyer: str
    price: int
    status: str  # "pending" | "accepted" | "rejected"
    created_at: int

    class Config:
        json_schema_extra = {
            "example": {
                "id": "offer_001",
                "listing_id": "list_001",
                "buyer": "GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
                "price": 480000,
                "status": "pending",
                "created_at": 1697010000,
            }
        }


# Mock data
PROPERTIES = {
    "prop_001": PropertyResponse(
        id="prop_001",
        title="Sunny Beachfront Villa",
        location="Miami, FL",
        price=500000,
        currency="USD",
        owner="GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        nft_contract="CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABSC4",
        nft_id="nft_001",
        metadata_uri="ipfs://QmExample1",
        created_at=1697000000,
        image="https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600",
    ),
    "prop_002": PropertyResponse(
        id="prop_002",
        title="Mountain Retreat Home",
        location="Aspen, CO",
        price=750000,
        currency="USD",
        owner="GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        nft_contract="CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABSC4",
        nft_id="nft_002",
        metadata_uri="ipfs://QmExample2",
        created_at=1697001000,
        image="https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=600",
    ),
    "prop_003": PropertyResponse(
        id="prop_003",
        title="Urban Penthouse",
        location="New York, NY",
        price=2000000,
        currency="USD",
        owner="GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        nft_contract="CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABSC4",
        nft_id="nft_003",
        metadata_uri="ipfs://QmExample3",
        created_at=1697002000,
        image="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=600",
    ),
}

LISTINGS = {
    "list_001": ListingResponse(
        id="list_001",
        property_id="prop_001",
        seller="GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        price=500000,
        currency="USD",
        status="active",
        created_at=1697000000,
    ),
    "list_002": ListingResponse(
        id="list_002",
        property_id="prop_002",
        seller="GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        price=700000,
        currency="USD",
        status="active",
        created_at=1697001000,
    ),
    "list_003": ListingResponse(
        id="list_003",
        property_id="prop_003",
        seller="GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        price=1950000,
        currency="USD",
        status="pending",
        created_at=1697002000,
    ),
}

OFFERS = {
    "offer_001": OfferResponse(
        id="offer_001",
        listing_id="list_001",
        buyer="GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        price=480000,
        status="pending",
        created_at=1697010000,
    ),
    "offer_002": OfferResponse(
        id="offer_002",
        listing_id="list_003",
        buyer="GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        price=1900000,
        status="accepted",
        created_at=1697012000,
    ),
}


# Routes
@app.get("/", tags=["Health"])
async def root():
    return {
        "service": "SilverKrest Backend",
        "version": "0.1.0",
        "network": STELLAR_NETWORK,
        "contract_id": CONTRACT_ID,
    }


@app.get("/health", tags=["Health"])
async def health():
    return {"status": "ok", "network": STELLAR_NETWORK}


# Properties
@app.get("/api/properties", response_model=List[PropertyResponse], tags=["Properties"])
async def list_properties(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    """Get all properties (paginated)."""
    items = list(PROPERTIES.values())
    return items[skip : skip + limit]


@app.get("/api/properties/{property_id}", response_model=PropertyResponse, tags=["Properties"])
async def get_property(property_id: str):
    """Get a single property by ID."""
    if property_id not in PROPERTIES:
        raise HTTPException(status_code=404, detail="Property not found")
    return PROPERTIES[property_id]


# Listings
@app.get("/api/listings", response_model=List[ListingResponse], tags=["Listings"])
async def list_listings(
    status: Optional[str] = Query(None), skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)
):
    """Get all listings, optionally filtered by status."""
    items = list(LISTINGS.values())
    if status:
        items = [l for l in items if l.status == status]
    return items[skip : skip + limit]


@app.get("/api/listings/{listing_id}", response_model=ListingResponse, tags=["Listings"])
async def get_listing(listing_id: str):
    """Get a single listing by ID."""
    if listing_id not in LISTINGS:
        raise HTTPException(status_code=404, detail="Listing not found")
    return LISTINGS[listing_id]


@app.get("/api/listings/property/{property_id}", response_model=List[ListingResponse], tags=["Listings"])
async def get_listings_for_property(property_id: str):
    """Get all listings for a property."""
    return [l for l in LISTINGS.values() if l.property_id == property_id]


# Offers
@app.get("/api/offers", response_model=List[OfferResponse], tags=["Offers"])
async def list_offers(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100)):
    """Get all offers (paginated)."""
    items = list(OFFERS.values())
    return items[skip : skip + limit]


@app.get("/api/offers/{offer_id}", response_model=OfferResponse, tags=["Offers"])
async def get_offer(offer_id: str):
    """Get a single offer by ID."""
    if offer_id not in OFFERS:
        raise HTTPException(status_code=404, detail="Offer not found")
    return OFFERS[offer_id]


@app.get("/api/offers/listing/{listing_id}", response_model=List[OfferResponse], tags=["Offers"])
async def get_offers_for_listing(listing_id: str):
    """Get all offers for a listing."""
    return [o for o in OFFERS.values() if o.listing_id == listing_id]


@app.get("/api/search", response_model=List[PropertyResponse], tags=["Search"])
async def search_properties(q: str = Query(..., min_length=1)):
    """Search properties by title or location."""
    query = q.lower()
    results = [
        p
        for p in PROPERTIES.values()
        if query in p.title.lower() or query in p.location.lower()
    ]
    return results


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

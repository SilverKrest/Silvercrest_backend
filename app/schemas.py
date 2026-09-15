from pydantic import BaseModel, Field
from typing import Optional, List


class PropertyOut(BaseModel):
    id: str
    title: str
    location: str
    price: int
    currency: str = "USD"
    owner: str
    nft_contract: str
    nft_id: str
    metadata_uri: str
    created_at: int
    image: str = ""
    beds: Optional[int] = None
    baths: Optional[int] = None
    sqft: Optional[int] = None
    property_type: Optional[str] = None
    featured: bool = False
    fractional: bool = False


class ListingOut(BaseModel):
    id: str
    property_id: str
    seller: str
    price: int
    currency: str = "USD"
    status: str
    created_at: int


class OfferOut(BaseModel):
    id: str
    listing_id: str
    buyer: str
    price: int
    status: str
    created_at: int


class AgentOut(BaseModel):
    id: str
    name: str
    title: str
    location: str
    specialty: str
    rating: float
    closed_deals: int


class InsightOut(BaseModel):
    id: str
    title: str
    city: str
    summary: str
    change_pct: float
    median_price: int
    published_at: int


class NotificationOut(BaseModel):
    id: str
    kind: str
    title: str
    body: str
    read: bool
    created_at: int


class HealthOut(BaseModel):
    status: str = "ok"
    network: str
    sample: bool = True

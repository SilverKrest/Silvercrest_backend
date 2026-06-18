# SilverKrest Backend

REST API & indexer for tokenized real estate on Stellar.

## Overview

FastAPI application that:
- **Indexes** contract state from Soroban (properties, listings, offers)
- **Serves** REST endpoints for the frontend
- **Handles** search and filtering
- **Mock data** for v0.1 (real indexing in v0.2+)

## Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

```bash
pip install -r requirements.txt
```

### Running

```bash
python main.py
```

Server runs on `http://localhost:8000`.

API docs: `http://localhost:8000/docs` (Swagger UI)

## Environment Variables

See `.env.example`:

```
STELLAR_NETWORK=testnet          # testnet or mainnet
STELLAR_RPC_URL=...              # Soroban RPC endpoint
CONTRACT_PROPERTY_REGISTRY_ID=... # Deployed contract ID
```

## API Endpoints

All endpoints return JSON and support CORS.

### Health

- `GET /` — Service info
- `GET /health` — Health check

### Properties

- `GET /api/properties?skip=0&limit=10` — List properties (paginated)
- `GET /api/properties/{id}` — Get property by ID
- `GET /api/search?q=Miami` — Search by title/location

### Listings

- `GET /api/listings?status=active` — List listings (filter by status: active/pending/sold)
- `GET /api/listings/{id}` — Get listing by ID
- `GET /api/listings/property/{property_id}` — Get listings for a property

### Offers

- `GET /api/offers` — List offers (paginated)
- `GET /api/offers/{id}` — Get offer by ID
- `GET /api/offers/listing/{listing_id}` — Get offers for a listing

## Data Models

**Property**
```json
{
  "id": "prop_001",
  "title": "Sunny Beachfront Villa",
  "location": "Miami, FL",
  "price": 500000,
  "currency": "USD",
  "owner": "GDZST3X...",
  "nft_contract": "CAAAA...",
  "nft_id": "nft_001",
  "metadata_uri": "ipfs://QmExample",
  "created_at": 1697000000,
  "image": "https://..."
}
```

**Listing**
```json
{
  "id": "list_001",
  "property_id": "prop_001",
  "seller": "GDZST3X...",
  "price": 500000,
  "currency": "USD",
  "status": "active",
  "created_at": 1697000000
}
```

**Offer**
```json
{
  "id": "offer_001",
  "listing_id": "list_001",
  "buyer": "GDZST3X...",
  "price": 480000,
  "status": "pending",
  "created_at": 1697010000
}
```

## Roadmap

- **v0.1** (current): Mock data, full API schema
- **v0.2**: Real Soroban indexing (event listener)
- **v0.3**: Database persistence (SQLite/Postgres)
- **v0.4**: Authentication & rate limiting
- **v0.5**: Webhook support for frontend push updates
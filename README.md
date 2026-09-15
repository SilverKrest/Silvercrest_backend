# SilverKrest Backend

FastAPI catalog indexer and REST API for tokenized real estate on Stellar.

Version **0.3.1** serves health (including a Horizon ping), properties, listings, offers, search, insights, agents, notifications, KYC, fractional lots, documents, and stats. Listings are derived from the property catalog. Offer create validates Stellar G-strkeys. Nested routes match the frontend:

- `GET /api/listings/property/{property_id}`
- `GET /api/offers/listing/{listing_id}`
- `POST /api/offers`

```bash
uvicorn app.main:app --reload --port 8000
pytest
```

Compatibility entry: `python main.py`

See `.env.example`. Never commit private keys.

# SilverKrest Backend

FastAPI catalog indexer and REST API for tokenized real estate on Stellar.

The `app/` package serves health, properties, listings, offers, search, insights, agents, notifications, KYC, fractional lots, documents, and stats. Modular `prop_*` fixtures are merged into the properties catalog at startup.

```bash
uvicorn app.main:app --reload --port 8000
```

Compatibility entry: `python main.py`

See `.env.example`. Never commit private keys.

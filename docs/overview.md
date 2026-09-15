# Backend overview

FastAPI catalog indexer for SilverKrest on Stellar.

Current API version: **0.3.1**. Property records in `app/data/prop_*.py` are loaded into `PROPERTIES` when the app starts. Active listings are generated from that catalog. `/health` reports `horizon_ok` after a short ping to Stellar Horizon. Offers require a G-strkey buyer and a known listing id.

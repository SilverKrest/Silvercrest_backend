import os

from dotenv import load_dotenv

from app.stellar import horizon_url

load_dotenv()

STELLAR_NETWORK = os.getenv("STELLAR_NETWORK", "testnet")
STELLAR_HORIZON_URL = os.getenv("STELLAR_HORIZON_URL", horizon_url(STELLAR_NETWORK))
CONTRACT_ID = os.getenv("CONTRACT_PROPERTY_REGISTRY_ID")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

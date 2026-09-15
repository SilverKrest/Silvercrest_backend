import os

STELLAR_NETWORK = os.getenv("STELLAR_NETWORK", "testnet")
CONTRACT_ID = os.getenv("CONTRACT_PROPERTY_REGISTRY_ID")
DEBUG = os.getenv("DEBUG", "true").lower() == "true"
CORS_ORIGINS = os.getenv("CORS_ORIGINS", "*").split(",")

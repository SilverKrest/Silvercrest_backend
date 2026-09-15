from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import CORS_ORIGINS, STELLAR_NETWORK
from app.routers import (
    health,
    properties,
    listings,
    offers,
    search,
    insights,
    agents,
    notifications,
    activity,
    stats,
    watchlist,
    kyc,
    fractional,
    transactions,
    documents,
)

app = FastAPI(
    title="SilverKrest Backend",
    description="API & indexer for tokenized real estate on Stellar (dummy data v0.2)",
    version="0.2.0",
)

origins = ["*"] if CORS_ORIGINS == ["*"] else CORS_ORIGINS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
app.include_router(properties.router)
app.include_router(listings.router)
app.include_router(offers.router)
app.include_router(search.router)
app.include_router(insights.router)
app.include_router(agents.router)
app.include_router(notifications.router)
app.include_router(activity.router)
app.include_router(stats.router)
app.include_router(watchlist.router)
app.include_router(kyc.router)
app.include_router(fractional.router)
app.include_router(transactions.router)
app.include_router(documents.router)

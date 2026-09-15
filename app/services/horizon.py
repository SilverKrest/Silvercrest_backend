from __future__ import annotations

import httpx
from app.config import STELLAR_NETWORK, STELLAR_HORIZON_URL
from app.stellar import horizon_url


async def ping_horizon(timeout: float = 2.5) -> bool:
    url = STELLAR_HORIZON_URL or horizon_url(STELLAR_NETWORK)
    try:
        async with httpx.AsyncClient(timeout=timeout) as client:
            res = await client.get(f"{url.rstrip('/')}/")
            return res.is_success
    except httpx.HTTPError:
        return False

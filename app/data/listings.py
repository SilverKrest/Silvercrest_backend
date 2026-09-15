from app.data.properties import PROPERTIES

LISTINGS = {
    "list_001": {
        "id": "list_001",
        "property_id": "prop_001",
        "seller": "GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        "price": 500000,
        "currency": "USD",
        "status": "active",
        "created_at": 1697000000,
    }
}


def _listings_from_catalog() -> None:
    for prop in PROPERTIES.values():
        listing_id = f"list_{prop['id'].removeprefix('prop_')}"
        if listing_id in LISTINGS:
            continue
        LISTINGS[listing_id] = {
            "id": listing_id,
            "property_id": prop["id"],
            "seller": prop.get("owner") or "",
            "price": int(prop.get("price") or 0),
            "currency": prop.get("currency") or "USD",
            "status": "active",
            "created_at": int(prop.get("created_at") or 0),
        }


_listings_from_catalog()

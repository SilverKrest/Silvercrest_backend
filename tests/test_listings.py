def test_list_listings(client):
    res = client.get("/api/listings")
    assert res.status_code == 200
    items = res.json()
    assert len(items) >= 1
    assert items[0]["seller"].startswith("G")


def test_listings_for_property(client):
    res = client.get("/api/listings/property/prop_001")
    assert res.status_code == 200
    items = res.json()
    assert items
    assert all(item["property_id"] == "prop_001" for item in items)


def test_listings_for_unknown_property(client):
    res = client.get("/api/listings/property/prop_missing")
    assert res.status_code == 404


def test_get_listing_by_id(client):
    res = client.get("/api/listings/list_001")
    assert res.status_code == 200
    assert res.json()["id"] == "list_001"

def test_watchlist_starts_with_sample(client):
    res = client.get("/api/watchlist")
    assert res.status_code == 200
    assert any(item["property_id"] == "prop_001" for item in res.json())


def test_watchlist_rejects_unknown_property(client):
    res = client.post("/api/watchlist", json={"property_id": "prop_missing"})
    assert res.status_code == 404


def test_watchlist_accepts_known_property(client):
    res = client.post("/api/watchlist", json={"property_id": "prop_001"})
    assert res.status_code == 200
    assert res.json()["property_id"] == "prop_001"

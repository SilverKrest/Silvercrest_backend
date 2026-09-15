def test_search_by_city(client):
    res = client.get("/api/search", params={"q": "Miami"})
    assert res.status_code == 200
    items = res.json()
    assert any("Miami" in item["location"] for item in items)


def test_search_by_property_id(client):
    res = client.get("/api/search", params={"q": "prop_001"})
    assert res.status_code == 200
    ids = [item["id"] for item in res.json()]
    assert "prop_001" in ids


def test_search_requires_query(client):
    res = client.get("/api/search")
    assert res.status_code == 422

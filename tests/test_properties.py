def test_list_properties_returns_catalog(client):
    res = client.get("/api/properties?limit=5")
    assert res.status_code == 200
    items = res.json()
    assert isinstance(items, list)
    assert len(items) >= 1
    assert items[0]["id"].startswith("prop_")
    assert items[0]["owner"].startswith("G")


def test_get_known_property(client):
    res = client.get("/api/properties/prop_001")
    assert res.status_code == 200
    body = res.json()
    assert body["id"] == "prop_001"
    assert body["title"]


def test_missing_property_is_404(client):
    res = client.get("/api/properties/prop_missing")
    assert res.status_code == 404

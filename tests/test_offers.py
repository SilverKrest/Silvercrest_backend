VALID_BUYER = "GDQP2KPQGKAJY5TPHFMWECV526QRSRKRHLHDMAGJJAAZKQTXGRLGUAAA"


def test_list_offers(client):
    res = client.get("/api/offers")
    assert res.status_code == 200
    items = res.json()
    assert any(item["id"] == "offer_001" for item in items)


def test_offers_for_listing(client):
    res = client.get("/api/offers/listing/list_001")
    assert res.status_code == 200
    items = res.json()
    assert all(item["listing_id"] == "list_001" for item in items)


def test_offers_for_unknown_listing(client):
    res = client.get("/api/offers/listing/list_missing")
    assert res.status_code == 404


def test_create_offer_rejects_non_stellar_buyer(client):
    res = client.post(
        "/api/offers",
        json={"listing_id": "list_001", "buyer": "not-a-key", "price": 1000},
    )
    assert res.status_code == 422


def test_create_offer_rejects_zero_price(client):
    res = client.post(
        "/api/offers",
        json={"listing_id": "list_001", "buyer": VALID_BUYER, "price": 0},
    )
    assert res.status_code == 422


def test_create_offer_for_known_listing(client):
    res = client.post(
        "/api/offers",
        json={"listing_id": "list_001", "buyer": VALID_BUYER, "price": 450000},
    )
    assert res.status_code == 201
    body = res.json()
    assert body["buyer"] == VALID_BUYER
    assert body["status"] == "pending"
    listed = client.get(f"/api/offers/listing/{body['listing_id']}")
    assert any(item["id"] == body["id"] for item in listed.json())

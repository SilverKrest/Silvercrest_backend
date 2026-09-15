from unittest.mock import AsyncMock, patch


def test_root_reports_current_version(client):
    res = client.get("/")
    assert res.status_code == 200
    body = res.json()
    assert body["version"] == "0.3.1"
    assert body["network"] == "testnet"
    assert "horizon_url" in body


def test_health_includes_horizon_when_reachable(client):
    with patch("app.routers.health.ping_horizon", new=AsyncMock(return_value=True)):
        res = client.get("/health")
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "ok"
    assert body["version"] == "0.3.1"
    assert body["horizon_ok"] is True
    assert body["horizon_url"]


def test_health_degraded_when_horizon_down(client):
    with patch("app.routers.health.ping_horizon", new=AsyncMock(return_value=False)):
        res = client.get("/health")
    assert res.status_code == 200
    body = res.json()
    assert body["status"] == "degraded"
    assert body["horizon_ok"] is False

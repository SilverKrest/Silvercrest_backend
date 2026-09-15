from app.main import app
from app.routers.health import API_VERSION


def test_api_version_is_current():
    assert app.version == "0.3.1"
    assert API_VERSION == app.version

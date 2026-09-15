"""API version coverage for 0.3.0."""

from app.main import app


def test_api_version_is_three():
    assert app.version == "0.3.0"

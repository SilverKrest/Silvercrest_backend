"""Sample property catalog served by the API."""

from importlib import import_module
from pathlib import Path

PROPERTIES = {
    "prop_001": {
        "id": "prop_001",
        "title": "Sunny Beachfront Villa",
        "location": "Miami, FL",
        "price": 500000,
        "currency": "USD",
        "owner": "GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP",
        "nft_contract": "CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABSC4",
        "nft_id": "nft_001",
        "metadata_uri": "ipfs://QmExample1",
        "created_at": 1697000000,
        "image": "https://images.unsplash.com/photo-1600585154340-be6161a56a0c?w=600",
        "featured": True,
    }
}


def _merge_catalog_fixtures() -> None:
    data_dir = Path(__file__).parent
    for path in sorted(data_dir.glob("prop_*.py")):
        mod = import_module(f"app.data.{path.stem}")
        rec = getattr(mod, "RECORD", None)
        if isinstance(rec, dict) and rec.get("id"):
            PROPERTIES[rec["id"]] = rec


_merge_catalog_fixtures()

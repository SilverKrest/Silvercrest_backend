import re

_STELLAR_ACCOUNT = re.compile(r"^G[A-Z2-7]{55}$")
_STELLAR_CONTRACT = re.compile(r"^C[A-Z2-7]{55}$")

HORIZON_URLS = {
    "testnet": "https://horizon-testnet.stellar.org",
    "mainnet": "https://horizon.stellar.org",
}


def is_stellar_public_key(value: str) -> bool:
    return bool(value) and bool(_STELLAR_ACCOUNT.match(value))


def is_stellar_contract_id(value: str) -> bool:
    return bool(value) and bool(_STELLAR_CONTRACT.match(value))


def horizon_url(network: str) -> str:
    return HORIZON_URLS.get(network, HORIZON_URLS["testnet"])

from app.stellar import horizon_url, is_stellar_contract_id, is_stellar_public_key


def test_accepts_g_strkey():
    assert is_stellar_public_key(
        "GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP"
    )


def test_rejects_short_or_wrong_prefix():
    assert not is_stellar_public_key("GSHORT")
    assert not is_stellar_public_key("not-a-key")
    assert not is_stellar_public_key("")


def test_contract_id_must_be_c_strkey():
    assert is_stellar_contract_id(
        "CAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABSC4"
    )
    assert not is_stellar_contract_id(
        "GDZST3XVCDTUJ76ZAV2HA72KYFL3JCPBHQ4PXESVXHMZQ5MDDG2WXYUP"
    )


def test_horizon_url_follows_network():
    assert horizon_url("testnet") == "https://horizon-testnet.stellar.org"
    assert horizon_url("mainnet") == "https://horizon.stellar.org"
    assert horizon_url("unknown") == "https://horizon-testnet.stellar.org"

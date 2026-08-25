def test_login(token):
    assert token is not None
    assert isinstance(token, str)
    assert token != ""

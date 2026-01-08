import pytest

@pytest.mark.smoke
def test_open():
    print("app opened")
    assert True


@pytest.mark.skip
@pytest.mark.smoke
def test_login():
    print("login page opened")
    assert True


def test_adduser():
    print("added user")
    assert True

def test_addpass():
    print("added password")
    assert True

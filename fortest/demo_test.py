import pytest
# def test_first():
#     a=3
#     b=6
#     assert a==b , "not equal"


@pytest.fixture
def db():
    db={"connected":True}
    yield db
    db.clear()

def test_login(db):
    assert db["connected"]

import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("Test Bun 1", 50.0),
    ("Test Bun 2", 75.0),
    ("Test Bun 3", 100.0)
])
def test_bun_creation(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price

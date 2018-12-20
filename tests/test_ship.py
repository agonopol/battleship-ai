from battleship.ship import Ship
import pytest

def test_ship_ok():
    ship = Ship((0, 0), (0, 2))
    assert ship

def test_ship_too_long():
    with pytest.raises(Exception):
        ship = Ship((0, 0), (0, 10))

def test_ship_on_diag():
    with pytest.raises(Exception):
        ship = Ship((0, 0), (2, 2))
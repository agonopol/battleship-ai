from battleship.ship import Ship
from battleship.grid import Grid, State
import pytest, random
import numpy as np

def test_ship_ok():
    ship = Ship((0, 0), (0, 2))
    assert ship

def test_ship_too_long():
    with pytest.raises(Exception):
        ship = Ship((0, 0), (0, 10))

def test_ship_on_diag():
    with pytest.raises(Exception):
        ship = Ship((0, 0), (2, 2))


@pytest.mark.skip(reason="use this for display and debug")
def test_bias():
    # random.seed(1000)
    counts = np.zeros((10, 10))
    for n in range(5000):
        grid = Grid(10)
        for n in [5, 4, 3, 3, 2]:
            ship = Ship.random(10, n)
            while not grid.place(ship):
                ship = Ship.random(10, n)
        for x in range(10):
            for y in range(10):
                if grid.grid[x,y] == State.SHIP:
                    counts[x,y] += 1
    print(counts)

def test_ship_random_ok():
    ship = Ship.random(10, 5)
    assert ship


def test_ship_around_ok():
    ships = Ship.around(10, 3, 3, 5)
    for ship in ships:
        if any([cell[0] < 0 or cell[1] < 0 or cell[0] >= 10 or cell[1] >= 10 for cell in ship.cells]):
            print(ship.cells)
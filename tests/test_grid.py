from battleship.grid import Grid, Outcome
from battleship.ship import Ship

def test_grid_creates_ok():
    grid = Grid(10)
    assert grid.lost( )


def test_grid_places_ship_ok():
    grid = Grid(10)
    assert grid.lost( )
    ship = Ship((0,0), (0, 2))
    grid.place(ship)
    assert grid.ships == 3
    assert not grid.lost( )


def test_grid_places_ship_overlap_not_ok():
    grid = Grid(10)
    assert grid.lost( )
    ship = Ship((0,0), (0, 2))
    grid.place(ship)
    another = Ship((0,1), (2, 1))
    assert not grid.place(another)
    assert grid.ships == 3
    assert not grid.lost( )


def test_grid_shot_miss():
    grid = Grid(10)
    assert grid.lost( )
    ship = Ship((0,0), (0, 2))
    grid.place(ship)
    assert grid.ships == 3
    result = grid.hit(1, 1)
    assert result == Outcome.MISS
    assert grid.ships == 3
    assert not grid.lost( )


def test_grid_shot_hit():
    grid = Grid(10)
    assert grid.lost( )
    ship = Ship((0,0), (0, 2))
    grid.place(ship)
    assert grid.ships == 3
    result = grid.hit(0, 1)
    assert result == Outcome.HIT
    assert grid.ships == 2
    assert not grid.lost( )


def test_grid_shot_invalid_same_spot():
    grid = Grid(10)
    assert grid.lost( )
    ship = Ship((0,0), (0, 2))
    grid.place(ship)
    assert grid.ships == 3
    result = grid.hit(1, 1)
    assert result == Outcome.MISS
    assert grid.ships == 3
    assert not grid.lost( )
    result = grid.hit(1, 1)
    assert result == Outcome.INVALID
    assert grid.ships == 3
    assert not grid.lost( )

def test_grid_shot_and_win():
    grid = Grid(10)
    assert grid.lost( )
    ship = Ship((0,0), (0, 1))
    grid.place(ship)
    assert grid.ships == 2
    result = grid.hit(0, 0)
    assert result == Outcome.HIT
    assert grid.ships == 1
    result = grid.hit(0, 1)
    assert result == Outcome.HIT
    assert grid.lost( )

from battleship.grid import Grid
import sys

def test_display_empty():
    grid = Grid(10)
    grid.display(sys.stdout)

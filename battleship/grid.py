import numpy as np
from enum import IntEnum
import sys


class Outcome(IntEnum):
    INVALID = 0
    MISS = 1
    HIT = 2


class State(IntEnum):
    EMPTY = 0
    MISS = 1
    SHIP = 2
    HIT = 3


class Grid(object):
    def __init__(self, size=10):
        super(Grid, self).__init__()
        self.size = size
        self.grid = np.zeros((size, size))
        self.ships = 0

    def place(self, ship):
        if not all([self.grid[i, j] == State.EMPTY.value for (i, j) in ship.cells]):
            return False
        for (i, j) in ship.cells:
            self.grid[i, j] = State.SHIP
        self.ships += ship.size()
        return True

    def display(self, hidden=False):
        for i in range(self.size):
            sys.stdout.write('\t')
            for j in range(self.size):
                if self.grid[i, j] == State.EMPTY:
                    sys.stdout.write("[ ]")
                elif self.grid[i, j] == State.MISS:
                    sys.stdout.write("[X]")
                elif self.grid[i, j] == State.SHIP:
                    if hidden:
                        sys.stdout.write("[ ]")
                    else:
                        sys.stdout.write("[S]")
                else:
                    sys.stdout.write("[H]")
            sys.stdout.write('\n')

    def lost(self):
        return self.ships == 0

    def hit(self, x, y):
        if x < 0 or x > self.size - 1or y < 0 or y > self.size - 1:
            return Outcome.INVALID
        elif self.grid[x, y] == State.MISS or self.grid[x, y] == State.HIT:
            return Outcome.INVALID
        elif self.grid[x, y] == State.SHIP:
            self.grid[x, y] = State.HIT
            self.ships -= 1
            return Outcome.HIT
        else:
            self.grid[x, y] = State.MISS
            return Outcome.MISS

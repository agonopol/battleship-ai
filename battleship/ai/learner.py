from battleship.ship import Ship
from battleship.grid import Grid
from battleship.ai.player import Player, Outcome
import numpy as np
import random


class Learner(Player):
    def __init__(self, size):
        super(Learner, self).__init__()
        self.size = size
        self.grid = Grid(size)
        self.mask = np.zeros((self.size, self.size))
        self.ships = 0

    def setup(self, ships=(5, 4, 3, 3, 2)):
        self.ships = sum(ships)
        for n in ships:
            ship = Ship.random(self.size, n)
            while not self.grid.place(ship):
                ship = Ship.random(self.size, n)

    def target(self) -> (int, int):
        where = np.where(self.mask == 0)
        choice = random.choice(list(zip(where[0], where[1])))
        self.mask[choice[0], choice[1]] = 1
        return choice[0], choice[1]

    def report(self, x: int, y: int) -> Outcome:
        result = self.grid.hit(x, y)
        if result == Outcome.HIT:
            self.ships -= 1
        return result

    def display(self, hidden=True):
        self.grid.display(hidden=hidden)

    def mark(self, x: int, y: int, result: Outcome):
        pass

    def remaining(self) -> int:
        return self.ships

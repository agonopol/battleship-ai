from battleship.ship import Ship
from battleship.grid import Grid, State
from battleship.ai.player import Player, Outcome
import numpy as np
import random


def valid(mask, ship):
    return not any([mask[cell[0], cell[1]] == State.MISS for cell in ship.cells])


def expected(mask, ships, samples=1000, ratio=.1):
    placements = np.zeros(mask.shape)
    for _ in range(samples):
        for k in ships:
            ship = Ship.random(mask.shape[0], k)
            # Handle misses
            if valid(mask, ship):
                for cell in ship.cells:
                    placements[cell[0], cell[1]] += 1
    for i in range(int(samples * ratio)):
        for x, y in zip(*np.where(mask == State.HIT)):
            for n in ships:
                choices = list(filter(lambda x: valid(mask, x), Ship.around(mask.shape[0], x, y, n)))
                if choices:
                    for cell in random.choice(choices).cells:
                        placements[cell[0], cell[1]] += 1
    placements[mask == State.HIT] = 0
    probibilities = placements / np.sum(placements)
    return np.unravel_index(np.argmax(probibilities), probibilities.shape)


class Counter(Player):
    def __init__(self, size, samples=1000, ratio=.1):
        super(Counter, self).__init__()
        self.size = size
        self.grid = Grid(size)
        self.mask = np.zeros((self.size, self.size))
        self.lives = 0
        self.samples = samples
        self.ratio = ratio
        self.ships = []

    def setup(self, ships=(5, 4, 3, 3, 2)):
        self.grid = Grid(self.size)
        self.ships = ships
        self.mask = np.zeros((self.size, self.size))
        self.lives = sum(ships)
        for n in ships:
            ship = Ship.random(self.size, n)
            while not self.grid.place(ship):
                ship = Ship.random(self.size, n)

    def target(self) -> (int, int):
        return expected(self.mask, self.ships, self.samples, self.ratio)

    def report(self, x: int, y: int) -> Outcome:
        result = self.grid.hit(x, y)
        if result == Outcome.HIT:
            self.lives -= 1
        return result

    def display(self, hidden=True):
        self.grid.display(hidden=hidden)

    def mark(self, x: int, y: int, result: Outcome):
        if result == Outcome.HIT:
            self.mask[x, y] = State.HIT
        elif result == Outcome.MISS:
            self.mask[x, y] = State.MISS

    def remaining(self) -> int:
        return self.lives


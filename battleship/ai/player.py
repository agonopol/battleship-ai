import abc, sys
from battleship.grid import Grid, Outcome
from battleship.ship import Ship


class Player(abc.ABC):

    @abc.abstractmethod
    def setup(self, ships=(5, 4, 3, 3, 2)):
        pass

    @abc.abstractmethod
    def target(self) -> (int, int):
        pass

    @abc.abstractmethod
    def report(self, x: int, y: int) -> Outcome:
        pass

    @abc.abstractmethod
    def display(self, hidden=True):
        pass

    @abc.abstractmethod
    def mark(self, x: int, y: int, result: Outcome):
        pass

    @abc.abstractmethod
    def remaining(self) -> int:
        pass


class Human(Player):

    def __init__(self, size):
        super(Human, self).__init__()
        self.grid = Grid(size)
        self.size = size
        self.ships = 0

    def setup(self, ships=(5, 4, 3, 3, 2)):
        self.grid = Grid(self.size)
        self.ships = sum(ships)
        for n in ships:
            ship = Ship.random(self.size, n)
            while not self.grid.place(ship):
                ship = Ship.random(self.size, n)

    def valid(self, coords):
        if not coords:
            return False
        if not len(coords) == 2:
            return False
        if coords[0] < 0 or coords[0] >= self.size:
            return False
        if coords[1] < 0 or coords[1] >= self.size:
            return False
        return True

    def target(self) -> (int, int):
        coords = None
        while not self.valid(coords):
            try:
                sys.stdout.write(
                    "Please enter comma separated location x,y (between values 0 and %d)\n" % (self.size - 1))
                coords = list(map(int, sys.stdin.readline().strip().split(",")))
            except ValueError:
                coords = None
        return coords[0], coords[1]

    def report(self, x: int, y: int) -> Outcome:
        outcome = self.grid.hit(x, y)
        if outcome == Outcome.HIT:
            self.ships -= 1
        return outcome

    def mark(self, x: int, y: int, result: Outcome):
        pass

    def display(self, hidden=False):
        self.grid.display(hidden=False)

    def remaining(self) -> int:
        return self.ships

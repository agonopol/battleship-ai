import random

class Ship(object):
    def __init__(self, start, end):
        super(Ship, self).__init__()
        if start[0] == end[0]:
            miny, maxy = [start[1], end[1]] if start[1] < end[1] else [end[1], start[1]]
            self.cells = [[start[0], i] for i in range(miny, maxy + 1)]
        elif start[1] == end[1]:
            minx, maxx = [start[0], end[0]] if start[0] < end[0] else [end[0], start[0]]
            self.cells = [[i, start[1]] for i in range(minx, maxx + 1)]
        else:
            raise Exception('Could not form ship on a diagonal from ', start, ' to ', end)
        if len(self.cells) > 5:
            raise Exception('The ship from', start, ' to ', end, ' is larger then 5 pieces.')

    def size(self):
        return len(self.cells)

    @staticmethod
    def random(size, n):
        start = [random.randint(0, size - 1), random.randint(0, size - 1)]
        if random.random() > .5:
            return Ship(start, [start[0], start[1] + n - 1] if start[1] + n - 1 < size else [start[0], start[1] - n + 1])
        else:
            return Ship(start, [start[0] + n - 1, start[1]] if start[0] + n - 1 < size else [start[0] - n + 1, start[1]])


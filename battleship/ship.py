import random
import numpy as np

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
    def random(board_size, n):
        rows = ((board_size - n) * board_size)
        possibilites = rows * 2
        choice = np.random.randint(0, possibilites)
        if choice <= rows:
            #last cell
            if choice == rows:
                return Ship([board_size - 1, board_size - n], [board_size - 1, board_size - 1])
            row = int(choice / ( board_size - n ))
            offset = choice % ( board_size - n )
            return Ship([row, offset], [row, (offset + n) - 1])
        else:
            choice = choice - rows
            if choice == rows:
                return Ship([board_size - n, board_size - 1], [board_size - 1, board_size - 1])
            column = int(choice / ( board_size - n ))
            offset = choice % ( board_size - n )
            return Ship([offset, column], [(offset + n) - 1, column])

    @staticmethod
    def around(board_size, x, y, n):
        for i in range(n):
            if y - i >= 0 and ((y - i) + ( n - 1))  < board_size:
                yield Ship([x, y - i], [x, (y - i) + ( n - 1 )])
            if y + i >= 0 and ((y + i) + ( n - 1))  < board_size:
                yield Ship([x, y + i], [x, (y + i) + ( n - 1)])
        for i in range(n):
            if x - i >= 0 and ((x - i) + ( n - 1))  < board_size:
                yield Ship([x - i, y], [(x - i) + ( n - 1 ), y])
            if x + i >= 0 and ((x + i) + ( n - 1))  < board_size:
                yield Ship([x + i, y], [(x + i) + ( n - 1 ), y])


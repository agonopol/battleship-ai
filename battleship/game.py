from battleship.grid import Outcome
import sys, os


class Game(object):
    def __init__(self, player, opponent, ships=(5, 4, 3, 3, 2)):
        super(Game, self).__init__()
        self.player = player
        self.opponent = opponent
        self.player.setup(ships)
        self.opponent.setup(ships)

    def display(self):
        sys.stdout.write(''.join(['\t', '-' * 12, 'Player', '-' * 12, '\n']))
        self.player.display()
        sys.stdout.write(''.join(['\t', '-' * 11, 'Opponent', '-' * 11, '\n']))
        self.opponent.display(hidden=True)

    def _turn(self, player, opponent, name, clear=False):
        result = Outcome.INVALID
        while result == Outcome.INVALID:
            (x, y) = player.target()
            result = opponent.report(x, y)
            if result == Outcome.INVALID:
                sys.stdout.write("Location %d,%d is not valid.\n" % (x, y))
            else:
                if clear:
                    os.system("clear")
                sys.stdout.write("%s shot at %d,%d\n" % (name, x, y))
        if result == Outcome.HIT:
            sys.stdout.write("%s hit!\n" % name)
        else:
            sys.stdout.write("%s missed!\n" % name)
        if not opponent.remaining():
            sys.stdout.write("%s won!\n" % name)
            return

    def turn(self):
        self._turn(self.player, self.opponent, "You", clear=True)
        self._turn(self.opponent, self.player, "Bot")

    def over(self):
        return not (self.player.remaining() and self.opponent.remaining())

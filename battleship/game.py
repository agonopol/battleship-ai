from battleship.grid import Outcome
import sys, os


class Game(object):
    def __init__(self, player, opponent, logger, ships=(5, 4, 3, 3, 2)):
        super(Game, self).__init__()
        self.logger = logger
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
        (x, y) = (0,0)
        result = Outcome.INVALID
        while result == Outcome.INVALID:
            (x, y) = player.target()
            result = opponent.report(x, y)
            if result == Outcome.INVALID:
                player.mark(x, y, result)
                if clear:
                    self.logger.info("Location %d,%d is not valid." % (x, y))
            else:
                if clear:
                    os.system("clear")
                self.logger.info("%s shot at %d,%d" % (name, x, y))
        if result == Outcome.HIT:
            self.logger.info("%s hit!" % name)
        else:
            self.logger.info("%s missed!" % name)
        if not opponent.remaining():
            self.logger.info("%s won!" % name)
            result = Outcome.WIN
        player.mark(x, y, result)
        return

    def turn(self, clear=False):
        self._turn(self.player, self.opponent, "You", clear)
        self._turn(self.opponent, self.player, "Bot", )

    def over(self):
        return not (self.player.remaining() and self.opponent.remaining())

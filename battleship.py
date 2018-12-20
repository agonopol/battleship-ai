from battleship.game import Game
from battleship.ai.player import Human
from battleship.ai.dummy import Dummy
from battleship.ai.learner import Learner
import random, os, click
import logging

@click.group()
def battleship():
    pass

@battleship.command()
@click.argument('rounds', type=click.INT)
def train(rounds):
    dummy = Dummy( 10 )
    ai = Learner( 10, os.path.join(os.path.dirname(__file__), "models"))

    logger = logging.getLogger('battleship-ai')
    handler = logging.StreamHandler()

    logger.setLevel(logging.ERROR)
    handler.setLevel(logging.ERROR)
    logger.addHandler(handler)

    for round in range(rounds):
        print("Round %d" % round)
        game = Game(dummy, ai, logger)
        while not game.over():
            game.turn()
    ai.save()

@battleship.command()
def play():
    logger = logging.getLogger('battleship-ai')
    handler = logging.StreamHandler()

    logger.setLevel(logging.INFO)
    handler.setLevel(logging.INFO)
    logger.addHandler( handler )

    random.seed(12345)
    learner = Learner(10, os.path.join(os.path.dirname(__file__), "models"))
    game = Game(Human(10), learner, logger)
    game.display()
    while not game.over():
        game.turn(clear=True)
        game.display()
    learner.save()


if __name__ == '__main__':
    battleship()

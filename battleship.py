from battleship.game import Game
from battleship.ai.player import Human
from battleship.ai.dummy import Dummy
from battleship.ai.learner import Learner
import random, os, click
from tqdm import tqdm
import matplotlib.pyplot as plt
import numpy as np
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

    turns = []
    for _ in tqdm(range(rounds)):
        game = Game(dummy, ai, logger)
        turn = 0
        while not game.over():
            game.turn()
            turn += 1
        turns.append(turn)
    mean = np.convolve(turns, np.ones((100,))/100, mode='valid')
    plt.plot(list(range(99, rounds)), mean)
    plt.savefig('rate.png')
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

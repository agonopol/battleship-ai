from battleship.game import Game
from battleship.ai.dummy import Dummy
from battleship.ai.counter import Counter
import click
import matplotlib.pyplot as plt
import logging
from multiprocessing import Pool
import numpy as np

@click.group()
def performance():
    pass

def _samples(samples):
    turns = []
    for i in range(5):
        print(samples, ": round ", i )
        turns.append(0)
        dummy = Dummy(10)

        logger = logging.getLogger('battleship-ai')
        handler = logging.StreamHandler()

        logger.setLevel(logging.ERROR)
        handler.setLevel(logging.ERROR)
        logger.addHandler(handler)

        ai = Counter(10, samples=samples)
        game = Game(ai, dummy, logger)
        while not game.over():
            turns[-1] += 1
            game.turn()
    return sum(turns) / 5

def _weights(w):
    turns = []
    for i in range(5):
        print(w, ": round ", i )
        turns.append(0)
        dummy = Dummy(10)

        logger = logging.getLogger('battleship-ai')
        handler = logging.StreamHandler()

        logger.setLevel(logging.ERROR)
        handler.setLevel(logging.ERROR)
        logger.addHandler(handler)

        ai = Counter(10, samples=100, ratio=w)
        game = Game(ai, dummy, logger)
        while not game.over():
            turns[-1] += 1
            game.turn()
    return sum(turns) / 5

@performance.command()
@click.option('--max', type=click.INT, default=1000)
def samples(max):
    pool = Pool(4)
    x = list(np.arange(100, max, 100))
    y = pool.map(_samples, x)
    plt.plot(x, y, 'ro')
    plt.savefig('samples.png')

@performance.command()
def weights():
    pool = Pool(4)
    x = np.arange(.1, 1.0, .1)
    y = pool.map(_weights, x)
    plt.plot(x, y, 'ro')
    plt.savefig('ratio.png')


if __name__ == '__main__':
    performance()

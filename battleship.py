from battleship.game import Game
from battleship.ai.player import Human
from battleship.ai.dummy import Dummy
import random, os, click


@click.group()
def battleship():
    pass


@battleship.command()
def train():
    '''Command on battleship'''
    click.echo('battleship train')


@battleship.command()
def play():
    '''Command on battleship'''
    random.seed(12345)
    game = Game(Human(10), Dummy(10))
    game.display( )
    while not game.over( ):
        game.turn( )
        game.display( )


if __name__ == '__main__':
    battleship()

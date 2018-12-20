from battleship.ship import Ship
from battleship.grid import Grid
from battleship.ai.player import Player, Outcome
import numpy as np
import os
from tensorforce.agents import PPOAgent


def to_model(size, path):
    return os.path.join(path, "%dx%d" % (size, size), "model")


def agent(size, path):
    path = os.path.dirname(to_model(size, path))
    agent = PPOAgent(states=dict(type='float', shape=(size, size)),
                     actions=dict(type='int', shape=(2,), num_actions=size),
                     network=[
                         dict(type='flatten'),
                         dict(type='dense', size=64),
                         dict(type='dense', size=64)
                     ],
                     batching_capacity=1000,
                     step_optimizer=dict(
                         type='adam',
                         learning_rate=1e-4
                     ))
    if os.path.exists(path):
        print("Loading previous model ... ")
        agent.restore_model(path)
        return agent
    return agent


class Learner(Player):
    def __init__(self, size, path):
        super(Learner, self).__init__()
        self.size = size
        self.grid = Grid(size)
        self.mask = np.zeros((self.size, self.size))
        self.ships = 0
        self.path = path
        self.agent = agent(size, path)

    def save(self):
        path = to_model(self.size, self.path)
        os.makedirs(path, exist_ok=True)
        self.agent.save_model(path, append_timestep=False)

    def setup(self, ships=(5, 4, 3, 3, 2)):
        self.grid = Grid(self.size)
        self.mask = np.zeros((self.size, self.size))
        self.ships = sum(ships)
        for n in ships:
            ship = Ship.random(self.size, n)
            while not self.grid.place(ship):
                ship = Ship.random(self.size, n)

    def target(self) -> (int, int):
        action = self.agent.act(self.mask)
        return action[0], action[1]

    def report(self, x: int, y: int) -> Outcome:
        result = self.grid.hit(x, y)
        if result == Outcome.HIT:
            self.ships -= 1
        return result

    def display(self, hidden=True):
        self.grid.display(hidden=hidden)

    def mark(self, x: int, y: int, result: Outcome):
        if result == Outcome.WIN:
            self.mask[x, y] = 1
            self.agent.observe(reward=1, terminal=True)
        elif result == Outcome.HIT:
            self.mask[x, y] = 1
            self.agent.observe(reward=1, terminal=False)
        elif result == Outcome.MISS:
            self.mask[x, y] = -1
            self.agent.observe(reward=0, terminal=False)
        else:
            self.agent.observe(reward=-1, terminal=False)
        return

    def remaining(self) -> int:
        return self.ships

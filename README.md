# battleship

Battleship AI based on RL using tensorforce

A command line battleship game using reinforcement learning to train the game AI.

Module battleship.ai.learner contains the simple Proximal Policy Optimization learner over the space battleship grid space.
The learner tries to predict from a given configuration of the NxN grid (hit/miss) where the next likely shot should be. 

##### TODO'S
 - Allow user to pick ship location, currently this is random
 - The current model is not optimized, after 1000 iterations of training the average # of shots it takes to finish the game is decreasing but not monotonically, need more time to experiment with layers, and state space

![alt text][logo]

[logo]: https://github.com/agonopol/battleship-ai/raw/master/rate.png "Performance"


## Basic setup

- python3.6
- tensorflow
- tensorfoce

Install the requirements:
```
$ pip install -r requirements.txt
```

Run the application:
```
$ python battleship.py --help
$ python battleship.py play
$ python battleship.py train <training rounds>
```

To run the tests:
```
    $ pytest
```

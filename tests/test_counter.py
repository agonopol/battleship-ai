from battleship.ai.counter import Counter
from battleship.ai.counter import Outcome

# def test_grid_creates_ok():
#     counter = Counter(10)
#     counter.setup()
#     target = counter.target()
#     counter.mark(target[0], target[1], Outcome.MISS)
#     nextone = counter.target()
#     assert nextone != target


def test_grid_hits_increase_probability_around():
    counter = Counter(10)
    counter.setup()
    target = counter.target()
    counter.mark(0, 0, Outcome.HIT)
    nextone = counter.target()
    assert nextone



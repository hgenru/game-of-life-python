import numpy as np
from nose.tools import raises, ok_
from src.live import live
from src.GameOfLife import GameOfLife

def test_flash():
    Space = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
    ])
    expected = np.array([
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ])
    a = GameOfLife(life_function = live, space = Space)
    a.simulate(5)
    ok_(
        np.array_equal(a.get_space(), expected),
        "Flash should flash!"
    )

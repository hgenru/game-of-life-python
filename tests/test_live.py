import numpy as np
from nose.tools import raises, ok_
from src.live import live


@raises(TypeError)
def test_should_raise_type_error_on_zero_none_shape():
    live([0])


@raises(TypeError)
def test_should_raise_type_error_on_zero_zero_shape():
    live([[]])


def test_the_dead_should_not_get_up():
    shape = (3, 3)
    ok_(
        np.array_equal(live(np.zeros(shape)), np.zeros(shape)),
        "Died cells should'nt get up"
    )


def test_alone_cell_should_die():
    space = np.array([
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ])
    ok_(
        np.array_equal(live(space), np.zeros((3, 3))),
        "Alone cell should die"
    )


def test_blok_should_be_always_live():
    space = np.array([
        [0, 0, 0, 0],
        [0, 1, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0],
    ])
    ok_(
        np.array_equal(live(space), space),
        "Block should be always live"
    )


def test_blinker_should_blink():
    space = np.array([
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
    ok_(
        np.array_equal(live(space), expected),
        "Blinker should blink"
    )


def test_beacon_should_live():
    space = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ])
    expected = np.array([
        [0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 1, 0],
        [0, 0, 0, 0, 0, 0],
    ])
    ok_(
        np.array_equal(live(space), expected),
        "Beacon should live"
    )

def test_basic_buffer_bug():
    space = np.array([
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 1],
    ])
    expected = np.array([
        [1, 1, 1],
        [1, 0, 0],
        [0, 1, 0],
    ])
    ok_(
        np.array_equal(live(space), expected),
        "test_basic_buffer_bug not completed"
    )

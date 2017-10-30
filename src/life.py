import numpy as np


def life(space):
    space = np.array(space)
    if not (len(space.shape) == 2 and space.shape[0] >= 1 and space.shape[1] >= 1):
        raise TypeError("space should be non-empty two-dimensional matrix")
    pass

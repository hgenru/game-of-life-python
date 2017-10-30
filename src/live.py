import numpy as np
from scipy.ndimage.filters import generic_filter


def live(space):
    """
    :param space: two-dimensional matrix (non-empty)
    :return: next tick of game space
    """
    space = np.array(space, dtype=bool)
    if not (len(space.shape) == 2 and space.shape[0] >= 1 and space.shape[1] >= 1):
        raise TypeError("space should be non-empty two-dimensional matrix")
    return generic_filter(space, live_filter, size=(3, 3), mode='wrap')


NEIGHBORS_MASK = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
], dtype=bool)


def live_filter(cell_with_neighbors):
    cell_with_neighbors = cell_with_neighbors.reshape(NEIGHBORS_MASK.shape)
    neighbors_count = cell_with_neighbors[NEIGHBORS_MASK].sum()
    if neighbors_count == 2:
        return cell_with_neighbors.item((1, 1))
    if neighbors_count == 3:
        return 1
    if neighbors_count > 3:
        return 0
    return 0

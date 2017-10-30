import numpy as np
from scipy.ndimage.filters import generic_filter

class Game:
    def Render(self, space):
        pass

    def InterruptRender(self):
        pass

    def IsContinueRendering(self):
        return True

    def StartSimulation(self, space, live_func):
        while self.IsContinueRendering():
            modified_space = live_func(space)
            self.Render(modified_space)



def live(space):
    """
    :param space: two-dimensional matrix (non-empty)
    :return: next tick of game space
    """
    space = np.array(space)
    if not (len(space.shape) == 2 and space.shape[0] >= 1 and space.shape[1] >= 1):
        raise TypeError("space should be non-empty two-dimensional matrix")
    return generic_filter(space, live_filter, size=(3, 3))


NEIGHBORS_MASK = np.array([
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
], dtype=bool)


def live_filter(cell_with_neighbors):
    cell_with_neighbors = cell_with_neighbors.reshape(NEIGHBORS_MASK.shape)
    neighbors = cell_with_neighbors[NEIGHBORS_MASK]
    neighbors_count = neighbors.sum()
    if neighbors_count == 2:
        return cell_with_neighbors.item((1, 1))
    if neighbors_count == 3:
        return 1
    if neighbors_count > 3:
        return 0
    return 0

import numpy as np

class GameOfLife(object):
    """
    Base class for game of life
    """
    
    _life_function = 0
    _life_space = [[0]]

    def __init__(self, life_function, space):
        self._life_function = life_function
        self._life_space = np.array(space, dtype=bool)
        if not (len(self._life_space.shape) == 2 and self._life_space.shape[0] >= 1 and self._life_space.shape[1] >= 1):
            raise TypeError("space should be non-empty two-dimensional matrix")

    def render_space(self, space):
        """
        Visualize space
        param space: space to visualization
        """
        pass

    def need_render(self):
        """
        Check render interupt
        return: False if need interupt render
        """
        return False

    def visualize(self):
        """
        Visualize current space state
        """
        self.render_space(self._life_space)

    def set_space(self, space):
        """
        param space: two-dimensional matrix (non-empty)     
        """
        self._life_space = np.array(space, dtype=bool)
        if not (len(self._life_space.shape) == 2 and self._life_space.shape[0] >= 1 and self._life_space.shape[1] >= 1):
            raise TypeError("space should be non-empty two-dimensional matrix")

    def get_space(self):
        """
        Returns current space state
        """
        return self._life_space

    def simulate(self, iterations_count = 1, visualize = False):
        """
        param   iterations_count: iterations count.
                visualize: if True need to visualize each iteration
        """
        for i in range(iterations_count):
            self._life_space = self._life_function(self._life_space)
            if visualize:
                self.render_space(self._life_space)
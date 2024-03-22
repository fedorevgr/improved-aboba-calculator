from numpy import linspace


class Space:
    def __init__(self):

        self._space = None
        self._values = None

    def set_values(self, l_bound, r_bound, solver: callable):
        self._space = linspace(l_bound, r_bound, num=50)
        self._values = [solver(x) for x in self._space]

    def get(self):
        """:return x, y"""
        return self._space, self._values

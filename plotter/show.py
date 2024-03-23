
from plotter.analyzer import Space

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Canvas(FigureCanvasQTAgg, Space):
    def __init__(self):
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.axes = self.fig.add_subplot(111)
        FigureCanvasQTAgg.__init__(self, self.fig)

        Space.__init__(self)

    def show(self, *bounds,  function: callable, x, y, x_e, y_e) -> None:
        self.set_args(*bounds,  function)

        self.add_points(x, y, "r")
        self.add_points(x_e, y_e, "b")

        self.axes.grid(True)
        self.draw()

    def set_args(self, l_bound, r_bound,  function):
        self.axes.cla()
        self.set_values(l_bound, r_bound,  function)

        self.axes.axis("equal")

        self.axes.plot(self._space, self._values)

    def add_points(self, x, y, col: str):
        self.axes.scatter(x, y, c=col, marker="o")




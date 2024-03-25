
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

        self.add_points(x, y, "r", "корни")
        self.add_points(x_e, y_e, "b", "экстремум")

        self.axes.grid(True)

        y_axis = self.axes.axvline(0, color="black", linestyle="--")
        x_axis = self.axes.axhline(0, color="black", linestyle="--")
        x_axis.set_label("Оси")

        self.axes.set_xlabel("x")
        self.axes.set_ylabel("y")

        self.axes.set_title("График функции")

        self.leg = self.axes.legend()
        self.leg.set_title("")

        self.draw()

    def set_args(self, l_bound, r_bound,  function):
        self.axes.cla()
        self.set_values(l_bound, r_bound,  function)

        self.axes.axis("equal")

        self.axes.plot(self._space, self._values)

    def add_points(self, x, y, col: str, name):
        self.scat = self.axes.scatter(x, y, c=col, marker="o")
        self.scat.set_label(name)



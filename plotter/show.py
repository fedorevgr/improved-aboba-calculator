
from plotter.analyzer import Space

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


# def _add_plot_space(self):
#     self.plotSpace = QtWidgets.QListWidget(self.verticalLayoutWidget)
#     self.plotSpace.setMinimumSize(QtCore.QSize(490, 0))  # prev value 600
#     self.plotSpace.setBaseSize(QtCore.QSize(0, 0))
#     self.plotSpace.setObjectName("plotSpace")
#     self.plotAndSettingsBox.addWidget(self.plotSpace)


class Canvas(FigureCanvasQTAgg, Space):
    def __init__(self):
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.axes = self.fig.add_subplot(111)
        FigureCanvasQTAgg.__init__(self, self.fig)

        Space.__init__(self)

    def show(self, *bounds,  function: callable, points: tuple[float] = None) -> None:
        self.set_args(*bounds,  function)
        self.add_points()
        self.axes.grid(True)
        self.draw()

    def set_args(self, l_bound, r_bound,  function):
        self.axes.cla()
        self.set_values(l_bound, r_bound,  function)

        self.axes.axis("equal")

        self.axes.plot(self._space, self._values)

    def add_points(self):
        self.axes.scatter((0, 0), (1, 2), c="r", marker="o")




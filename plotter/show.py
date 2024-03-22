from matplotlib import pyplot as plt
from plotter.analyzer import Space

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


# def _add_plot_space(self):
#     self.plotSpace = QtWidgets.QListWidget(self.verticalLayoutWidget)
#     self.plotSpace.setMinimumSize(QtCore.QSize(490, 0))  # prev value 600
#     self.plotSpace.setBaseSize(QtCore.QSize(0, 0))
#     self.plotSpace.setObjectName("plotSpace")
#     self.plotAndSettingsBox.addWidget(self.plotSpace)


class Shower(FigureCanvasQTAgg):
    def __init__(self):
        super().__init__()
        self.fig, self.ax = plt.subplots()
        self.ax.grid()

    def set_args(self, l_bound, r_bound,  function):
        self.set_values(l_bound, r_bound,  function)

        self.ax.plot(self._space, self._values)

    @classmethod
    def show(cls):
        plt.show()

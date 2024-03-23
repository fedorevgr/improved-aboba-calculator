from PyQt5 import QtWidgets, QtCore


class ListWidget(QtWidgets.QTableWidget):
    INT_WIDTH = 90
    FLOAT_WIDTH = 180
    SEGMENT_WIDTH = 220

    def __init__(self, parent):
        super().__init__(parent)
        self.setMaximumSize(QtCore.QSize(16777215, 200))
        self.setObjectName("solutionsList")

        print(self.INT_WIDTH * 2 + self.FLOAT_WIDTH * 2 + self.SEGMENT_WIDTH)

"""
self.solutionsList.setColumnCount(5)
        self.solutionsList.setHorizontalHeaderLabels(("Отрезок", "x", "f(x)", "Итер.", "Ошибка"))

        self.solutionsList.setColumnWidth(0, self.solutionsList.SEGMENT_WIDTH)
        self.solutionsList.setColumnWidth(1, self.solutionsList.FLOAT_WIDTH)
        self.solutionsList.setColumnWidth(2, self.solutionsList.FLOAT_WIDTH)
        self.solutionsList.setColumnWidth(3, self.solutionsList.INT_WIDTH)
        self.solutionsList.setColumnWidth(4, self.solutionsList.INT_WIDTH)

        self.solutionsList.setRowCount(len(solutions))
        self.solutionsList.setVerticalHeaderLabels([str(x) for x in range(1, len(solutions) + 1)])
        """
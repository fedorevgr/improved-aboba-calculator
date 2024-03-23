from PyQt5 import QtWidgets, QtCore


class ListWidget(QtWidgets.QTableWidget):
    INT_WIDTH = 90
    FLOAT_WIDTH = 170
    SEGMENT_WIDTH = 220

    def __init__(self, parent):
        super().__init__(parent)
        self.setMaximumSize(QtCore.QSize(16777215, 200))
        self.setObjectName("solutionsList")

        print(self.INT_WIDTH * 2 + self.FLOAT_WIDTH * 2 + self.SEGMENT_WIDTH)

    def setup(self, headers):
        self.setRowCount(5)

        # self.setColumnWidth(0, INT_WIDTH)
        # self.setColumnWidth(1, SEGMENT_WIDTH)
        # self.setColumnWidth(2, FLOAT_WIDTH)
        # self.setColumnWidth(3, FLOAT_WIDTH)
        # self.setColumnWidth(4, INT_WIDTH)
        # self.setColumnWidth(5, INT_WIDTH)

        self.setHorizontalHeaderLabels(headers)

from PyQt5 import QtWidgets, QtCore


INT_WIDTH = 50
FLOAT_WIDTH = 150
SEGMENT_WIDTH = 200


class ListWidget(QtWidgets.QTableWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.setMaximumSize(QtCore.QSize(16777215, 200))
        self.setObjectName("solutionsList")

        print(INT_WIDTH * 3 + FLOAT_WIDTH * 2 + SEGMENT_WIDTH)

    def setup(self, headers):
        self.setRowCount(6)

        # self.setColumnWidth(0, INT_WIDTH)
        # self.setColumnWidth(1, SEGMENT_WIDTH)
        # self.setColumnWidth(2, FLOAT_WIDTH)
        # self.setColumnWidth(3, FLOAT_WIDTH)
        # self.setColumnWidth(4, INT_WIDTH)
        # self.setColumnWidth(5, INT_WIDTH)

        self.setHorizontalHeaderLabels(headers)

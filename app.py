from PyQt5.QtWidgets import QApplication, QTableWidgetItem
from sys import argv

from calculator.interface import Interface

from plotter.show import Canvas

from gui.ui import CalculatorUI

from gui.src.Exceptions import *
from calculator import exceptions

from gui.src import Filter


class App(Interface, CalculatorUI):
    def __init__(self):
        Interface.__init__(self)
        CalculatorUI.__init__(self)

        self.plot = Canvas()

        self.plotAndSettingsBox.addWidget(self.plot)

        self._edits = {
            "functionEditLine": self.functionEditLine,
            "leftBoundEdit": self.leftBoundEdit,
            "rightBoundEdit": self.rightBoundEdit,
            "stepEdit": self.stepEdit,
            "maxIterEdit": self.maxIterEdit,
            "epsEdit": self.epsEdit
        }

        self._parameters = {
            "leftBound": 0.0,
            "rightBound": 0.0,
            "step": 0.0,
            "maxIter": 0,
            "eps": 0.0
        }

        self.computeButton.clicked.connect(self._on_compute_pressed)

    def _check_values(self):
        self.set_expression(self.functionEditLine.text())

        for name in ["leftBoundEdit", "rightBoundEdit", "stepEdit", "epsEdit"]:
            self._parameters[name[:-4]] = Filter.check_float(self._edits[name].text(), name)

        self._parameters["maxIter"] = Filter.check_int(self.maxIterEdit.text(), "maxIterEdit")

    def _draw_table(self, solutions):

        self.setup(len(solutions))

        for row, solution in enumerate(solutions):
            self.solutionsList.setItem(row, 0, QTableWidgetItem(solution[0]))
            error = solution[-1] > 0
            for col in range(1, 5):
                if error and 1 <= col <= 2:
                    continue
                self.solutionsList.setItem(row, col, QTableWidgetItem(f"{solution[col]:g}"))

    def _on_compute_pressed(self):
        self.solutionsList.clear()
        for edit in self._edits.values():
            edit.setStyleSheet("color: black; border: 1px solid black;")

        try:
            self._check_values()
            solutions = self.solver.find_solution(
                self._parameters["leftBound"],
                self._parameters["rightBound"],
                self._parameters["step"],
                self._parameters["eps"],
                self._parameters["maxIter"],
                self.functionEditLine.text()
            )
            extreme_points = self.solver.extreme_points(
                self._parameters["leftBound"],
                self._parameters["rightBound"],
                self.functionEditLine.text()
            )
            self.plot.show(
                self._parameters["leftBound"], self._parameters["rightBound"],
                function=self.solver.F,
                x=[x[1] for x in solutions],
                y=[x[2] for x in solutions],
                x_e=extreme_points[0],
                y_e=extreme_points[1]
            )
            self._draw_table(solutions)

        except InvalidNumber as setting_exception:
            self._edits[setting_exception.type].setStyleSheet("color: red; border: 1px solid red;")
        except exceptions.ParseExceptions as func_exception:
            self.functionEditLine.setStyleSheet("color: red; border: 1px solid red;")
            func_exception.message = str(func_exception)

    def setup(self, rows):
        self.solutionsList.setColumnCount(5)
        self.solutionsList.setHorizontalHeaderLabels(("Отрезок", "x", "f(x)", "Итер.", "Ошибка"))

        self.solutionsList.setColumnWidth(0, self.solutionsList.SEGMENT_WIDTH)
        self.solutionsList.setColumnWidth(1, self.solutionsList.FLOAT_WIDTH)
        self.solutionsList.setColumnWidth(2, self.solutionsList.FLOAT_WIDTH)
        self.solutionsList.setColumnWidth(3, self.solutionsList.INT_WIDTH)
        self.solutionsList.setColumnWidth(4, self.solutionsList.INT_WIDTH)

        self.solutionsList.setRowCount(rows)
        self.solutionsList.setVerticalHeaderLabels([str(x) for x in range(1, rows + 1)])


def main():

    app = QApplication(argv)
    calc = App()
    calc.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()

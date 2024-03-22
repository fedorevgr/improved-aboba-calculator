from PyQt5.QtWidgets import QApplication
from sys import argv

from calculator.interface import Interface

from plotter.show import Shower

from gui.ui import CalculatorUI

from gui.src.Exceptions import *
from calculator import exceptions

from gui.src import Filter


class App(Interface, CalculatorUI):
    def __init__(self):
        Interface.__init__(self)
        CalculatorUI.__init__(self)

        self.drawer = Shower()

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

    def _on_compute_pressed(self):
        for edit in self._edits.values():
            edit.setStyleSheet("color: black; border: 1px solid black;")

        try:
            self._check_values()
            self.drawer.set_args(self._parameters["leftBound"], self._parameters["rightBound"], self.solver.F)
            self.drawer.show()
        except InvalidNumber as setting_exception:
            self._edits[setting_exception.type].setStyleSheet("color: red; border: 1px solid red;")
        except exceptions.ParseExceptions as func_exception:
            self.functionEditLine.setStyleSheet("color: red; border: 1px solid red;")
            func_exception.message = str(func_exception)


def main():

    app = QApplication(argv)
    calc = App()
    calc.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()

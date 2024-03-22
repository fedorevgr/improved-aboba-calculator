from PyQt5.QtWidgets import QApplication
from sys import argv

from calculator.interface import Interface
from gui.ui import CalculatorUI

from gui.src.Exceptions import *
from calculator import exceptions

from gui.src import Filter


class App(Interface, CalculatorUI):
    def __init__(self):
        super().__init__()

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

        self.computeButton.clicked.connect(self._on_compute_pressed())

    def _check_values(self):
        self.set_expression(self.functionEditLine.text())

        for name in ["leftBoundEdit", "rightBoundEdit", "stepEdit", "epsEdit"]:
            self._parameters[name[:-4]] = Filter.check_float(self._edit[name], name)

        self._parameters["maxIter"] = Filter.check_int(self.maxIterEdit, "maxIterEdit")

    def _on_compute_pressed(self):
        for edit in self._edits.values():
            edit.setStyleSheet("color: black;")

        try:
            self._check_values()
        except InvalidNumber as exception:
            self._edits[exception].setStyleSheet("color: red;")
        except exceptions.EmptyExpression:
            pass
        except exceptions.NoClosureBracket:
            pass
        except exceptions.OperatorEnding:
            pass
def main():
    app = QApplication(argv)
    calc = App()
    calc.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()
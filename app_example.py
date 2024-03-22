from PyQt5.QtWidgets import QApplication

from sys import argv, exit
from gui.ui import CalculatorUI


def main():
    app = QApplication(argv)
    calc = CalculatorUI()
    calc.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()

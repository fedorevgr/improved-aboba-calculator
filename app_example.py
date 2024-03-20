from PyQt5.QtWidgets import QApplication
from sys import version, argv, exit
from gui.ui import CalculatorUI
from gui.InfoWindow import InfoUI


def main():
    app = QApplication(argv)
    calc = CalculatorUI()
    #calc = InfoUI()
    calc.show()
    exit(app.exec_())


if __name__ == '__main__':
    main()

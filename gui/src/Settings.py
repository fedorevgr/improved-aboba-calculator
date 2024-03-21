from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QShortcut, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QGridLayout


def _create_font(size):
    font = QtGui.QFont()
    font.setPointSize(size)
    return font


class SettingLabel(QLabel):

    def __init__(self, name: str, parent: QWidget):
        self.__FONT = _create_font(20)

        super().__init__(parent)
        self.setFont(self.SETTINGS_FONT)
        self.maxIterLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.setObjectName(name)


class SettingsEdit(QLineEdit):
    def __init__(self, name: str, parent: QWidget):
        self.__FONT = _create_font(25)

        super().__init__(parent)
        self.setFont(self.__FONT)
        self.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.setObjectName(name)


class ComputeButton(QPushButton):
    def __init__(self, parent: QPushButton):
        ...

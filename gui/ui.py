# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prog.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QShortcut, QMainWindow, QPushButton, QVBoxLayout, QWidget, QLineEdit, QGridLayout


class CalculatorUI(QMainWindow):

    def __init__(self):
        self.SETTINGS_FONT = self._create_font(20)

        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 800)

        self.setFont(self._create_font())

        self._add_main_widget()

        self._add_function_box()

        self._add_plot_and_settings_box()

        self._add_solutions_list()

        self._add_menu_button()

        self.setCentralWidget(self.mainWidget)

        self._add_names()
        QtCore.QMetaObject.connectSlotsByName(self)

    def _add_main_widget(self):
        self.mainWidget = QtWidgets.QWidget(self)
        self.mainWidget.setObjectName("mainWidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.mainWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 780, 731))  # prev value 10, 40, 944, 731
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.UI = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.UI.setContentsMargins(0, 0, 0, 0)
        self.UI.setObjectName("UI")

    def _add_function_box(self):
        self.functionEditBox = QtWidgets.QHBoxLayout()
        self.functionEditBox.setObjectName("functionEditBox")

        self._add_y_label()
        self._add_function_edit()

        self.UI.addLayout(self.functionEditBox)

    def _add_y_label(self):
        self.y = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.y.setFont(self._create_font(30))
        self.y.setObjectName("y")
        self.functionEditBox.addWidget(self.y)

    def _add_function_edit(self):
        self.functionEditLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)

        self.functionEditLine.setFont(self._create_font(30))
        self.functionEditLine.setObjectName("functionEditLine")
        self.functionEditBox.addWidget(self.functionEditLine)

    def _add_plot_and_settings_box(self):
        self.plotAndSettingsBox = QtWidgets.QHBoxLayout()
        self.plotAndSettingsBox.setObjectName("plotAndSettingsBox")

        self._add_settings_box()

        self._add_plot_space()

        self.UI.addLayout(self.plotAndSettingsBox)

    def _add_settings_box(self):
        self.settingsBox = QtWidgets.QVBoxLayout()
        self.settingsBox.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.settingsBox.setContentsMargins(0, -1, 0, -1)
        self.settingsBox.setObjectName("settingsBox")

        self._add_left_bound_label()
        self._add_left_bound_edit()
        self._add_right_bound_label()
        self._add_right_bound_edit()
        self._add_step_label()
        self._add_step_edit()
        self._add_max_iter_label()
        self._add_max_iter_edit()
        self._add_eps_label()
        self._add_eps_edit()
        self._add_compute_button()

        self.plotAndSettingsBox.addLayout(self.settingsBox)

    def _add_left_bound_label(self):
        self.leftBoundLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.leftBoundLabel.setFont(self.SETTINGS_FONT)
        self.leftBoundLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leftBoundLabel.setTextFormat(QtCore.Qt.AutoText)
        self.leftBoundLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.leftBoundLabel.setObjectName("leftBoundLabel")
        self.settingsBox.addWidget(self.leftBoundLabel)

    def _add_left_bound_edit(self):
        self.leftBoundEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBoundEdit.sizePolicy().hasHeightForWidth())

        self.leftBoundEdit.setSizePolicy(sizePolicy)
        self.leftBoundEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.leftBoundEdit.setMaximumSize(QtCore.QSize(1600, 16777215))

        self.leftBoundEdit.setFont(self.SETTINGS_FONT)
        self.leftBoundEdit.setObjectName("leftBoundEdit")
        self.settingsBox.addWidget(self.leftBoundEdit)

    def _add_right_bound_label(self):
        self.rigthBoundLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.rigthBoundLabel.setFont(self.SETTINGS_FONT)
        self.rigthBoundLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.rigthBoundLabel.setObjectName("rigthBoundLabel")
        self.settingsBox.addWidget(self.rigthBoundLabel)

    def _add_right_bound_edit(self):
        self.rightBoundEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.rightBoundEdit.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.rightBoundEdit.setFont(self.SETTINGS_FONT)
        self.rightBoundEdit.setObjectName("rightBoundEdit")
        self.settingsBox.addWidget(self.rightBoundEdit)

    def _add_step_label(self):
        self.stepLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.stepLabel.setFont(self.SETTINGS_FONT)
        self.stepLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.stepLabel.setObjectName("stepLabel")
        self.settingsBox.addWidget(self.stepLabel)

    def _add_step_edit(self):
        self.stepEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.stepEdit.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.stepEdit.setFont(self.SETTINGS_FONT)
        self.stepEdit.setObjectName("stepEdit")
        self.settingsBox.addWidget(self.stepEdit)

    def _add_max_iter_label(self):
        self.maxIterLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.maxIterLabel.setFont(self.SETTINGS_FONT)
        self.maxIterLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.maxIterLabel.setObjectName("maxIterLabel")
        self.settingsBox.addWidget(self.maxIterLabel)

    def _add_max_iter_edit(self):
        self.maxIterEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.maxIterEdit.setMaximumSize(QtCore.QSize(1600, 16777215))
        self.maxIterEdit.setFont(self.SETTINGS_FONT)
        self.maxIterEdit.setObjectName("maxIterEdit")
        self.settingsBox.addWidget(self.maxIterEdit)

    def _add_eps_label(self):
        self.epsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.epsLabel.setFont(self.SETTINGS_FONT)
        self.epsLabel.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft)
        self.epsLabel.setObjectName("epsLabel")
        self.settingsBox.addWidget(self.epsLabel)

    def _add_eps_edit(self):
        self.epsEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.epsEdit.setFont(self.SETTINGS_FONT)
        self.epsEdit.setObjectName("epsEdit")
        self.settingsBox.addWidget(self.epsEdit)

    def _add_compute_button(self):
        self.computeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.computeButton.setMinimumSize(QtCore.QSize(40, 40))
        self.computeButton.setFont(self.SETTINGS_FONT)
        self.computeButton.setIconSize(QtCore.QSize(16, 20))
        self.computeButton.setDefault(False)
        self.computeButton.setFlat(False)
        self.computeButton.setObjectName("computeButton")
        self.settingsBox.addWidget(self.computeButton)

    def _add_plot_space(self):
        self.plotSpace = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.plotSpace.setMinimumSize(QtCore.QSize(490, 0))  # prev value 600
        self.plotSpace.setBaseSize(QtCore.QSize(0, 0))
        self.plotSpace.setObjectName("plotSpace")
        self.plotAndSettingsBox.addWidget(self.plotSpace)

    def _add_solutions_list(self):
        self.solutionsList = QtWidgets.QListView(self.verticalLayoutWidget)
        self.solutionsList.setMaximumSize(QtCore.QSize(16777215, 200))
        self.solutionsList.setObjectName("solutionsList")
        self.UI.addWidget(self.solutionsList)

    def _add_menu_button(self):
        self.Menu = QtWidgets.QPushButton(self.mainWidget)
        self.Menu.setGeometry(QtCore.QRect(0, 0, 100, 32))
        self.Menu.setObjectName("Menu")

    @classmethod
    def _create_font(cls, size: int = 13, Bold: bool = False, Italic: bool = False) -> QtGui.QFont:
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(Bold)
        font.setItalic(Italic)
        return font

    def _add_names(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.y.setText(_translate("MainWindow", "y="))
        self.functionEditLine.setText(_translate("MainWindow", "Function(x)"))
        self.leftBoundLabel.setText(_translate("MainWindow", "Левая граница:"))
        self.leftBoundEdit.setText(_translate("MainWindow", "граница"))
        self.rigthBoundLabel.setText(_translate("MainWindow", "Правая граница:"))
        self.rightBoundEdit.setText(_translate("MainWindow", "граница"))
        self.stepLabel.setText(_translate("MainWindow", "Шаг:"))
        self.stepEdit.setText(_translate("MainWindow", "шаг"))
        self.maxIterLabel.setText(_translate("MainWindow", "Max кол-во итераций:"))
        self.maxIterEdit.setText(_translate("MainWindow", "iter"))
        self.epsLabel.setText(_translate("MainWindow", "Точность:"))
        self.epsEdit.setText(_translate("MainWindow", "eps"))
        self.computeButton.setText(_translate("MainWindow", "Вычислить"))


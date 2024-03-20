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
        SETTINGS_FONT = self._create_font(20)

        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 800)

        self.setFont(self._create_font())

        self.mainWidget = QtWidgets.QWidget(self)
        self.mainWidget.setObjectName("mainWidget")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.mainWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 944, 731))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")

        self.UI = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.UI.setContentsMargins(0, 0, 0, 0)
        self.UI.setObjectName("UI")

        self.functionEditBox = QtWidgets.QHBoxLayout()
        self.functionEditBox.setObjectName("functionEditBox")

        self.y = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.y.setFont(self._create_font(30))
        self.y.setObjectName("y")
        self.functionEditBox.addWidget(self.y)

        self.fuctionEditLine = QtWidgets.QLineEdit(self.verticalLayoutWidget)

        self.fuctionEditLine.setFont(self._create_font(30))
        self.fuctionEditLine.setObjectName("fuctionEditLine")
        self.functionEditBox.addWidget(self.fuctionEditLine)
        self.UI.addLayout(self.functionEditBox)

        self.plotAndSettingsBox = QtWidgets.QHBoxLayout()
        self.plotAndSettingsBox.setObjectName("plotAndSettingsBox")

        self.settingsBox = QtWidgets.QVBoxLayout()
        self.settingsBox.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.settingsBox.setContentsMargins(0, -1, 0, -1)
        self.settingsBox.setObjectName("settingsBox")

        self.leftBoundLabel = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.leftBoundLabel.setFont(SETTINGS_FONT)
        self.leftBoundLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.leftBoundLabel.setTextFormat(QtCore.Qt.AutoText)
        self.leftBoundLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.leftBoundLabel.setObjectName("leftBoundLabel")
        self.settingsBox.addWidget(self.leftBoundLabel)

        self.leftBoundEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftBoundEdit.sizePolicy().hasHeightForWidth())

        self.leftBoundEdit.setSizePolicy(sizePolicy)
        self.leftBoundEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.leftBoundEdit.setMaximumSize(QtCore.QSize(1600, 16777215))

        self.leftBoundEdit.setFont(SETTINGS_FONT)
        self.leftBoundEdit.setObjectName("leftBoundEdit")
        self.settingsBox.addWidget(self.leftBoundEdit)
        self.rigthBoundLabel = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.rigthBoundLabel.setFont(SETTINGS_FONT)
        self.rigthBoundLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.rigthBoundLabel.setObjectName("rigthBoundLabel")
        self.settingsBox.addWidget(self.rigthBoundLabel)
        self.rightBoundEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.rightBoundEdit.setMaximumSize(QtCore.QSize(1600, 16777215))

        self.rightBoundEdit.setFont(SETTINGS_FONT)
        self.rightBoundEdit.setObjectName("rightBoundEdit")
        self.settingsBox.addWidget(self.rightBoundEdit)
        self.stepLabel = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.stepLabel.setFont(SETTINGS_FONT)
        self.stepLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.stepLabel.setObjectName("stepLabel")
        self.settingsBox.addWidget(self.stepLabel)
        self.stepEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.stepEdit.setMaximumSize(QtCore.QSize(1600, 16777215))

        self.stepEdit.setFont(SETTINGS_FONT)
        self.stepEdit.setObjectName("stepEdit")
        self.settingsBox.addWidget(self.stepEdit)
        self.maxIterLabel = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.maxIterLabel.setFont(SETTINGS_FONT)
        self.maxIterLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.maxIterLabel.setObjectName("maxIterLabel")
        self.settingsBox.addWidget(self.maxIterLabel)

        self.maxIterEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.maxIterEdit.setMaximumSize(QtCore.QSize(1600, 16777215))

        self.maxIterEdit.setFont(SETTINGS_FONT)
        self.maxIterEdit.setObjectName("maxIterEdit")
        self.settingsBox.addWidget(self.maxIterEdit)

        self.epsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)

        self.epsLabel.setFont(SETTINGS_FONT)
        self.epsLabel.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.epsLabel.setObjectName("epsLabel")
        self.settingsBox.addWidget(self.epsLabel)

        self.epsEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)

        self.epsEdit.setFont(SETTINGS_FONT)
        self.epsEdit.setObjectName("epsEdit")
        self.settingsBox.addWidget(self.epsEdit)

        self.computeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.computeButton.setMinimumSize(QtCore.QSize(40, 40))

        self.computeButton.setFont(SETTINGS_FONT)
        self.computeButton.setIconSize(QtCore.QSize(16, 20))
        self.computeButton.setDefault(False)
        self.computeButton.setFlat(False)
        self.computeButton.setObjectName("computeButton")
        self.settingsBox.addWidget(self.computeButton)

        self.plotAndSettingsBox.addLayout(self.settingsBox)

        self.plotSpace = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.plotSpace.setMinimumSize(QtCore.QSize(600, 0))
        self.plotSpace.setBaseSize(QtCore.QSize(0, 0))
        self.plotSpace.setObjectName("plotSpace")
        self.plotAndSettingsBox.addWidget(self.plotSpace)
        self.UI.addLayout(self.plotAndSettingsBox)

        self.solutionsList = QtWidgets.QListView(self.verticalLayoutWidget)
        self.solutionsList.setMaximumSize(QtCore.QSize(16777215, 200))
        self.solutionsList.setObjectName("solutionsList")
        self.UI.addWidget(self.solutionsList)

        self.Menu = QtWidgets.QPushButton(self.mainWidget)
        self.Menu.setGeometry(QtCore.QRect(10, 10, 100, 32))
        self.Menu.setObjectName("Menu")

        self.setCentralWidget(self.mainWidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    @classmethod
    def _create_font(cls, size: int = 13, Bold: bool = False, Italic: bool = False) -> QtGui.QFont:
        font = QtGui.QFont()
        font.setPointSize(size)
        font.setBold(Bold)
        font.setItalic(Italic)
        return font

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.y.setText(_translate("MainWindow", "y="))
        self.fuctionEditLine.setText(_translate("MainWindow", "Function(x)"))
        self.leftBoundLabel.setText(_translate("MainWindow", "Левая граница:"))
        self.leftBoundEdit.setText(_translate("MainWindow", "граница"))
        self.rigthBoundLabel.setText(_translate("MainWindow", "Правая граница:"))
        self.rightBoundEdit.setText(_translate("MainWindow", "граница"))
        self.stepLabel.setText(_translate("MainWindow", "Шаг:"))
        self.stepEdit.setText(_translate("MainWindow", "шаг"))
        self.maxIterLabel.setText(_translate("MainWindow", "Max количество итераций:"))
        self.maxIterEdit.setText(_translate("MainWindow", "iter"))
        self.epsLabel.setText(_translate("MainWindow", "Точность:"))
        self.epsEdit.setText(_translate("MainWindow", "eps"))
        self.computeButton.setText(_translate("MainWindow", "Вычислить"))


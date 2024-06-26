
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QMenu, QAction

from gui.src import Settings
from gui.src import InfoWindow
from gui.src import Listing


class CalculatorUI(QMainWindow):

    def __init__(self):

        self.SETTINGS_FONT = self._create_font(20)

        self._info_window = InfoWindow.InfoUI()

        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(800, 800)

        self.setFont(self._create_font())

        self._add_main_widget()

        self._add_function_box()

        self._add_plot_and_settings_box()

        self._add_solutions_list()

        self.menu = self.menuBar()
        self.info = QMenu("&Справка", self)

        self.act = QAction(text="Информация")
        self.act.triggered.connect(self._info_window.show)
        self.info.addAction(self.act)

        self.menu.addMenu(self.info)
        # self._add_menu_button()

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
        self.leftBoundLabel = Settings.SettingLabel("leftBoundLabel", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.leftBoundLabel)

    def _add_left_bound_edit(self):
        self.leftBoundEdit = Settings.SettingsEdit("leftBoundEdit", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.leftBoundEdit)

    def _add_right_bound_label(self):
        self.rightBoundLabel = Settings.SettingLabel("rightBoundLabel", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.rightBoundLabel)

    def _add_right_bound_edit(self):
        self.rightBoundEdit = Settings.SettingsEdit("rightBoundEdit", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.rightBoundEdit)

    def _add_step_label(self):
        self.stepLabel = Settings.SettingLabel("stepLabel", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.stepLabel)

    def _add_step_edit(self):
        self.stepEdit = Settings.SettingsEdit("stepEdit", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.stepEdit)

    def _add_max_iter_label(self):
        self.maxIterLabel = Settings.SettingLabel("maxIterLabel", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.maxIterLabel)

    def _add_max_iter_edit(self):
        self.maxIterEdit = Settings.SettingsEdit("maxIterEdit", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.maxIterEdit)

    def _add_eps_label(self):
        self.epsLabel = Settings.SettingLabel("epsLabel", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.epsLabel)

    def _add_eps_edit(self):
        self.epsEdit = Settings.SettingsEdit("epsEdit", self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.epsEdit)

    def _add_compute_button(self):
        self.computeButton = Settings.ComputeButton(self.verticalLayoutWidget)
        self.settingsBox.addWidget(self.computeButton)

    def _add_solutions_list(self):
        self.solutionsList = Listing.ListWidget(self.verticalLayoutWidget)
        self.UI.addWidget(self.solutionsList)

    def _add_menu_button(self):
        self.Menu = QtWidgets.QPushButton(self.mainWidget)
        self.Menu.setGeometry(QtCore.QRect(0, 0, 100, 32))
        self.Menu.setObjectName("Menu")
        self.Menu.clicked.connect(self._info_window.show)

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
        self.rightBoundLabel.setText(_translate("MainWindow", "Правая граница:"))
        self.rightBoundEdit.setText(_translate("MainWindow", "граница"))
        self.stepLabel.setText(_translate("MainWindow", "Шаг:"))
        self.stepEdit.setText(_translate("MainWindow", "шаг"))
        self.maxIterLabel.setText(_translate("MainWindow", "Max кол-во итераций:"))
        self.maxIterEdit.setText(_translate("MainWindow", "iter"))
        self.epsLabel.setText(_translate("MainWindow", "Точность:"))
        self.epsEdit.setText(_translate("MainWindow", "eps"))
        self.computeButton.setText(_translate("MainWindow", "Вычислить"))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# https://www.youtube.com/watch?v=LStHozI2aDo&t=0s

from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
import seaborn as sns
import pandas as pd
import sip

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 680)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 3, 816, 623))
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(758, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 358, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.MaxValueSlider = QtWidgets.QSlider(self.widget)
        self.MaxValueSlider.setSliderPosition(95)
        self.MaxValueSlider.setOrientation(QtCore.Qt.Vertical)
        self.MaxValueSlider.setObjectName("MaxValueSlider")
        self.horizontalLayout_4.addWidget(self.MaxValueSlider)
        self.verticalLayout_8.addLayout(self.horizontalLayout_4)
        self.ResponseValueSlider = QtWidgets.QSlider(self.widget)
        self.ResponseValueSlider.setMaximum(8000)
        self.ResponseValueSlider.setSliderPosition(10)
        self.ResponseValueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ResponseValueSlider.setObjectName("ResponseValueSlider")
        self.verticalLayout_8.addWidget(self.ResponseValueSlider)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.step_var_layout = QtWidgets.QLabel(self.widget)
        self.step_var_layout.setObjectName("step_var_layout")
        self.verticalLayout_2.addWidget(self.step_var_layout)
        self.Response_var_layout = QtWidgets.QLabel(self.widget)
        self.Response_var_layout.setObjectName("Response_var_layout")
        self.verticalLayout_2.addWidget(self.Response_var_layout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.StepVarBox = QtWidgets.QComboBox(self.widget)
        self.StepVarBox.setObjectName("StepVarBox")
        self.StepVarBox.addItem("")
        self.StepVarBox.addItem("")
        self.verticalLayout.addWidget(self.StepVarBox)
        self.ResponseVarBox = QtWidgets.QComboBox(self.widget)
        self.ResponseVarBox.setObjectName("ResponseVarBox")
        self.verticalLayout.addWidget(self.ResponseVarBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.checkBox_enable_sliders = QtWidgets.QCheckBox(self.widget)
        self.checkBox_enable_sliders.setObjectName("checkBox_enable_sliders")
        self.verticalLayout_3.addWidget(self.checkBox_enable_sliders)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.spinBox = QtWidgets.QSpinBox(self.widget)
        self.spinBox.setMaximumSize(QtCore.QSize(75, 16777215))
        self.spinBox.setMaximum(100000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_6.addWidget(self.spinBox)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.widget)
        self.doubleSpinBox.setMaximumSize(QtCore.QSize(75, 16777215))
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_5.addWidget(self.doubleSpinBox)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pB_calculate = QtWidgets.QPushButton(self.widget)
        self.pB_calculate.setObjectName("pB_calculate")
        self.horizontalLayout_2.addWidget(self.pB_calculate)
        self.pB_reset = QtWidgets.QPushButton(self.widget)
        self.pB_reset.setObjectName("pB_reset")
        self.horizontalLayout_2.addWidget(self.pB_reset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_4)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.resultBox = QtWidgets.QTextBrowser(self.widget)
        self.resultBox.setObjectName("resultBox")
        self.verticalLayout_5.addWidget(self.resultBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pB_save = QtWidgets.QPushButton(self.widget)
        self.pB_save.setObjectName("pB_save")
        self.horizontalLayout_3.addWidget(self.pB_save)
        spacerItem5 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pB_clear = QtWidgets.QPushButton(self.widget)
        self.pB_clear.setObjectName("pB_clear")
        self.horizontalLayout_3.addWidget(self.pB_clear)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuImport = QtWidgets.QMenu(self.menubar)
        self.menuImport.setObjectName("menuImport")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionPDF = QtWidgets.QAction(MainWindow)
        self.actionPDF.setObjectName("actionPDF")
        self.actionCustom = QtWidgets.QAction(MainWindow)
        self.actionCustom.setObjectName("actionCustom")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionImport_CSV_file = QtWidgets.QAction(MainWindow)
        self.actionImport_CSV_file.setObjectName("actionImport_CSV_file")
        self.menuExport.addAction(self.actionPDF)
        self.menuExport.addAction(self.actionCustom)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuImport.addAction(self.actionImport_CSV_file)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuImport.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Bindings
        self.pB_clear.clicked.connect(self.clear)
        self.pB_calculate.clicked.connect(self.get_file)
        self.actionOpen.triggered.connect(self.get_file)



    def clear(self):
        self.write_to_box("")


    def get_file(self):
        self.filname = QFileDialog.getOpenFileName(filter= "csv (*.csv)")[0]
        self.write_to_box("Hey")

    def write_to_box(self, msg):
        _translate = QtCore.QCoreApplication.translate
        self.resultBox.setHtml(_translate("MainWindow", f"{msg}"))


  #  def update(self, value):

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.step_var_layout.setText(_translate("MainWindow", "Step Var"))
        self.Response_var_layout.setText(_translate("MainWindow", "Response"))
        self.StepVarBox.setItemText(0, _translate("MainWindow", "Looooong Naaaaaaaaaaaaaaaaaaaaaaaaaaaaame"))
        self.StepVarBox.setItemText(1, _translate("MainWindow", "Short name"))
        self.checkBox_enable_sliders.setText(_translate("MainWindow", "Enable sliders"))
        self.label.setText(_translate("MainWindow", "ϴ"))
        self.label_2.setText(_translate("MainWindow", "Max"))
        self.pB_calculate.setText(_translate("MainWindow", "Calculate"))
        self.pB_reset.setText(_translate("MainWindow", "Reset"))

        # Text in result box
        self.resultBox.setHtml(_translate("MainWindow", "Test"))

        self.pB_save.setText(_translate("MainWindow", "Save"))
        self.pB_clear.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionPDF.setText(_translate("MainWindow", "PDF"))
        self.actionCustom.setText(_translate("MainWindow", "Custom"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionImport_CSV_file.setText(_translate("MainWindow", "Import CSV file"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

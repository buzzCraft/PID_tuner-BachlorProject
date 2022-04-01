# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './PID_tuner/GUI/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 694)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(5, 11, 673, 646))
        self.widget.setObjectName("widget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.wi_plot = QtWidgets.QWidget(self.widget)
        self.wi_plot.setMinimumSize(QtCore.QSize(600, 0))
        self.wi_plot.setObjectName("wi_plot")
        self.horizontalLayout_10.addWidget(self.wi_plot)
        spacerItem = QtWidgets.QSpacerItem(20, 358, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_10.addItem(spacerItem)
        self.MaxValueSlider = QtWidgets.QSlider(self.widget)
        self.MaxValueSlider.setMaximum(100)
        self.MaxValueSlider.setSliderPosition(95)
        self.MaxValueSlider.setOrientation(QtCore.Qt.Vertical)
        self.MaxValueSlider.setObjectName("MaxValueSlider")
        self.horizontalLayout_10.addWidget(self.MaxValueSlider)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.ResponseValueSlider = QtWidgets.QSlider(self.widget)
        self.ResponseValueSlider.setMaximum(8000)
        self.ResponseValueSlider.setSliderPosition(10)
        self.ResponseValueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ResponseValueSlider.setObjectName("ResponseValueSlider")
        self.horizontalLayout_4.addWidget(self.ResponseValueSlider)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
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
        self.StepVarBox.setMinimumSize(QtCore.QSize(100, 0))
        self.StepVarBox.setObjectName("StepVarBox")
        self.verticalLayout.addWidget(self.StepVarBox)
        self.ResponseVarBox = QtWidgets.QComboBox(self.widget)
        self.ResponseVarBox.setMinimumSize(QtCore.QSize(100, 0))
        self.ResponseVarBox.setObjectName("ResponseVarBox")
        self.verticalLayout.addWidget(self.ResponseVarBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_11.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sB_from = QtWidgets.QSpinBox(self.widget)
        self.sB_from.setMinimumSize(QtCore.QSize(37, 0))
        self.sB_from.setMaximumSize(QtCore.QSize(37, 16777215))
        self.sB_from.setObjectName("sB_from")
        self.horizontalLayout_7.addWidget(self.sB_from)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sB_to = QtWidgets.QSpinBox(self.widget)
        self.sB_to.setMinimumSize(QtCore.QSize(37, 0))
        self.sB_to.setMaximumSize(QtCore.QSize(37, 16777215))
        self.sB_to.setObjectName("sB_to")
        self.horizontalLayout_8.addWidget(self.sB_to)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.Sb_sampling_time = QtWidgets.QDoubleSpinBox(self.widget)
        self.Sb_sampling_time.setObjectName("Sb_sampling_time")
        self.horizontalLayout_9.addWidget(self.Sb_sampling_time)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_9)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.verticalLayout_8.addLayout(self.verticalLayout_4)
        self.checkBox_enable_sliders = QtWidgets.QCheckBox(self.widget)
        self.checkBox_enable_sliders.setObjectName("checkBox_enable_sliders")
        self.verticalLayout_8.addWidget(self.checkBox_enable_sliders)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sB_theta = QtWidgets.QSpinBox(self.widget)
        self.sB_theta.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sB_theta.setMaximum(100000)
        self.sB_theta.setObjectName("sB_theta")
        self.horizontalLayout_6.addWidget(self.sB_theta)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sB_max = QtWidgets.QDoubleSpinBox(self.widget)
        self.sB_max.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sB_max.setSingleStep(0.01)
        self.sB_max.setObjectName("sB_max")
        self.horizontalLayout_5.addWidget(self.sB_max)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_8.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pB_calculate = QtWidgets.QPushButton(self.widget)
        self.pB_calculate.setObjectName("pB_calculate")
        self.horizontalLayout_2.addWidget(self.pB_calculate)
        self.pB_reset = QtWidgets.QPushButton(self.widget)
        self.pB_reset.setObjectName("pB_reset")
        self.horizontalLayout_2.addWidget(self.pB_reset)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem5)
        self.horizontalLayout_13.addLayout(self.verticalLayout_8)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem6)
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
        spacerItem7 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.pB_clear = QtWidgets.QPushButton(self.widget)
        self.pB_clear.setObjectName("pB_clear")
        self.horizontalLayout_3.addWidget(self.pB_clear)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_13.addLayout(self.verticalLayout_5)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.verticalLayout_6.addLayout(self.horizontalLayout_13)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.step_var_layout.setText(_translate("MainWindow", "Step Var"))
        self.Response_var_layout.setText(_translate("MainWindow", "Response"))
        self.label_3.setText(_translate("MainWindow", "Step From"))
        self.label_4.setText(_translate("MainWindow", "Step To"))
        self.label_5.setText(_translate("MainWindow", "Sampling time"))
        self.checkBox_enable_sliders.setText(_translate("MainWindow", "Enable sliders"))
        self.label.setText(_translate("MainWindow", "ϴ"))
        self.label_2.setText(_translate("MainWindow", "Max"))
        self.pB_calculate.setText(_translate("MainWindow", "Calculate"))
        self.pB_reset.setText(_translate("MainWindow", "Reset"))
        self.resultBox.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
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
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
from matplotlib.figure import Figure
matplotlib.use('Qt5Agg')
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
import seaborn as sns
import pandas as pd
import sip
import pid_calc as pid

from PyQt5 import QtCore, QtGui, QtWidgets

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)


        super(MplCanvas, self).__init__(fig)





class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("PID - Tuning Helper")
        MainWindow.resize(716, 719)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.wi_plot = QtWidgets.QWidget(self.centralwidget)
        self.wi_plot.setMinimumSize(QtCore.QSize(600, 0))
        self.wi_plot.setObjectName("wi_plot")
        self.horizontalLayout_10.addWidget(self.wi_plot)
        spacerItem = QtWidgets.QSpacerItem(20, 358, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_10.addItem(spacerItem)
        self.MaxValueSlider = QtWidgets.QSlider(self.centralwidget)
        self.MaxValueSlider.setMaximum(100)
        self.MaxValueSlider.setSliderPosition(95)
        self.MaxValueSlider.setOrientation(QtCore.Qt.Vertical)
        self.MaxValueSlider.setObjectName("MaxValueSlider")
        self.horizontalLayout_10.addWidget(self.MaxValueSlider)
        self.verticalLayout_10.addLayout(self.horizontalLayout_10)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.ResponseValueSlider = QtWidgets.QSlider(self.centralwidget)
        self.ResponseValueSlider.setMaximum(8000)
        self.ResponseValueSlider.setSliderPosition(10)
        self.ResponseValueSlider.setOrientation(QtCore.Qt.Horizontal)
        self.ResponseValueSlider.setObjectName("ResponseValueSlider")
        self.horizontalLayout_4.addWidget(self.ResponseValueSlider)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_14.addItem(spacerItem3)
        self.verticalLayout_9.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.step_var_layout = QtWidgets.QLabel(self.centralwidget)
        self.step_var_layout.setObjectName("step_var_layout")
        self.verticalLayout_2.addWidget(self.step_var_layout)
        self.Response_var_layout = QtWidgets.QLabel(self.centralwidget)
        self.Response_var_layout.setObjectName("Response_var_layout")
        self.verticalLayout_2.addWidget(self.Response_var_layout)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.StepVarBox = QtWidgets.QComboBox(self.centralwidget)
        self.StepVarBox.setMinimumSize(QtCore.QSize(100, 0))
        self.StepVarBox.setObjectName("StepVarBox")
        self.verticalLayout.addWidget(self.StepVarBox)
        self.ResponseVarBox = QtWidgets.QComboBox(self.centralwidget)
        self.ResponseVarBox.setMinimumSize(QtCore.QSize(100, 0))
        self.ResponseVarBox.setObjectName("ResponseVarBox")
        self.verticalLayout.addWidget(self.ResponseVarBox)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout_11.addLayout(self.horizontalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.sB_from = QtWidgets.QSpinBox(self.centralwidget)
        self.sB_from.setMinimumSize(QtCore.QSize(37, 0))
        self.sB_from.setMaximumSize(QtCore.QSize(37, 16777215))
        self.sB_from.setObjectName("sB_from")
        self.horizontalLayout_7.addWidget(self.sB_from)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_7.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.sB_to = QtWidgets.QSpinBox(self.centralwidget)
        self.sB_to.setMinimumSize(QtCore.QSize(37, 0))
        self.sB_to.setMaximumSize(QtCore.QSize(37, 16777215))
        self.sB_to.setObjectName("sB_to")
        self.horizontalLayout_8.addWidget(self.sB_to)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_8.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_11.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.Sb_sampling_time = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.Sb_sampling_time.setObjectName("Sb_sampling_time")
        self.horizontalLayout_9.addWidget(self.Sb_sampling_time)
        self.horizontalLayout_12.addLayout(self.horizontalLayout_9)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.checkBox_enable_sliders = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_enable_sliders.setObjectName("checkBox_enable_sliders")
        self.verticalLayout_6.addWidget(self.checkBox_enable_sliders)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sB_theta = QtWidgets.QSpinBox(self.centralwidget)
        self.sB_theta.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sB_theta.setMaximum(100000)
        self.sB_theta.setObjectName("sB_theta")
        self.horizontalLayout_6.addWidget(self.sB_theta)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.verticalLayout_7.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.sB_max = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.sB_max.setMaximumSize(QtCore.QSize(75, 16777215))
        self.sB_max.setSingleStep(0.01)
        self.sB_max.setObjectName("sB_max")
        self.horizontalLayout_5.addWidget(self.sB_max)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6.addLayout(self.verticalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pB_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.pB_calculate.setObjectName("pB_calculate")
        self.horizontalLayout_2.addWidget(self.pB_calculate)
        self.pB_reset = QtWidgets.QPushButton(self.centralwidget)
        self.pB_reset.setObjectName("pB_reset")
        self.horizontalLayout_2.addWidget(self.pB_reset)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem6)
        self.horizontalLayout_13.addLayout(self.verticalLayout_6)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_13.addItem(spacerItem7)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem8)
        self.horizontalLayout_15.addLayout(self.horizontalLayout_13)
        spacerItem9 = QtWidgets.QSpacerItem(13, 240, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.resultBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.resultBox.setMaximumSize(QtCore.QSize(16777215, 250))
        self.resultBox.setObjectName("resultBox")
        self.verticalLayout_5.addWidget(self.resultBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pB_save = QtWidgets.QPushButton(self.centralwidget)
        self.pB_save.setObjectName("pB_save")
        self.horizontalLayout_3.addWidget(self.pB_save)
        spacerItem10 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.pB_clear = QtWidgets.QPushButton(self.centralwidget)
        self.pB_clear.setObjectName("pB_clear")
        self.horizontalLayout_3.addWidget(self.pB_clear)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8.addLayout(self.verticalLayout_5)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem11)
        self.horizontalLayout_15.addLayout(self.verticalLayout_8)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_15.addItem(spacerItem12)
        self.verticalLayout_9.addLayout(self.horizontalLayout_15)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.horizontalLayout_16.addLayout(self.verticalLayout_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 716, 21))
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
        self.pB_calculate.clicked.connect(self.calculating)
        #self.pB_calculate.clicked.connect(self.get_file)
        self.actionOpen.triggered.connect(self.get_file)

        # Trying to make plotting work
        # self.canvas = PlotCanvase(self)
        # self.toolbar = self.canvas
        # self.drawing_space.addItem(self.toolbar)
        # sc = PlotCanvas(self, width=5, height=4, dpi=100)
        # sc.axes.plot([0, 1, 2, 3, 4], [10, 1, 20, 3, 40])
        #
        # # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        # toolbar = Navi(sc, self)
        #
        # self.horizontalLayout_10.addItem(toolbar)
        # self.horizontalLayout_10.addItem(sc)
        #
        # wi = QtWidgets.QVBoxLayout()
        # wi.setLayout(self.horizontalLayout_10)
        # self.setCentralWidget(wi)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        # self.sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        self.toolbar = Navi(self.sc, MainWindow)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        # widget = QtWidgets.QWidget()
        # widget.setLayout(layout)
        self.wi_plot.setLayout(self.layout)
        # MainWindow.setCentralWidget(widget)

       # self.show()







    def get_file(self):
        self.filname = QFileDialog.getOpenFileName(filter= "csv (*.csv)")[0]
        if self.filname:
            self.step = pid.read(self.filname)
            self.update_combo_box(self.step.columns)
            self.suggest_values()

            #print()
            #self.write_to_box(self.step.head())

    def suggest_values(self):
        # Set min and max values to spin box when step var is chosen
        self.write_to_box(self.step[str(self.StepVarBox.currentText())].max())
        self.sB_from.setValue(int(self.step[str(self.StepVarBox.currentText())].min()))
        self.sB_to.setValue(int(self.step[str(self.StepVarBox.currentText())].max()))
        time = self.step.index.to_series().diff().value_counts()
        self.Sb_sampling_time.setValue(abs(time.index[0].total_seconds()))




    def write_to_box(self, msg, cls = False):
        # TODO Fikse dette, det er hacky
        _translate = QtCore.QCoreApplication.translate
        self.resultBox.setHtml(_translate("MainWindow", f"{msg}"))

    def update_combo_box(self, values):
        self.StepVarBox.clear()
        self.ResponseVarBox.clear()
        self.ResponseVarBox.addItems(values)
        self.StepVarBox.addItems(values)

    def calculating(self):
        # Getting values
        # TODO Check if values are set
        step_var = str(self.StepVarBox.currentText())
        response_var = str(self.ResponseVarBox.currentText())
        step_from = int(self.sB_from.value())
        step_to = int(self.sB_to.value())
        step_done = [step_from,step_to]
        samp = int(self.Sb_sampling_time.value())
        print(step_var, response_var)

        # Calculating
        t = pid.find_step(self.step, step_done, name = step_var)
        self.step_resp = pid.step_analytics(t, samp,step_done,0.1)
        self.step_resp.measured_value=response_var
        self.step_resp.gain=step_var
        self.step_resp.calculate(band=True)
        try:
            self.sc.axes.plot(self.step_resp.plot_detailed(False))
        except Exception as e: print(f'error {e}')

        # Result
        self.plot_calc()
        self.ResponseValueSlider.setValue(int(self.step_resp.theta))
        self.MaxValueSlider.setValue(int(self.step_resp.max_val))
        self.sB_theta.setValue(int(self.step_resp.theta))
        self.sB_max.setValue(self.step_resp.max_val)

        self.write_to_box(f'Kp = {self.step_resp.k_c} Ti = {self.step_resp.t_i}', cls = True)





  #  def update(self, value):

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
        self.resultBox.setHtml(_translate("MainWindow",
                                          "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
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

    def plot_calc(self):
        # Clear old plot
        self.clear_plot()
        self.sc.axes.grid(color = 'oldlace')

        self.sc.axes.plot(self.step_resp.step_df[self.step_resp.measured_value], color="r")

        # TODO Add second axies for step?
        # self.sc.axes.plot(self.step_resp.step_df[self.step_resp.gain], color="y")

        # Polotting point for when we choose step response
        # # Plotting vertical and hrisontal lines for 63% point
        self.sc.axes.hlines(self.step_resp.prosent63[1], xmin=0,
                            xmax=(-self.step_resp.prosent63[0]-1) * self.step_resp._sampling_time, color="grey",
                            linestyles='dashed')
        self.sc.axes.vlines((-self.step_resp.prosent63[0]-1) * self.step_resp._sampling_time,
                            ymin=self.step_resp.start[1] * 0.99, ymax=self.step_resp.prosent63[1],
                            color="grey",
                            linestyles='dashed')
        self.sc.axes.vlines(((-self.step_resp.response-1) * self.step_resp._sampling_time),
                            ymin=self.step_resp.start[1] * 0.99,
                            ymax=self.step_resp.step_df.iloc[self.step_resp.response][self.step_resp.measured_value],
                            color="grey", linestyles='dashed')
        self.sc.axes.vlines((self.step_resp.step_df.iloc[self.step_resp.start[0]]["Time"]),
                            ymin=self.step_resp.start[1] * 0.99,
                            ymax=self.step_resp.step_df.iloc[self.step_resp.response][self.step_resp.measured_value],
                            color="grey", linestyles='dashed')


        self.sc.axes.axhline(y=self.step_resp.max_val, color='blue', linestyle='-')
        self.sc.axes.axhline(y=self.step_resp.dY * 0.95 + self.step_resp.start[1], color='y', linestyle='-')
        self.sc.axes.text(-self.step_resp.response * self.step_resp._sampling_time * 1.2, self.step_resp.max_val,
                          f'Max val = {self.step_resp.max_val} ', fontsize=6, va="top")
        self.sc.axes.text(-self.step_resp.response * self.step_resp._sampling_time * 1.2,
                          self.step_resp.dY * 0.95 + self.step_resp.start[1],
                          f'95% = {self.step_resp.dY * 0.95 + self.step_resp.start[1]} ', fontsize=6, va="top")
        self.sc.axes.text(-self.step_resp.response * self.step_resp._sampling_time * 1.2,
                          self.step_resp.step_df.iloc[self.step_resp.response][self.step_resp.measured_value],
                          f'{self.step_resp.step_df.iloc[self.step_resp.response][self.step_resp.measured_value]} ',
                          fontsize=6, va="center")
        self.sc.axes.text((-self.step_resp.response * self.step_resp._sampling_time) + 5, self.step_resp.start[1],
                          f'ϴ: {self.step_resp.theta} ', fontsize=6, va="top", ha='right')
        self.sc.axes.text(((-self.step_resp.prosent63[0]) * self.step_resp._sampling_time) + 5, self.step_resp.start[1],
                          f'τ: {self.step_resp.tau}', fontsize=6, va="bottom", ha='right')
        self.sc.axes.text(((-self.step_resp.prosent63[0]) * self.step_resp._sampling_time) - 5,
                          self.step_resp.prosent63[1], f'63% value\n{self.step_resp.prosent63[1]}', fontsize=6,
                          va="top")
        # Plot cho0sen max point
        # Plot cho0sen max point
        self.sc.axes.plot()
        # Plotting points for local max/min
        #self.sc.axes.scatter(self.step_resp.step_df.index, self.step_resp.step_df["peak"], c='g')
        self.sc.draw()





    def clear(self, te=True):
        self.clear_plot()
        self.write_to_box("")

    def clear_plot(self):
        self.sc.axes.cla()
        self.sc.draw()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

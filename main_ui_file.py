# -*- coding: utf-8 -*-
# License information
# PyQt GPL - https://www.gnu.org/licenses/gpl-3.0.en.html
# Matplotlib, Numpy, Pandas BSD - https://opensource.org/licenses/BSD-3-Clause
# Python PSF - https://docs.python.org/3/license.html
# GPL will override BSD licenses
# For commercial use obtain a commercial license at https://riverbankcomputing.com/commercial/buy
# NOTE: No need for commercial license for internal use or if
# the sourcecode is made public.


import matplotlib
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QFileDialog
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as Navi
import gui_calc as pid
from PyQt5 import QtCore, QtWidgets, uic

matplotlib.use('Qt5Agg')

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig.set_tight_layout('pad')
        self.axes = self.fig.add_subplot(111)

        super(MplCanvas, self).__init__(self.fig)

    def save(self):
        self.fig.savefig('line_plot.png')

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('GUI/main3.ui', self)

        self.show()

        # Bindings
        self.pB_clear.clicked.connect(self.clear)
        self.actionClose.triggered.connect(self.clear)
        self.pB_calculate.clicked.connect(self.calculating)
        self.pB_reset.clicked.connect(self.reset_onclick)
        # self.pB_calculate.clicked.connect(self.get_file)
        self.actionImport_CSV_file.triggered.connect(self.get_file)
        self.actionExit.triggered.connect(MainWindow.close)
        self.MaxValueSlider.valueChanged.connect(self.change_sb_max)
        self.ResponseValueSlider.valueChanged.connect(self.change_sb_resp)
        self.sB_max.valueChanged.connect(self.change_slider_max)
        self.sB_theta.valueChanged.connect(self.change_slider_resp)
        self.pB_save.clicked.connect(self.save)






        self.sc = MplCanvas(self, width=5, height=4, dpi=100)


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
        self.k = False
        self.ti = False
        self.first = True

    def save(self):
        self.sc.save()

    def reset_onclick(self):
        self.reset_values()
        self.step = pid.read(self.filname)

    # Max value
    def change_sb_max(self):
        self.sB_max.setValue((self.MaxValueSlider.value()/100))
        self.calculating()
    def change_slider_max(self):
        self.MaxValueSlider.setValue(int(self.sB_max.value()*100))


    # Theta
    def change_sb_resp(self):
        self.sB_theta.setValue(self.ResponseValueSlider.value())

    def change_slider_resp(self):
        self.ResponseValueSlider.setValue(self.sB_theta.value())
        self.calculating()




    def get_file(self):
        # If loading a second CSV clear the last one
        if self.k:
            self.reset_values()
            self.clear()
        self.filname = QFileDialog.getOpenFileName(filter="csv (*.csv)")[0]
        if self.filname:
            self.step = pid.read(self.filname)
            self.update_combo_box(self.step.columns)
            self.suggest_values()
            self.plot_file()


            # print()
            # self.write_to_box(self.step.head())

    def suggest_values(self):
        # Set min and max values to spin box when step var is chosen
        self.write_to_box(self.step[str(self.StepVarBox.currentText())].max())
        self.sB_from.setValue(int(self.step[str(self.StepVarBox.currentText())].min()))
        self.sB_to.setValue(int(self.step[str(self.StepVarBox.currentText())].max()))
        time = self.step.index.to_series().diff().value_counts()
        self.Sb_sampling_time.setValue(abs(time.index[0].total_seconds()))

    def write_to_box(self, msg, cls=False):
        # TODO Fikse dette, det er hacky
        #_translate = QtCore.QCoreApplication.translate
        self.resultBox.clear()
        self.resultBox.insertPlainText(str(msg))
       # self.resultBox.setHtml(_translate("MainWindow", f"{msg}"))

    def update_combo_box(self, values):
        self.StepVarBox.clear()
        self.ResponseVarBox.clear()
        self.ResponseVarBox.addItems(values)
        self.StepVarBox.addItems(values)

    def calculating(self):

        # Getting values
        # TODO Check if values are set
        try:
            step_var = str(self.StepVarBox.currentText())
            response_var = str(self.ResponseVarBox.currentText())
            step_from = int(self.sB_from.value())
            step_to = int(self.sB_to.value())
            step_done = [step_from, step_to]
            samp = int(self.Sb_sampling_time.value())
        except Exception as e:
            print(f'error {e}')


        # Calculating
        # First run
        try:
            if not self.k:
                curr_step = pid.find_step(df = self.step, step = step_done, name=step_var)
                self.step_resp = pid.step_analytics(df = curr_step, sampling_time = samp, step_from_to = step_done, factor = 0.1)
                self.step_resp.measured_value = response_var
                self.step_resp.gain = step_var

                self.step_resp.calculate(band=False)

                self.MaxValueSlider.setMaximum(int(self.step_resp.max_val * 1.1*100))
                self.MaxValueSlider.setMinimum(int(self.step_resp.max_val * 0.9*100))
                # self.MaxValueSlider.setSliderPosition(int(self.step_resp.max_val))
            # Recalc with current values
            else:
                max_val = self.sB_max.value()
                theta = self.sB_theta.value()
                self.step_resp.re_calculate(max_val, theta)
        except Exception as e:
            print(f'error {e}')

        try:
            #self.sc.axes.plot(self.step_resp.plot_detailed(False))
            # Result
            self.plot_calc()
            # self.ResponseValueSlider.setValue(int(self.step_resp.theta))
            # self.MaxValueSlider.setValue(int(self.step_resp.max_val))
            self.sB_theta.setValue(int(self.step_resp.theta))
            self.sB_max.setValue(self.step_resp.max_val)
            self.k = self.step_resp.k_c
            self.sb_kp.setValue(self.step_resp.k_c)
            self.sb_ti.setValue(self.step_resp.t_i)

            self.write_to_box(self.step_resp)
        except Exception as e:
            print(f'error {e}')



    def plot_calc(self):
        # Clear old plot
        self.clear_plot()
        self.sc.axes.grid(color='oldlace')

        # df.loc[df['column_name'] == some_value]
        x = self.step_resp.step_df.loc[self.step_resp.step_df[self.step_resp.measured_value]==self.step_resp.max_val]

        self.sc.axes.plot(self.step_resp.step_df[self.step_resp.measured_value], color="r")

        # TODO Add second axies for step?
        # self.sc.axes.plot(self.step_resp.step_df[self.step_resp.gain], color="y")

        # Polotting point for when we choose step response
        # # Plotting vertical and horisontal lines for 63% point
        self.sc.axes.hlines(self.step_resp.prosent63[1], xmin=0,
                            xmax=(-self.step_resp.prosent63[0] - 1) * self.step_resp._sampling_time, color="grey",
                            linestyles='dashed')
        self.sc.axes.vlines((-self.step_resp.prosent63[0] - 1) * self.step_resp._sampling_time,
                            ymin=self.step_resp.start[1] * 0.99, ymax=self.step_resp.prosent63[1],
                            color="grey",
                            linestyles='dashed')
        # THETA
        self.sc.axes.vlines(((-self.step_resp.response - 1) * self.step_resp._sampling_time),
                            ymin=self.step_resp.start[1] * 0.99,
                            ymax=self.step_resp.step_df.iloc[self.step_resp.response][self.step_resp.measured_value],
                            color="grey", linestyles='dashed')
        self.sc.axes.vlines((self.step_resp.step_df.iloc[self.step_resp.start[0]]["Time"]),
                            ymin=self.step_resp.start[1] * 0.99,
                            ymax=self.step_resp.start[1] * 1.1,
                            color="blue", linestyles='dashdot')

        self.sc.axes.axhline(y=self.step_resp.max_val, color='blue', linestyle='-')
        # self.sc.axes.axhline(y=self.step_resp.dY * 0.95 + self.step_resp.start[1], color='y', linestyle='-')
        self.sc.axes.text(-self.step_resp.start[1] * self.step_resp._sampling_time * 1.5, self.step_resp.max_val,
                          f'Max val = {self.step_resp.max_val:.2f} ', fontsize=6, va="top")
        # self.sc.axes.text(-self.step_resp.start[1] * self.step_resp._sampling_time * 1.5,
        #                   self.step_resp.dY * 0.95 + self.step_resp.start[1],
        #                   f'95% = {self.step_resp.dY * 0.95 + self.step_resp.start[1]:.2f} ', fontsize=6, va="top")
        # Value at Theta
        self.sc.axes.text(-self.step_resp.response * self.step_resp._sampling_time * 1.2,
                          self.step_resp.step_df.iloc[self.step_resp.response][self.step_resp.measured_value],
                          f' {self.step_resp.step_df.iloc[self.step_resp.response][self.step_resp.measured_value]:.2f} ',
                          fontsize=6, va="center")
        self.sc.axes.text((-self.step_resp.response * self.step_resp._sampling_time) + 5, self.step_resp.start[1],
                          f'ϴ: {self.step_resp.theta:.0f} ', fontsize=6, va="top", ha='right')
        self.sc.axes.text(((-self.step_resp.prosent63[0]) * self.step_resp._sampling_time) + 5, self.step_resp.start[1],
                          f'τ: {self.step_resp.tau:.0f}', fontsize=6, va="bottom", ha='right')
        self.sc.axes.text(((-self.step_resp.prosent63[0]) * self.step_resp._sampling_time) - 5,
                          self.step_resp.prosent63[1], f'63% value\n{self.step_resp.prosent63[1]:.2f}', fontsize=6,
                          va="top")

        self.sc.axes.plot()

        # self.sc.axes.scatter(self.step_resp.step_df.index, self.step_resp.step_df["peak"], c='g')
        self.sc.draw()

    def plot_file(self):
        # Clear old plot
        self.clear_plot()
        self.sc.axes.grid(color='oldlace')
        self.sc.axes.plot(self.step)
        self.sc.draw()


    def clear(self):
        self.sB_from.clear()
        self.sB_to.clear()
        self.Sb_sampling_time.clear()
        self.clear_plot()
        self.StepVarBox.clear()
        self.ResponseVarBox.clear()
        self.MaxValueSlider.setMaximum(100)
        self.MaxValueSlider.setMinimum(0)


        self.sB_theta.clear()
        self.sB_max.clear()
        self.k = False
        self.ti = False
        self.filname = ""
        self.write_to_box("")

    def reset_values(self):
        self.clear_plot()
        # self.ResponseValueSlider.setValue(0)
        self.MaxValueSlider.setMaximum(100)
        self.MaxValueSlider.setMinimum(0)
        # self.MaxValueSlider.setValue(0)
        self.sB_theta.clear()
        self.sB_max.clear()
        self.k = False
        self.ti = False
        self.step = ""

    def clear_plot(self):
        self.sc.axes.cla()
        self.sc.draw()

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui()
    sys.exit(app.exec_())
import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


### Les inn fil
def read(file):
    df = pd.read_csv(file, delimiter=",", decimal=",")
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%d/%m/%Y %H:%M:%S")
    df.set_index(['Timestamp'], inplace=True)
    return df


### Rename fil
def rename(df, name):
    navn = list(name)
    for i in range(len(df.columns)):
        df.rename(columns={df.columns[i]: navn[i]}, inplace=True)
    return df


# Copy a step to a new dataFrame
def find_step(df, step, name = "SB401"):
    start_step = step[0]
    end_step = step[1]

    for i in range(1, len(df)):

        if df.iloc[-i][name] == start_step:

            if df.iloc[-(i + 1)][name] == end_step:
                df = df.drop(df.tail(i - 5).index)

                break
    for i in range(6, len(df)):
        if df.iloc[-i][name] != end_step:
            df = df.tail(i - 1)
            break
    return df


# Plot steps side by side
def multiPlot(plot_list, rows=3):
    nr_of_plots = len(plot_list)
    columns = nr_of_plots % rows
    columns = max(1, columns)

    fig, axes = plt.subplots(columns, rows, figsize=(15, 5), sharey=True)
    fig.suptitle('Step responses')
    i = 0
    for df in plot_list:
        sns.lineplot(ax=axes[i], data=df)
        axes[i].set_title(f"Step{i + 1}")
        i += 1


class step_analytics:
    # TODO - Implement the 5% band in the top as a variabel
    # TODO - Check usage of factor
    # TODO - Check usage of band
    # TODO - Seperate automatic calculation of parameters form finding parameters
    # TODO - Make setters for "response start" and "max_value"
    #           The setters should recalculate everything

    def __init__(self, df, sampling_time, step_from_to, factor=0.1):
        self.step_df = df  # dataframe with one step
        self._step_from = step_from_to[0]  # Step from value
        self._step_to = step_from_to[1]  # Step to value
        self._factor = factor  # The factor for when we say a change in value represent the first responce
        self._sampling_time = sampling_time
        # SYSTEM VALUES
        self.theta = 0
        self.tau = 0
        self.k = 0
        self.k_m = 0
        self.k_c = 0
        self.t_i = 0
        self.positive_step = True
        self.gain = "Navnet på pådraget"  # Navn på pådrags organ
        self.measured_value = "Navn på målt verdi"  # Navn på måleverdien
        self.prosent63 = []
        self.band = False

    # Find and return the position in the DF where the step happens
    def find_step(self):
        """
        Find where the step is done in the pandas dataframe
        :return: index place of the step
        """
        i = 1

        while self.step_df.iloc[-i][self.gain] == self._step_from:
            i += 1
        return -i + 1

    # Change the index of the DF to be == with sampling time
    # since you can argue that timestamps isnt to important for the test
    def change_index(self):
        """"
        Set df[-1] (the end of dataframe) = 0
        Each row is calculated row_nr*sampling_time
        :returns True on success:
        """
        try:
            self.step_df["Time"] = (np.arange(len(self.step_df)) * self._sampling_time)[::-1]
            ret = True
        except:
            print("Error in changing index")
            ret = False
        return ret
        # [::-1] -> Start the df at max time and decrease (Reversing the array)
        # This is done since the dataframe starts at the end

    def plot(self, show=False):
        """
        :param show: If true, show plot, false return plot:
        :return plt:
        """

        ax = sns.lineplot(data=self.step_df[self.measured_value], color="r")
        _ = ax.vlines(x=40, ymin=40, ymax=50, colors='g')

        ax2 = plt.twinx()
        sns.lineplot(data=self.step_df[self.gain], color="c")
        if show:
            plt.show()
        else:
            return plt

    def plot_detailed(self, show=False):
        """

        :param show: If true, show plot, false return plot:
        :return plt:
        """


        # Plotting the step
        ax = sns.lineplot(data=self.step_df[self.measured_value], color="r")
        # Polotting point for when we choose step response
        _ = ax.plot(-self.response * self._sampling_time, self.step_df.iloc[self.response][self.measured_value], marker="x", color="b")
        # Plotting vertical and hrisontal lines for 63% point
        _ = ax.hlines(self.prosent63[1], xmin=0, xmax=(-self.prosent63[0]) * self._sampling_time, color="grey",
                      linestyles='dashed')
        _ = ax.vlines((-self.prosent63[0]) * self._sampling_time, ymin=self.start[1] * 0.99, ymax=self.prosent63[1],
                      color="grey",
                      linestyles='dashed')
        _ = ax.vlines((-self.response * self._sampling_time), ymin=self.start[1] * 0.99, ymax=self.step_df.iloc[self.response][self.measured_value],
                      color="grey",linestyles='dashed')
        _ = ax.vlines((self.step_df.iloc[self.start[0]]["Time"]), ymin=self.start[1] * 0.99,
                      ymax=self.step_df.iloc[self.response][self.measured_value],
                      color="grey", linestyles='dashed')

        # Text test
       # text(x, y, s, fontdict=None, **kwargs)
        _ = ax.axhline(y=self.max_val, color='r', linestyle='-')
        _ = ax.axhline(y=self.dY*0.95+self.start[1], color='y', linestyle='-')
        _ = ax.text(-self.response * self._sampling_time * 1.2, self.max_val,
                    f'Max val = {self.max_val} ', fontsize=6, va="top")
        _ = ax.text(-self.response * self._sampling_time * 1.2, self.dY*0.95+self.start[1],
                    f'95% = {self.dY*0.95+self.start[1]} ', fontsize=6, va="top")
        _ = ax.text(-self.response * self._sampling_time*1.2, self.step_df.iloc[self.response][self.measured_value], f'{self.step_df.iloc[self.response][self.measured_value]} ', fontsize=6, va = "center")
        _ = ax.text((-self.response * self._sampling_time)+5, self.start[1], f'ϴ: {self.theta} ', fontsize=6, va = "top", ha = 'right')
        _ = ax.text(((-self.prosent63[0]) * self._sampling_time)+5, self.start[1], f'τ: {self.tau}', fontsize=6, va="bottom", ha = 'right')
        _ = ax.text(((-self.prosent63[0]) * self._sampling_time)-5, self.prosent63[1], f'63% value\n{self.prosent63[1]}', fontsize=6, va="top")
        # Plot cho0sen max point
        _ = ax.plot()
        # Plotting points for local max/min




        # New ax for the step variabel
        ax2 = plt.twinx()
        # Plotting the step
        sns.lineplot(data=self.step_df[self.gain], color="c")
        if show:
            plt.show()
        else:
            return ax

    def calculate(self, band=False):
        """
        Run calculations
        band : If set true, max value will be calculated out from 5% of observed max
        :returns: string on sucsess, false on error
        """
        self.use_band = band
        # try:
        self.find_parameters()
        return self.__str__()

    def re_calculate(self, max, theta):
        try:
            self.theta = theta
            self.max_val = max
            self.find_delta()
            self.find_63(0)
            self.find_tau()
            # Find tau value
            self.find_response_for_plot()
            self.k_m = self.k / self.tau

            # 4 x tau  -> 98% of response
            tc = self.theta

            # # firstOrder
            self.k_c = (1 / self.k) * self.tau / (tc + self.theta)
            self.t_i = min(self.tau, 4 * (tc + self.theta))
            return self.__str__()
        except:
            return "error"

    #

    def find_gradient(self):
        # Er inne på noe, men trenger også kanskje possisjonen
        df = pandas.DataFrame()
        df["gradient"] = self.step_df[self.measured_value] / self.step_df.shift[-1][self.measured_value]
        return max(df["gradient"])

    def find_local_peak(self):
        """
        Find all local maximum / minimum
        :return:
        """
        # Trying to find local min/max

        if self.positive_step:
            # For each row, compair it with the next and previous, if both are true, we have an local max
            self.step_df['peak'] = self.step_df[self.measured_value][
                (self.step_df[self.measured_value].shift(1) < self.step_df[self.measured_value]) & (
                            self.step_df[self.measured_value].shift(-1) < self.step_df[self.measured_value])]
        else:
            self.step_df['peak'] = self.step_df[self.measured_value][
                (self.step_df[self.measured_value].shift(1) > self.step_df[self.measured_value]) & (
                            self.step_df[self.measured_value].shift(-1) > self.step_df[self.measured_value])]

    def find_tau(self):
        """
        Calculate tau
        Time from response to 63%
        :return:
        """
        self.tau = self.step_df.iloc[self.prosent63[0]]['Time'] - self.theta - self.step_df.iloc[self.start[0]]["Time"]


    def find_theta(self):
        """
        Find theta
        From step start to response
        :return:
        """
        self.theta = self.step_df.iloc[self.response]["Time"] - self.step_df.iloc[self.start[0]]["Time"]


    def find_63(self, band = 0.05):
        """
        Find value and index for 63% of step
        :return:
        """
        self.prosent63 = []
        # Find 63% value and keep index and value
        if self.positive_step:
            dy2 = self.dY-self.dY*band

            #self.six = self.dY * 0.63 + self.start[1] - (self.dY*0.05)
            self.six = dy2 * 0.63 + self.start[1]


            # Loop the df
            for i in range(1, len(self.step_df)):
                # If the value for 63% is found
                if self.six <= self.step_df.iloc[-i][self.measured_value]:

                    if (abs(self.step_df.iloc[-i][self.measured_value] - self.six) > abs(
                            self.step_df.iloc[-i + 1][self.measured_value] - self.six)):
                        i = i + 1

                    # Add index to the list
                    self.prosent63.append(-i)
                    # Add value to the list
                    self.prosent63.append(self.step_df.iloc[-i][self.measured_value])

                    break

        else:
            dy2 = self.dY-self.dY*band
            self.six = dy2 * 0.63 + self.start[1]
            # Loop the df
            for i in range(1, len(self.step_df)):
                if self.six >= self.step_df.iloc[-i][self.measured_value]:
                    # Add index to the list
                    self.prosent63.append(-i)
                    # Add value to the list
                    self.prosent63.append(self.step_df.iloc[-i][self.measured_value])
                    break

    def find_max(self, use_factor=False, use_local_max=False):
        """
        Find the maxima value for the step
        :return:
        """
        # Add posibility to find it with a bond +/- 5% feks
        # Since SMIC say find max when t-> inf, we can use max/min functions since the step is issolated
        if use_factor:
            # TODO : Add a factor max way
            print("Need to add a factor thinghy here!")
            if self.positive_step:
                for i in range(len(self.step_df)):
                    if self.step_df.iloc[-i][self.measured_value] > self.step_df.iloc[-i - 1][self.measured_value]:
                        self.max_val = self.step_df.iloc[-i][self.measured_value] * (1 - self._factor)
            else:
                for i in range(len(self.step_df)):
                    if self.step_df.iloc[-i][self.measured_value] < self.step_df.iloc[-i - 1][self.measured_value]:
                        self.max_val = self.step_df.iloc[-i][self.measured_value]
        elif use_local_max:
            if self.positive_step:
                for i in range(len(self.step_df)):
                    if self.step_df.iloc[-i][self.measured_value] > self.step_df.iloc[-i - 1][self.measured_value]:
                        self.max_val = self.step_df.iloc[-i][self.measured_value]
            else:
                for i in range(len(self.step_df)):
                    if self.step_df.iloc[-i][self.measured_value] < self.step_df.iloc[-i - 1][self.measured_value]:
                        self.max_val = self.step_df.iloc[-i][self.measured_value]

        else:
            if self.positive_step:
                self.max_val = self.step_df[self.measured_value].max()
            else:
                self.max_val = self.step_df[self.measured_value].min()

    def find_delta(self):
        """
        Find:
        dY = max-start
        dU = step start value - step stop value
        k = dY / dU
        :return:
        """
        self.dY = abs((self.max_val - self.start[1]))
        # # dU = 60-40  # Use this if you got more then one stepresponse in the dataset
        self.dU = abs(self._step_to - self._step_from)
        #
        self.k = self.dY / self.dU

    def find_factor(self, calculate_factor=True):
        """
        Set the factor to 5% of dY
        :return:
        """
        if calculate_factor:
            self._factor = self.dY * 0.05

        else:
            pass

    def find_response(self):
        for i in range(-self.start[0], len(self.step_df)):
            if abs(self.start[1] - self.step_df.iloc[-i][self.measured_value]) >= self._factor:
                self.response = -i
                break

    def find_response_for_plot(self):
        self.response = -int(self.theta/self._sampling_time)


    def find_parameters(self):

        # Change index from timestamp to sampling time
        self.change_index()
        # Check type of step (from low to high = True, high to low = False)
        if self._step_to > self._step_from:
            self.positive_step = True
        else:
            self.positive_step = False

        # Find where the step happens
        step_start = self.find_step()
        # Add it to list start to be able to access it easy later on
        self.start = [step_start, self.step_df.iloc[step_start][self.measured_value]]


        # Find maxima value
        # Max for positive step
        # Min for negative step
        self.find_max(use_factor=False, use_local_max=False)

        # Find all local maxima
        # Max for positive step
        # Min for negative step
        self.find_local_peak()

        # Debug var


        # Find dY, dU and k
        self.find_delta() # Find dY/du

        self.find_factor(self.use_band) # Find the factor we would use as a % of dY/dU

        #self.find_max(use_factor=True,use_local_max=False)
        self.find_delta()

        # Find where we get the first sign of an response

        self.find_response()

        # Copy index to a column, to make it easier to do math on it
        self.step_df.index = self.step_df["Time"]

        self.find_theta()
        self.find_63()

        # All values aquired, and you know what that means...
        # MATH TIME

        # 63% = (dY * 0.63) + start_val
        # Theta = response time - start time
        # Tau = 63% time - response time


        # Find tau value
        self.find_tau()
        self.k_m = self.k / self.tau

        # 4 x tau  -> 98% of response
        tc = self.theta

        # # firstOrder
        self.k_c = (1 / self.k) * self.tau / (tc + self.theta)
        self.t_i = min(self.tau, 4 * (tc + self.theta))



    # Setters and getters for important vars
    # Doing it this way, we can automagicly re-calculate when vars are changed

    def __str__(self):
        return (
            f'{self._step_from} -> {self._step_to} \n Theta: {self.theta}\n Tau: {self.tau}\n K : {self.k}\n K* : {self.k_m}\n'
            f' Kc : {self.k_c}\n Ti : {self.t_i}'
            f'\nFor debug:\nMax = {self.max_val}\n63% sample point = {self.prosent63[0]} and value = {self.prosent63[1]}\n'
            f'Theta_h =  {self.theta} star_val= {self.start[1]}\n63% tid : {self.step_df.iloc[self.prosent63[0]]["Time"]} Response tid : {self.step_df.iloc[self.response]["Time"]}'
            f'\nStart verdi = {self.start[1]}  63% value = {self.prosent63[1]} Factor = {self._factor}'
            f'\nResponse value = {self.step_df.iloc[self.response][self.measured_value]} Response time = {-self.response * self._sampling_time}')

    @property
    def factor(self):
        return self._factor

    @factor.setter
    def factor(self, factor):
        self._factor = factor
        self.calculate()

    @property
    def sampling_time(self):
        return self._sampling_time

    @sampling_time.setter
    def sampling_time(self, sampling_time):
        self._sampling_time = sampling_time


if __name__ == "__main__":
    #df = read("https://raw.githubusercontent.com/buzzCraft/RobTek-prosjekt/main/StepRespons%2003032022_2.csv")
    #df = read("Step_A_220320222.csv")
    df = read("Step_B_30032022.csv")
    navn = {
        "SB401": "Ventilåpning til bygg E",
        "RT503": "Retur radiator",
    }
    df = rename(df, navn)
    #steps_done = [[50, 40], [40, 60], [60, 50]]
    steps_done = [[40,60]]
    single_step = []
    list_of_steps = []
    for step in steps_done:
        single_step.append(step_analytics(find_step(df, step), 10, step, 0.1))
    n = 0
    single_step[n].measured_value = "RT503"
    single_step[n].gain = "SB401"
    print(single_step[n].calculate(band=True))
    single_step[n].plot_detailed(True)


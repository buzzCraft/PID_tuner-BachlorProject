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
def find_step(df, step):
    start_step = step[0]
    end_step = step[1]

    for i in range(1, len(df)):

        if df.iloc[-i]["SB401"] == start_step:

            if df.iloc[-(i + 1)]["SB401"] == end_step:
                df2 = df.drop(df.tail(i - 5).index)

                break
    for i in range(6, len(df2)):
        if df2.iloc[-i]["SB401"] != end_step:
            df2 = df2.tail(i - 1)
            break
    return df2


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

    # Find and return the position in the DF where the step happens
    def find_step(self):
        i = 1

        while self.step_df.iloc[-i][self.gain] == self._step_from:
            print(i)
            i += 1
        return -i

    # Change the index of the DF to be == with sampling time
    # since you can argue that timestamps isnt to important for the test
    # TODO - Would maybe be smart to save test start timestamp for report?
    def change_index(self):
        self.step_df["Time"] = (np.arange(len(self.step_df)) * self._sampling_time)[::-1]

        # [::-1] -> Start the df at max time and decrease (Reversing the array)
        # This is done since the dataframe starts at the end

    def plot(self):
        print("Plotting")
        ax = sns.lineplot(data=self.step_df[self.measured_value], color="r")
        _ = ax.vlines(x = 40, ymin=40, ymax = 50, colors='g')


        ax2 = plt.twinx()
        sns.lineplot(data=self.step_df[self.gain], color="c")
        plt.show()
    def plot_detailed(self):
        print("Plotting")
        #Plotting the step
        ax = sns.lineplot(data=self.step_df[self.measured_value], color="r")
        # Polotting point for when we choose step response
        _ =ax.plot(self.theta,self.start[1], marker="x", color="b")
        # Plotting vertical and hrisontal lines for 63% point
        _ = ax.hlines(self.prosent63[1], xmin=0, xmax =(self.prosent63[1]-1)*self._sampling_time, color="grey", linestyles='dashed' )
        _ = ax.vlines((self.prosent63[1] - 1) * self._sampling_time, ymin=self.start[1]*0.99, ymax=self.prosent63[1], color="grey",
                      linestyles='dashed')
        # Plotting points for local max/min
        _ = ax.scatter(self.step_df.index, self.step_df["peak"], c='g')

        # New ax for the step variabel
        ax2 = plt.twinx()
        # Plotting the step
        sns.lineplot(data=self.step_df[self.gain], color="c")
        plt.show()


    def calculate(self):
        print("Starting with calculations")
        self.find_parameters()
        print("Done..")
        print(self.__str__())

    def find_gradient(self):
        # Er inne på noe, men trenger også kanskje possisjonen
        df = pandas.DataFrame()
        df["gradient"] = self.step_df[self.measured_value]/self.step_df.shift[-1][self.measured_value]
        return max(df["gradient"])

    def find_peak(self):
        # Trying to find local min/max

        if self.positive_step:
            # For each row, compair it with the next and previous, if both are true, we have an local max
            self.step_df['peak'] = self.step_df[self.measured_value][(self.step_df[self.measured_value].shift(1) < self.step_df[self.measured_value]) &(self.step_df[self.measured_value].shift(-1) < self.step_df[self.measured_value])]
        else:
            self.step_df['peak'] = self.step_df[self.measured_value][(self.step_df[self.measured_value].shift(1) > self.step_df[self.measured_value]) &(self.step_df[self.measured_value].shift(-1) > self.step_df[self.measured_value])]

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

        self.start = [step_start, self.step_df.iloc[step_start][self.measured_value]]

        # Find where we get the first sign of an response
        print(self.start[1])
        for i in range(1, len(self.step_df)):
            if abs(self.start[1] - self.step_df.iloc[-i][self.measured_value]) > self._factor:
                response = -i

                # TRENGS IKKE?
                # response.append(-i)
                # response.append(self.df.iloc[-i][self.result])
                break

        # Max value
        # Find max value
        # Add posibility to find it with a bond +/- 5% feks
        # Since SMIC say find max when t-> inf, we can use max/min functions since the step is issolated
        if self.positive_step:
            peak_val = self.step_df[self.measured_value].max()
            # rt503_peak = self.df.iloc[self.findMax(self.df, response)][self.measured_value]
        else:
            peak_val = self.step_df[self.measured_value].min()
        self.find_peak()
        # delta Y = (peak value - start value) absolute value

        self.dY = abs((peak_val - self.start[1]))
        # # dU = 60-40  # Use this if you got more then one stepresponse in the dataset
        self.dU = abs(self._step_to - self._step_from)
        #
        self.k = self.dY / self.dU
        #
        # # Calculate time - Theta
        # df2['index_col'] = df2.index
        # Copy index to a column, to make it easier to do math on it
        self.step_df.index = self.step_df["Time"]
        # time = (df2.iloc[response[0]]['index_col'] - df2.iloc[start[0]]['index_col'])
        self.theta = self.step_df.iloc[response]["Time"] - self.step_df.iloc[self.start[0]]["Time"]
        #
        #
        # # Calculate value for 63%

        #
        self.prosent63 = []

        # Find 63% value and keep index and value
        if self.positive_step:
            self.six = self.dY * 0.63 + self.start[1]

            for i in range(1, len(self.step_df)):
                if self.six <= self.step_df.iloc[-i][self.measured_value]:
                    self.prosent63.append(-i)
                    self.prosent63.append(self.step_df.iloc[-i][self.measured_value])
                    break

        else:
            self.six = -self.dY * 0.63 + self.start[1]

            for i in range(1, len(self.step_df)):
                if self.six >= self.step_df.iloc[-i][self.measured_value]:
                    self.prosent63.append(-i)
                    self.prosent63.append(self.step_df.iloc[-i][self.measured_value])
                    break

        # All values aquired, and you know what that means...
        # MATH TIME
        self.tau = self.step_df.iloc[self.prosent63[0]]['Time'] - self.step_df.iloc[response]['Time']
        self.k_m = self.k / self.tau
        # 4 x tau  -> 98% av respons
        tc = self.theta
        # # firstOrder
        self.k_c = (1 / self.k) * self.tau / (tc + self.theta)
        self.t_i = min(self.tau, 4 * (tc + self.theta))
        #
        # return [(str(step_start_value) + "-> " + str(step_stop_value)), theta, tau, k, k_m, k_c, t_i]

    # Setters and getters for important vars
    # Doing it this way, we can automagicly re-calculate when vars are changed

    def __str__(self):
        return (
            f'{self._step_from} -> {self._step_to} \n Theta: {self.theta}\n Tau: {self.tau}\n K : {self.k}\n K* : {self.k_m}\n'
            f' Kc : {self.k_c}\n Ti : {self.t_i}')

    @property
    def factor(self):
        return self._factor

    @factor.setter
    def factor(self, factor):
        self._factor = factor

    @property
    def sampling_time(self):
        return self._sampling_time

    @sampling_time.setter
    def sampling_time(self, sampling_time):
        self._sampling_time = sampling_time


if __name__ == "__main__":
    df = read("https://raw.githubusercontent.com/buzzCraft/RobTek-prosjekt/main/StepRespons%2003032022_2.csv")
    navn = {
        "SB401": "Ventilåpning til bygg E",
        "RT503": "Retur radiator",
    }
    df = rename(df, navn)
    steps_done = [[50, 40], [40, 60], [60, 50]]
    single_step = []
    list_of_steps = []
    for step in steps_done:
        single_step.append(step_analytics(find_step(df, step),60,step,0.3))
    single_step[1].measured_value = "RT503"
    single_step[1].gain = "SB401"
    single_step[1].calculate()
    single_step[1].plot_detailed()




#
# test = step("w", [40, 20], 0.3)
#
# print(test.factor)
# test.factor = 34
# print(test.factor)

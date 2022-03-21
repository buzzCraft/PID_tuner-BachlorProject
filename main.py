import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


#pnypszzxrixrmhuemk # nthrw # c0m
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


# Find peak after a positive step
def findMax(df, start):
    for i in range(abs(start), len(df)):
        if df.iloc[-i]["RT503"] > df.iloc[-i - 1]["RT503"]:
            return -i


# Find peak after a negative step
def findMin(df, start):
    for i in range(abs(start), len(df)):
        if df.iloc[-i]["RT503"] < df.iloc[-i - 1]["RT503"]:
            return -i


# Function to calculate skogstad from stepresponse
def skogestad(df2, step, df, factor=0.1):
    # Read in step values
    step_start_value = step[0]
    step_stop_value = step[1]
    # Check type of step (from low to high = True, high to low = False)

    if step_stop_value - step_start_value > 0:
        positive_step = True
    else:
        positive_step = False

    # Factor to decide when we get a response
    # if start - current > factor -> set response
    # factor = 0.1

    # Set = to row where the stepresponse was done (- to start from the back)
    step_start = -6

    start = [step_start, df2.iloc[step_start]["RT503"]]

    # Find where we get the first sign of an response
    for i in range(1, len(df)):
        if abs(start[1] - df2.iloc[-i]["RT503"]) > factor:
            response = []
            response.append(-i)
            response.append(df2.iloc[-i]["RT503"])
            break

    # Max value
    # As observed the temperature has a dip after the first top, use
    # the first way to find max to get the first top
    # use the second function to find the max value
    if positive_step:
        rt503_peak = df2.iloc[findMax(df2, response[0])]["RT503"]
    else:
        rt503_peak = df2.iloc[findMin(df2, response[0])]["RT503"]

    # delta Y = (peak value - start value) absolute value

    dY = abs((rt503_peak - start[1]))
    # dU = 60-40  # Use this if you got more then one stepresponse in the dataset
    dU = abs(step_start_value - step_stop_value)

    k = dY / dU

    # Calculate time - Theta
    df2['index_col'] = df2.index
    time = (df2.iloc[response[0]]['index_col'] - df2.iloc[start[0]]['index_col'])

    theta = time.total_seconds()

    # Calculate value for 63%
    if positive_step:
        six = dY * 0.63 + start[1]
    else:
        six = -dY * 0.63 + start[1]

    prosent63 = []

    # Find 63% value and keep index and value
    if positive_step:

        for i in range(1, len(df)):
            if six == df2.iloc[-i]["RT503"]:
                prosent63.append(-i)
                prosent63.append(df2.iloc[-i]["RT503"])
                break
            elif six < df2.iloc[-i]["RT503"]:
                prosent63.append(-i)
                prosent63.append(df2.iloc[-i]["RT503"])
                break
    else:

        for i in range(1, len(df)):
            if six == df2.iloc[-i]["RT503"]:
                prosent63.append(-i)
                prosent63.append(df2.iloc[-i]["RT503"])
                break
            elif six > df2.iloc[-i]["RT503"]:
                prosent63.append(-i)
                prosent63.append(df2.iloc[-i]["RT503"])
                break

    time = (df2.iloc[prosent63[0]]['index_col'] - df2.iloc[response[0]]['index_col'])
    tau = time.total_seconds()
    k_m = k / tau
    # 4 x tau  -> 98% av respons
    tc = theta
    # firstOrder
    k_c = (1 / k) * tau / (tc + theta)
    t_i = min(tau, 4 * (tc + theta))

    return [(str(step_start_value) + "-> " + str(step_stop_value)), theta, tau, k, k_m, k_c, t_i]




class step:
    def __init__(self, df, sampling_time, step_from_to, factor = 0.1):
        self.step_df = df #dataframe with one step
        self._step_from = step_from_to[0] # Step from value
        self._step_to = step_from_to[1] # Step to value
        self._factor = factor # The factor for when we say a change in value represent the first responce
        self._sampling_time = sampling_time
        # SYSTEM VALUES
        self.theta = 0
        self.tau = 0
        self.k=0
        self.k_m = 0
        self.k_c=0
        self.t_i=0
        self.positive_step = True
        self.gain = "Navnet på pådraget"   # Navn på pådrags organ
        self.measured_value = "Navn på målt verdi" # Navn på måleverdien

    # Find and return the position in the DF where the step happens
    def find_step(self):
        i = 1
        while self.df.iloc[-i][self.gain] == self._step_from:
            i += 1
        return i

    # Change the index of the DF to be == with sampling time
    # since you can argue that timestamps isnt to important for the test
    # TODO - Would maybe be smart to save test start timestamp for report?
    def change_index(self):
        self.step_df["Time"] = (np.arrange(len(self.df))*self._sampling_time)[::-1]
        # [::-1] -> Start the df at max time and decrease (Reversing the array)
        # This is done since the dataframe starts at the end

    def find_theta(self):

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

        start = [step_start, self.df.iloc[step_start][self.measured_value]]

        # Find where we get the first sign of an response
        for i in range(1, len(self.df)):
            if abs(start[1] - self.df.iloc[-i][self.measured_value]) > self._factor:
                response = -i

                #TRENGS IKKE?
                # response.append(-i)
                # response.append(self.df.iloc[-i][self.result])
                break

        # Max value
        # Find max value
        # Add posibility to find it with a bond +/- 5% feks
        # Since SMIC say find max when t-> inf, we can use max/min functions since the step is issolated
        if self.positive_step:
            peak_val = self.df[self.measured_value].max()
            # rt503_peak = self.df.iloc[self.findMax(self.df, response)][self.measured_value]
        else:
            peak_val = self.df[self.measured_value].min()

        # delta Y = (peak value - start value) absolute value

        self.dY = abs((peak_val - start[1]))
        # # dU = 60-40  # Use this if you got more then one stepresponse in the dataset
        self.dU = abs(self._step_to - self.step_from)
        #
        self.k = self.dY / self.dU
        #
        # # Calculate time - Theta
        # df2['index_col'] = df2.index
        # Copy index to a column, to make it easier to do math on it
        self.step_df["Time"] = self.step_df.index
        # time = (df2.iloc[response[0]]['index_col'] - df2.iloc[start[0]]['index_col'])
        self.theta = self.step_df.iloc[response]["Time"] - self.step_df.iloc[start[0]]["Time"]
        #
        #
        # # Calculate value for 63%


        #
        prosent63 = []

        # Find 63% value and keep index and value
        if self.positive_step:
            six = self.dY * 0.63 + start[1]

            for i in range(1, len(self.step_df)):
                if six <= self.step_df.iloc[-i][self.measured_value]:
                    prosent63.append(-i)
                    prosent63.append(self.step_df.iloc[-i][self.measured_value])
                    break
                elif six < self.step_df.iloc[-i][self.measured_value]:
                    prosent63.append(-i)
                    prosent63.append(self.step_df.iloc[-i][self.measured_value])
                    break
        else:
            six = -self.dY * 0.63 + start[1]

            for i in range(1, len(self.step_df)):
                if six >= self.step_df.iloc[-i][self.measured_value]:
                    prosent63.append(-i)
                    prosent63.append(self.step_df.iloc[-i][self.measured_value])
                    break

        # All values aquired, and you know what that means...
        # MATH TIME
        self.tau = self.step_df.iloc[prosent63[0]]['Time']-self.step_df.iloc[response[0]]['Time']
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
        return (f'{self._step_from} -> {self._step_to} \n Theta: {self.theta}\n Tau: {self.tau}\n K : {self.k}\n K* : {self.k_m}\n'
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




test = step("w",[40,20], 0.3)

print(test.factor)
test.factor = 34
print(test.factor)

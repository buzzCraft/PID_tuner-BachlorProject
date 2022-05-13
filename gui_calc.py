import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


### Les inn fil
def read(file):
    df = pd.read_csv(file, delimiter=",", decimal=",")
    try:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], format="%d/%m/%Y %H:%M:%S")
    except:
        pass
    df.set_index(['Timestamp'], inplace=True)
    return df


# Copy a step to a new dataFrame
def find_step(df, step, name="SB401"):
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


class step_analytics:

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
        self.gain = "Name of gain var"  # Navn på pådrags organ
        self.measured_value = "Name of response var"  # Navn på måleverdien
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
            self.use_band = False
            self.theta = theta
            self.max_val = max
            self.find_delta()
            self.prosent63 = self.find_precent(0.63)
            self.find_tau()
            # Find tau value
            self.find_response_for_plot()

            self.calc_skogestad()
            return self.__str__()
        except:
            return "error"

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

    # def find_63(self, band = 0.05):
    #     """
    #     Find value and index for 63% of step
    #     :return:
    #     """
    #     self.prosent63 = []
    #     # Find 63% value and keep index and value
    #
    #     dy2 = self.dY-self.dY*band
    #     self.six = dy2 * 0.63 + self.start[1]
    #     # Loop the df
    #     for i in range(1, len(self.step_df)):
    #         # If the value for 63% is found
    #         if self.six <= self.step_df.iloc[-i][self.measured_value]:
    #
    #             if (abs(self.step_df.iloc[-i][self.measured_value] - self.six) > abs(
    #                     self.step_df.iloc[-i + 1][self.measured_value] - self.six)):
    #                 i = i + 1
    #
    #             # Add index to the list
    #             self.prosent63.append(-i)
    #             # Add value to the list
    #             self.prosent63.append(self.step_df.iloc[-i][self.measured_value])

    # break
    def find_precent(self, prct=0.63, band=0.05):
        """
        Find value and index for 63% of step
        :return:
        """
        percent = []
        # Find prct value and keep index and value

        dy_band = self.dY - self.dY * band
        percent_value = dy_band * prct + self.start[1]
        # Loop the df
        for i in range(1, len(self.step_df)):
            # If the value for 63% is found
            if percent_value <= self.step_df.iloc[-i][self.measured_value]:

                if (abs(self.step_df.iloc[-i][self.measured_value] - percent_value) > abs(
                        self.step_df.iloc[-i + 1][self.measured_value] - percent_value)):
                    i = i + 1

                # Return index and value
                percent = [-i, (self.step_df.iloc[-i][self.measured_value])]

                return percent

    def find_max(self, use_factor=False):
        """
        Find the maxima value for the step
        :return:
        """
        # Add posibility to find it with a bond +/- 5% feks
        # Since SMIC say find max when t-> inf, we can use max/min functions since the step is issolated
        self.max_val = self.step_df[self.measured_value].max()
        self.max_val_id = self.step_df[self.measured_value].idxmax()

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
        self.response = -int((self.theta / self._sampling_time) - self.start[0])

    def find_parameters(self):

        # Change index from timestamp to sampling time
        self.change_index()
        step_start = self.find_step()
        # Add it to list start to be able to access it easy later on
        self.start = [step_start, self.step_df.iloc[step_start][self.measured_value]]
        # Find maxima value
        self.find_max(use_factor=False)
        # Find dY, dU and k
        self.find_delta()  # Find dY/du
        self.find_factor(self.use_band)  # Find the factor we would use as a % of dY/dU
        # Find where we get the first sign of an response
        self.find_response()
        # Copy index to a column, to make it easier to do math on it
        self.step_df.index = self.step_df["Time"]
        self.find_theta()
        # self.find_63()
        self.prosent63 = self.find_precent(0.63)
        # All values aquired, and you know what that means...
        # MATH TIME
        self.calc_skogestad()

    def calc_skogestad(self):
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
            f'Step from {self._step_from} to {self._step_to} \nTheta: {self.theta}\nTau: {self.tau}\nK : {self.k:.2}\nK* : {self.k_m:.2}\n'
            f'Kp : {self.k_c:.3}\n Ti : {self.t_i}'
            f'\nMax = {self.max_val}\n63% value = {self.prosent63[1]}\n'
            f'Start value= {self.start[1]}\n63% time : {self.step_df.iloc[self.prosent63[0]]["Time"]}'
            f'\nResponse value = {self.step_df.iloc[self.response][self.measured_value]} \nResponse time = {-(self.response - self.start[0]) * self._sampling_time}')

    def get_vars(self):
        var = {
            "from": self._step_from,
            "to": self._step_to,
            "theta": self.theta,
            "tau": self.tau,
            "kp": self.k_c,
            "ti": self.t_i,
            "k": self.k,
            "max": self.max_val,
            "63%val": self.prosent63[1],
            "gain" :self.gain,
            "resp":self.measured_value,
        }
        return var

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

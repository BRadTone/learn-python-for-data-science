import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from src.data_manipulation import main_df, avg_df
from matplotlib import cm

plt.rc('xtick', labelsize=7)
plt.rc('ytick', labelsize=7)

avg_cols = list(avg_df)
avg_cols_len = len(avg_cols)
avg_polution_cols = ['mean_pm1', 'mean_pm10', 'mean_pm25']


def yearly_polution_scattered():
    for idx, col in enumerate(avg_cols):
        plt.subplot(avg_cols_len, 1, idx + 1)
        plt.plot(avg_df.index, avg_df[col], 'b.', label=col)
        plt.grid(True)
        plt.legend()

    plt.show()


def yearly_pollution_histogram():
    # todo: change to figure
    for idx, col in enumerate(avg_cols):
        plt.subplot(avg_cols_len, 1, idx + 1)
        plt.hist(avg_df[col], label=col, alpha=.8)
        plt.grid(True)
        plt.legend()

    plt.show()


def yearly_temp_to_pollution():
    # todo: change to figure
    for idx, col in enumerate(avg_polution_cols):
        plt.subplot(len(avg_polution_cols), 1, idx + 1)
        plt.scatter(avg_df.mean_temperature, avg_df[col], s=.2, label=col)
        plt.grid(True)
        plt.legend()

    plt.show()


def temp_pollution_date():
    # todo: tutorial - https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html#d-plots-in-3d
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x = avg_df.mean_pressure
    y = avg_df.mean_temperature
    z = avg_df.mean_pm25
    c = avg_df.mean_pm25.tolist()

    ax.scatter(x, y, z, s=5, c=c)
    plt.show()

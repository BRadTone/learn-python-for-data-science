import pandas as pd
import src.data_manipulation as manipulate
import matplotlib.pyplot as plt

plt.rc('xtick', labelsize=7)
plt.rc('ytick', labelsize=7)


# TODO convert to jupyter notebook
# TODO change description in README, to all locations
# TODO https://jsfiddle.net/gqty1fq9/ - move it as inner part of project
# TODO gausian distribution, anomaly detection, median, variance, plot it

def plot():
    main_df = manipulate.get_krakow_air_df()
    avg_df = manipulate.get_mean_cols(main_df) \
        .resample('D') \
        .mean() \
        .round(1)

    cols = list(avg_df)
    cols_len = len(cols)
    for idx, col in enumerate(cols):
        plt.subplot(cols_len, 1, idx + 1)
        plt.plot(avg_df.index, avg_df[col], 'b.', label=col)
        plt.grid(True)
        plt.legend()

    plt.show()

    for idx, col in enumerate(cols):
        plt.subplot(cols_len, 1, idx + 1)
        plt.hist(avg_df[col], label=col, alpha=.8)
        plt.grid(True)
        plt.legend()

    plt.show()


if __name__ == '__main__':
    plot()

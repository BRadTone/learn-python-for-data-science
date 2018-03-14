import pandas as pd
import pickle
import glob
import os

pd.set_option('display.width', 8000)

debug = True


def get_sensor_locations():
    return False


def get_krakow_air_df():
    pickle_name = '../data/air_krakow.pickle'

    if os.path.isfile(pickle_name) and not debug:
        return pd.read_pickle(pickle_name)

    print('creating pickle...')

    df = get_all_csv_df()

    pickle_out = open(pickle_name, 'wb')
    pickle.dump(df, pickle_out)
    pickle_out.close()

    return df


def get_all_csv_df():
    path_ = r'../data/original_data'
    all_files = glob.glob(os.path.join(path_, "*.csv"))
    list_ = []

    for file in all_files:
        df = pd.read_csv(file, index_col=None, header=0)
        list_.append(df)

    df = pd.concat(list_)
    df.set_index('UTC time', inplace=True)
    df.sort_index()
    df.index = pd.to_datetime(df.index)
    # todo: move reseaple to plotting file
    df = df.resample('D').mean()
    return df



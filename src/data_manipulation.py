import pandas as pd
import pickle
import glob
import os

pd.set_option('display.width', 5000)


def get_sensor_locations():
    return False


def get_krakow_air_df():
    # todo: __init__.py https://stackoverflow.com/questions/448271/what-is-init-py-for
    pickle_name = 'data/air_krakow.pickle'

    debug_csv = False
    if os.path.isfile(pickle_name) and not debug_csv:
        return pd.read_pickle(pickle_name)

    print('creating pickle...')

    df = get_all_csv_df()

    pickle_out = open(pickle_name, 'wb')
    pickle.dump(df, pickle_out)
    pickle_out.close()

    return df


def get_all_csv_df():
    path_ = r'data/original_data'
    all_files = glob.glob(os.path.join(path_, "*.csv"))
    print(all_files)
    list_ = []

    for file in all_files:
        df = pd.read_csv(file, index_col=None, header=0)
        list_.append(df)

    df = pd.concat(list_)
    df.set_index('UTC time', inplace=True)
    df.sort_index(inplace=True)
    df.index = pd.to_datetime(df.index)

    return df


def average_over_sensors(base_df):
    column_types = ['humidity', 'pressure', 'temperature', 'pm1', 'pm10', 'pm25']
    _avg_df = pd.DataFrame(index=base_df.index)

    for type_ in column_types:
        type_all_cols = [col for col in list(base_df) if type_ in col]
        _avg_df['mean_' + type_] = base_df[type_all_cols].mean(axis=1)

    return _avg_df


main_df = get_krakow_air_df()
avg_df = average_over_sensors(main_df).resample('4H').mean().round(1)

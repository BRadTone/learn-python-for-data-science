import datetime
import pandas as pd
import pickle
import glob
import os
pd.set_option('display.width', 800)


def parse_date(date_int):
    return datetime.datetime.strptime(str(date_int), "%Y%m%d%H%M")


def get_seoul_air_df():
    pickle_name = 'SeulAirData.pickle'

    if os.path.isfile(pickle_name):
        return pd.read_pickle(pickle_name)

    print('creating pickle...')

    df = pd.read_csv('src/SeoulHourlyAvgAirPollution.air_polution')
    df.columns = ['date', 'Callee', 'nitrogen dioxide(ppm)', 'ozone(ppm)',
                  'Carbon monoxide(ppm)', 'Sulfur dioxide(ppm)', 'Fine dust (㎍/㎥)', 'Ultra fine dust']
    df = df.drop(['Callee', 'Ultra fine dust'], axis=1)
    df.date = df.date.apply(parse_date)
    df.set_index('date', inplace=True)

    pickle_out = open(pickle_name, 'wb')  # wb - write bytes
    pickle.dump(df, pickle_out)
    pickle_out.close()

    return df


# todo
def get_sensor_locations():
    return False


# todo: use all columns, handle extra commas in air_pollution files
# def get_all_csv_df():
#     path_ = r'../data/air_polution'
#     all_files = glob.glob(os.path.join(path_, "*.csv"))
#     list_ = []
#
#     for file in all_files:
#         df = pd.read_csv(file, index_col=None, header=0)
#         list_.append(df)
#
#     return pd.concat(list_)

# todo http://fredgibbs.net/tutorials/extract-transform-save-csv - remove commas from original_data

# df_ = get_all_csv_df()
#
# print(df_)
# print(df_.tail())
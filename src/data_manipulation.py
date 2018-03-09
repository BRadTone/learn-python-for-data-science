import os.path as path
import datetime
import pandas as pd
import pickle


def parse_date(date_int):
    return datetime.datetime.strptime(str(date_int), "%Y%m%d%H%M")


def get_df():
    pickle_name = 'SeulAirData.pickle'
    pd.set_option('display.width', 800)

    if path.isfile(pickle_name):
        return pd.read_pickle(pickle_name)

    print('creating pickle...')

    df = pd.read_csv('src/SeoulHourlyAvgAirPollution.csv')
    df.columns = ['date', 'Callee', 'nitrogen dioxide(ppm)', 'ozone(ppm)',
                  'Carbon monoxide(ppm)', 'Sulfur dioxide(ppm)', 'Fine dust (㎍/㎥)', 'Ultra fine dust']
    df = df.drop(['Callee', 'Ultra fine dust'], axis=1)
    df.date = df.date.apply(parse_date)
    df.set_index('date', inplace=True)

    pickle_out = open(pickle_name, 'wb')  # wb - write bytes
    pickle.dump(df, pickle_out)
    pickle_out.close()

    return df


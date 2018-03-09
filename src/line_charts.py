from src.data_manipulation import get_seoul_air_df
import matplotlib.pyplot as plt

df = get_seoul_air_df()

#
col_1_name = 'nitrogen dioxide(ppm)'
col_2_name = 'Sulfur dioxide(ppm)'

range_from = 0
range_to = 100

plt.plot(df.index[range_from: range_to], df[col_1_name].tolist()[range_from:range_to], label=col_1_name)
plt.plot(df.index[range_from: range_to], df[col_2_name].tolist()[range_from:range_to], label=col_2_name)

plt.xlabel('time')
plt.legend()
plt.show()

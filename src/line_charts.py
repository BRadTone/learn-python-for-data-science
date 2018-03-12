from src.data_manipulation import get_krakow_air_df
import matplotlib.pyplot as plt

main_df = get_krakow_air_df()

print(main_df.tail())

#
col_1_name = '857_pm10'
print(main_df[col_1_name].tolist())
# col_2_name = 'Sulfur dioxide(ppm)'

range_from = 1
range_to = 355

plt.plot(main_df.index[range_from: range_to], main_df[col_1_name].tolist()[range_from:range_to], label=col_1_name)
# plt.plot(df.index[range_from: range_to], df[col_2_name].tolist()[range_from:range_to], label=col_2_name)

plt.xlabel('time')
plt.legend()
plt.show()

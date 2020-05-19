# Write a Pandas program to get the day of month, day of year,
# week number and day of week from a given series of date strings.

# start
# import modules

import pandas as pd
from dateutil.parser import parse
date_series = pd.Series(['01 Jan 2015', '10-02-2016', '20180307', '2014/05/06', '2016-04-12', '2019-04-06T11:20'])
print(("Original Series:") + str(date_series))
date_series = date_series.map(lambda x: parse(x))
print("Day of month:")
print(date_series.dt.day.tolist())
print("Day of year:")
print(date_series.dt.dayofyear.tolist())
print("Week number:")
print(date_series.dt.weekofyear.tolist())
# print("Day of week:")
# print(date_series.dt.weekday_name.tolist())

# Write a Pandas program to convert a series of date strings to a timeseries.

# start
# import modules

import pandas as pd
date_series = pd.Series(['05 Jan 2016', '10-02-2011', '20180307', '2021/05/06', '2006-04-12', '2020-04-06T11:20'])
print(("Original Series:") + str(date_series))
print("\nSeries of date strings to a timeseries:")
print(pd.to_datetime(date_series))

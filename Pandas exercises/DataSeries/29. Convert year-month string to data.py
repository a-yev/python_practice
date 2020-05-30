# Write a Pandas program to convert year-month string
# to dates adding a specified day of the month.

# start
# import modules

import pandas as pd
# we use dateutil.parser
from dateutil.parser import parse
date_series = pd.Series(['Jan 2015', 'Feb 2016', 'Mar 2017', 'Apr 2018', 'May 2019'])
print(("Original Series:") + str (date_series))
print("\nNew dates:")
result = date_series.map(lambda d: parse('11 ' + d))
print(result)

# Write a Pandas program to convert Series of lists to one Series.

# start
# import modules

import pandas as pd

s = pd.Series([
    ['23', '45', '12'],
    ['72', '12'],
    ['10'],
    ['21', '90', '92', '12', '32']])
print(("Series of list: ") + str(s))
# print(s)
os = s.apply(pd.Series).stack().reset_index(drop=True)
print(("One Series: ") + str(os))

# Write a Pandas program to change the data type of given a column or a Series.

# start
# import modules

import pandas as pd
s1 = pd.Series(['24', '54', 'test', '312', '340'])
print("Original Data Series:")
print(s1)
print("Change the said data type to numeric:")
s2 = pd.to_numeric(s1, errors='errors')
print(s2)

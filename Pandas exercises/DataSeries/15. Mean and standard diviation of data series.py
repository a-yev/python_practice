# Write a Pandas program to create the mean and standard deviation of the data of a given Series.

# start
# import modules

import pandas as pd
s = pd.Series(data = [43,21,7,12,574,28,12,76,90,2])
print(("Original Data Series:") + str(s))
print("Mean of the said Data Series:")
print(s.mean())
print("Standard deviation of the said Data Series:")
print(s.std())

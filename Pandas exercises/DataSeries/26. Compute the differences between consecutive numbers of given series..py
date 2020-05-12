# Write a Pandas program to compute difference
# of differences between consecutive numbers of a given series.

# start
# import modules

import pandas as pd
series1 = pd.Series([34, 12, 32, 1, 32, 1, 43])
print(("Original Series:") + str(series1))
print("\nDifference of differences between consecutive numbers of the said series:")
print(series1.diff().tolist())
print(series1.diff().diff().tolist())

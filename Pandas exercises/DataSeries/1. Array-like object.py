# Write a Pandas program to create and display a one-dimensional
# array-like object containing an array of data.

# start

# import and check pandas
import pandas as pd
print(pd.__version__)

# creating array
a = pd.Series([3, 5, 6, 2, 1, 3, 8, 6, 7, 9, 0, 23, 64, 2, 1, 8, 0])
print(a)

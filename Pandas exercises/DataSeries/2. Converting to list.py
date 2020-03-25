# Write a Python program to convert a Panda module Series
# to Python list and it's type.

# start
# import module
import pandas as pd

# pandas series
a = pd.Series([4, 6, 12, 8, 98, 0, 34, 23, 2, 4, 2, 4, 65, 7, 12, 3, 4, 8])
print(("Pandas series") + str(a))

# converting series to list
print("List: ")
print(a.tolist())

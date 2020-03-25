# Write a Python program to convert a NumPy array to a Pandas series.

# start
# import modules

import numpy as np
import pandas as pd

np_array = np.array([10, 20, 23, 44, 53, 26, 87, 80])
print("NumPy array:")
print(np_array)
new_series = pd.Series(np_array)
print("Converted Pandas series:")
print(new_series)

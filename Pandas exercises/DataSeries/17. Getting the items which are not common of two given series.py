# Write a Pandas program to get the items which are not common of two given series.

# start
# import modules

import pandas as pd
import numpy as np
a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([2, 4, 6, 8, 10])
print("Original Series:")
print("a:")
print(a)
print("b:")
print(b)
print("\nItems of a given series not present in another given series:")
src = pd.Series(np.union1d(a, b))
srd = pd.Series(np.intersect1d(a, b))
result = src[~src.isin(srd)]
print(result)

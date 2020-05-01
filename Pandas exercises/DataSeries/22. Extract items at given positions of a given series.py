# Write a Pandas program to extract items at given positions of a given series.

# start
# import modules

import pandas as pd
import numpy as np

num_series = pd.Series(list('83849004390236239023'))
element_pos = [0, 2, 4, 8, 16]
print("Original Series:")
print(num_series)
result = num_series.take(element_pos)
print("\nExtract items at given positions of the said series:")
print(result)

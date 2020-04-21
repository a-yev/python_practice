# Write a Pandas program to compute the minimum, 20th percentile,
# median, 80th, and maximum of a given series.

# start
# import modules

import pandas as pd
import numpy as np
num_state = np.random.RandomState(80)
num_series = pd.Series(num_state.normal(4, 8, 16))
print("Original Series:")
print(num_series)
result = np.percentile(num_series, q=[1, 20, 32, 80, 85])
print("\nMinimum, 20th percentile, median, 75th, and maximum of a given series:")
print(result)

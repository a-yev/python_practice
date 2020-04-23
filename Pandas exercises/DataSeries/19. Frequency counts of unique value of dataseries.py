# Write a Pandas program to calculate the frequency counts of each unique value of a given series.

# start
# import modules

import pandas as pd
import numpy as np
num_series = pd.Series(np.take(list('098712347890134587613'), np.random.randint(8, size=32)))
print("Original Series:")
print(num_series)
print("Frequency of each unique value of the said series.")
result = num_series.value_counts()
print(result)

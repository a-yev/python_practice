# Display most frequent value in a given series and replace everything else as ‘Other’
# in the series

# start
# import modules

import pandas as pd
import numpy as np

np.random.RandomState(120)
num_series = pd.Series(np.random.randint(2, 6, [28]))
print("Original Series:")
print(num_series)
print("Top 2 Freq:", num_series.value_counts())
result = num_series[~num_series.isin(num_series.value_counts().index[:1])] = 'Other'

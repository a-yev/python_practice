# Write a Pandas program to compute
# the Euclidean distance between two given series.

# start
# import modules

import pandas as pd
import numpy as np
x = pd.Series([11, 23, 30, 45, 54, 67, 73, 87, 92, 110])
y = pd.Series([11, 8, 7, 5, 6, 5, 3, 4, 7, 1])
print(("Original series:") + str(x) + str(y))
print("\nEuclidean distance between two series:")
print(np.linalg.norm(x-y))

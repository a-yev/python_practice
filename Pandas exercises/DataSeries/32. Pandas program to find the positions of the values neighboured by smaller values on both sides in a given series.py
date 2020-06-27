# Pandas program to find the positions of the values neighboured by smaller values on both sides in a given series

# start
# import modules

import pandas as pd
import numpy as np
nums = pd.Series([1, 6, 3, 8, 5, 6, 2, 8, 34, 10, 6, 23, 75])
print(("Original series:") + str(nums))
print("\nPositions of the values surrounded by smaller values on both sides:")
temp = np.diff(np.sign(np.diff(nums)))
result = np.where(temp == -2)[0] + 1
print(result)

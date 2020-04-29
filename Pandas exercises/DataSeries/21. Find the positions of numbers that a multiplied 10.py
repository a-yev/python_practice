# Write a Pandas program to find the positions
# of numbers that are multiples of 10 of a given series.

# start
# import modules

import pandas as pd
import numpy as np
a = pd.Series(np.random.randint(2, 10, 10))
print(("Original Series:") + str(a))
result = np.argwhere(a % 10==0)
print(("Positions of numbers that are multiples of 10:") + str(result))

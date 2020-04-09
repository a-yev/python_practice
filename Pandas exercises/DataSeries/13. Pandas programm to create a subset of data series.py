# Create a subset of a given series based on value and condition.

# start
# import modules

import pandas as pd
s = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 8])
print (("Original data series is: ") + str (s))
print("\nSubset of the given Data Series:")
n = 4
new_s = s[s < n]
print(new_s)

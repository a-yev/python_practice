# Write a Pandas program to convert a given Series to an array.

# start
# import modules

import pandas as pd
import numpy as np

# defining data series
s = pd.Series(['pandas', '400', 'numpy', 'python', '20'])
print("The Data Series is: ")
print(s)
# converting series to data frame
print("The array is: ")
a = np.array(s.values.tolist())
print (a)

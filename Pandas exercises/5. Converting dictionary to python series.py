# Write a Python program to convert a dictionary to a Pandas series.

# start
# import module

import pandas as pd
dict = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800}
print(("Dictionary: \n") + str(dict))
print(("Series: \n") + str(pd.Series(dict)))

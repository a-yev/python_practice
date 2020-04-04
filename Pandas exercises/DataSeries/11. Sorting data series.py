# Write a Pandas program to sort a given Series.

# start
# import modules

import pandas as pd

# define series

s = pd.Series(['test', '24', '80', '10', '40'])
print(("Data Series is:") + str(s))
s1 = pd.Series(s).sort_values()
print(s1)

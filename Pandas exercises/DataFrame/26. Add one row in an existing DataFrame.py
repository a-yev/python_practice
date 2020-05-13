# Write a Pandas program to add one row in an existing DataFrame.

# start
# import modules

import pandas as pd
import numpy as np

d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print(("Original DataFrame")+str(df))
print('After add one row:')
df2 = {'col1': 10, 'col2': 11, 'col3': 12}
df = df.append(df2, ignore_index=True)
print(df)

# Write a Pandas program to select a row of series/dataframe by given integer index.

# start
# import modules

import pandas as pd
import numpy as np

d = {'col1': [1, 4, 3, 4, 5], 'col2': [4, 5, 6, 7, 8], 'col3': [7, 8, 9, 0, 1]}
df = pd.DataFrame(data=d)
print(("Original DataFrame") + str(df))
result = df.iloc[[2]]
print(("Index-2: Details") + str(result))

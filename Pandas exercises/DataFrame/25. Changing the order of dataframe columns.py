# Write a Pandas program to change the order of a DataFrame columns.

# start
# import modules

import pandas as pd
import numpy as np
from pandas import DataFrame

d = {'col1': [1, 4, 3, 4, 5], 'col2': [6, 7, 8, 9, 0], 'col3': [7, 8, 9, 0, 1]}
df: DataFrame = pd.DataFrame(data=d)
print(("Original DataFrame") + str(df))
df = df[['col3', 'col2', 'col1']]
print(('After altering col1 and col3') + str(df))

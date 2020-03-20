# Write a Pandas program to create and display a DataFrame from
# a specified dictionary data which has the index labels.

# start
# import module

import pandas as pd
import numpy as np

# creating dictionary
results = {'surname': ['Dvorak', 'Nowacki', 'Harket', 'Lundt',
'Jensen', 'Kardif', 'Bergger', 'Aronson', 'Verin', 'Ulemaa'],
        'score': [1.5, 9, 16.5, np.nan, 20, 12, 4.5, np.nan, 8, 18],
        'attempts': [2, 1, 1, 4, 1, 2, 2, 3, 1, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no',
        'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# creating a dataframe from dictionary
df = pd.DataFrame(results, index=labels)
print(df)

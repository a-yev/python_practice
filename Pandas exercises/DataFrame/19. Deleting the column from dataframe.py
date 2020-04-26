# Write a Pandas program to delete the 'qualify' column from the DataFrame.

# start
# import modules

import pandas as pd
import numpy as np

results = {'surname': ['Dvorak', 'Nowacki', 'Harket', 'Lundt',
                       'Jensen', 'Kardif', 'Bergger', 'Aronson', 'Verin', 'Ulemaa'],
           'score': [1.5, 9, 16.5, np.nan, 20, 12, 4.5, np.nan, 8, 18],
           'attempts': [2, 1, 1, 4, 1, 2, 2, 3, 1, 1],
           'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no',
                       'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(results, index=labels)
print("Orginal rows:")
print(df)
print("\nDelete the 'qualify' column from the data frame:")
df.pop('qualify')
print(df)

# Write a Pandas program to replace all the NaN values with Zero's in a column of a dataframe.
# start
# import modules

import pandas as pd
import numpy as np

exam_data = {'surname': ['Dvorak', 'Nowacki', 'Harket', 'Lundt',
                       'Jensen', 'Kardif', 'Bergger', 'Aronson', 'Verin', 'Ulemaa'],
           'score': [1.5, 9, 16.5, np.nan, 20, 12, 4.5, np.nan, 8, 18],
           'attempts': [2, 1, 1, 4, 1, 2, 2, 3, 1, 1],
           'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no',
                       'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data)
print("Original DataFrame")
print(df)
df =  df.fillna(0)
print("\nNew DataFrame replacing all NaN with 0:")
print(df)

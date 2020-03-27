# Write a Pandas program to count the number of rows and columns of a DataFrame.

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

df = pd.DataFrame(results , index=labels)
total_rows=len(df.axes[0])
total_cols=len(df.axes[1])
print("Number of Rows: "+str(total_rows))
print("Number of Columns: "+str(total_cols))

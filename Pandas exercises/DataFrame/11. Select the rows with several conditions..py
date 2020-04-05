# Write a Pandas program to select the rows where number of attempts in the examination is less than 4
# and score greater than 8.

# start
# import modules

import pandas as pd
import numpy as np

# define dataframe
results = {'surname': ['Dvorak', 'Nowacki', 'Harket', 'Lundt',
'Jensen', 'Kardif', 'Bergger', 'Aronson', 'Verin', 'Ulemaa'],
        'score': [1.5, 9, 16.5, np.nan, 20, 12, 4.5, np.nan, 8, 18],
        'attempts': [2, 1, 1, 4, 1, 2, 2, 3, 1, 1],
        'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no',
        'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# selecting rows
df = pd.DataFrame(results , index=labels)
print("Number of attempts in the examination is less than 2 and score greater than 15 :")
print(df[(df['attempts'] < 4) & (df['score'] > 8)])

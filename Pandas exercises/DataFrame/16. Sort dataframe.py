# Write a Pandas program to sort the DataFrame first by 'name' in descending order,
# then by 'score' in ascending order.

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
print(("Orginal dataframe:") + str(results))
result_sort=df.sort_values(by=['surname', 'score'], ascending=[True, True])
print("Sort the data frame first by ‘name’ in descending order, then by ‘score’ in ascending order:")
print(result_sort)

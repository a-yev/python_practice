# Write a Python Pandas program to convert the first column of a DataFrame as a Series.

# start
# import modules

import pandas as pd
df = pd.DataFrame({'x': [4, 34, 12, 40, 82, 42], 'y': [43, 25, 76, 89, 43, 10], 'z': [72, 52, 80, 72, 134, 42]})
# df = pd.DataFrame(data=d)
print(("Original DataFrame") + str(df))
# print(df)
s = df.iloc[:,0]

print(("First column converted to series: \n") + str(s))

# print("\n1st column as a Series:")
# print(s)
# print(type(s))

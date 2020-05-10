# Write a Pandas program to calculate the number of characters in each word in a given series.

# start
# import

import pandas as pd
series1 = pd.Series(['Php', 'Python', 'Java', 'C#'])
print(("Original Series:") + str(series1))
result = series1.map(lambda x: len(x))
print(("\nNumber of characters in each word in the said series:") + str(result))

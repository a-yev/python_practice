# Get the items of a given series not present in another given series

# start
# import modules

import pandas as pd

a = pd.Series([1, 2, 3, 4, 5])
b = pd.Series([2, 4, 6, 8, 10])
print("Original Series is:")
print(("a:") + str(a))
print(("b:") + str(b))
print("\nItems of sr1 not present in sr2:")
result = a[~a.isin(b)]
print(result)

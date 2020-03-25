# Write a Python program to compare to data series.

# start
# import module

import pandas as pd
ds1 = ([2, 4, 6, 8, 10])
ds2 = ([1, 3, 5, 7, 9])
print(("The first ds is: ") + str(ds1))
print(("The second ds is: ") + str(ds2))

# comparison
print(("Are data series equel? ") + str(ds1 == ds2))
print(("Is the first data serie greater? ") + str(ds1 > ds2))
print(("Is the second data serie greater? ") + str(ds2 < ds1))


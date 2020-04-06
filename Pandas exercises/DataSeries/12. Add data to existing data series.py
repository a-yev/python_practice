# Add some data to an existing Series

# start
# import modules

import pandas as pd

# defining data series
a = pd.Series(['20', '10', '50', '60', '80', '20', '70'])
print(("The data series is:") + str(a))
# add data
print("\nData Series after adding some data:")
new_a = a.append(pd.Series(['10', '32']))
print(new_a)

# Write a Pandas program to filter words
# from a given series that contain atleast two vowels.

# start
# import modules

import pandas as pd
from collections import Counter
color_series = pd.Series(['Red', 'Green', 'Orange', 'Pink', 'Yellow', 'White'])
print(("Original Series:") + str (color_series))
print("\nFiltered words:")
result = mask = color_series.map(lambda c: sum([Counter(c.lower()).get(i, 0) for i in list('aeiou')]) >= 2)
print(color_series[result])

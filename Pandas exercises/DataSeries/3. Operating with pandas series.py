# Write a Python program to add, subtract, multiple and divide two Pandas Series.

# start
# import pandas

import pandas as pd
a = pd.Series([23, 24, 65, 12, 90, 24])
b = pd.Series([54, 23, 6, 12, 8, 10])
c = a + b
print("Add two Series:")
print(c)
print("Subtract two Series:")
d = a - b
print(d)
print("Multiply two Series:")
e = a * b
print(e)
print("Divide Series1 by Series2:")
f = a / b
print(f)


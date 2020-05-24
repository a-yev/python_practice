# Write a Pandas program to count city wise number
# of people from a given of data set (city, name of the person).

# start
# import modules

import pandas as pd
df1 = pd.DataFrame(dict(name=['Dvorak', 'Nowacki', 'Harket', 'Lundt',
                       'Jensen', 'Kardif', 'Bergger', 'Aronson', 'Verin', 'Ulemaa'],
                        city=['California', 'Los Angeles', 'California', 'California', 'California', 'Los Angeles',
                              'Los Angeles',
                              'Georgia', 'Georgia', 'Los Angeles']))
g1 = df1.groupby(["city"]).size().reset_index(name='Number of people')
print(g1)

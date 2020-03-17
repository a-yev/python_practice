# Take two lists, say for example these two:

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements
# that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this

# start
# import module
import random

# define lists
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(("The first list is: ") + str(a))
print(("The second list is: ") + str(b))

# create result list
c = []
for num in a:
    if num in b:
        c.append(num)

print(
    ("The list that contains only the elements\n that are common between the lists: ") + str(c)
     )

# generate random lists


d = random.sample(range(10), 10)
e = random.sample(range(15), 15)

print(("The first random list is: ") + str(d))
print(("The second random list is: ") + str(e))

# create result list
f = []
for num in d:
    if num in e:
        f.append(num)

print(
    ("The list that contains only the elements that are common \n between the random generated lists: ") + str(f)
    )

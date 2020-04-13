# A programm that creates a new list with only even elements of given list.

# start
# defining the list
a = [23, 41, 54, 85, 90, 10, 22, 35, 67, 98, 42, 73]
print(("The list is: ") + str(a))

# new list
b = [value for value in a if value%2 == 0]
print(("New list with even elements is: ") + str(b))

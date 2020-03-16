# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of
# the list that are less than 5.
# Extras:
# Instead of printing the elements one by one, make a new list that has all
# the elements less than 5 from this list in it
# and print out this new list.
# Write this in one line of Python.
# Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than
# that number given by the user.

# start
# defining list
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# printing list and elements that are less than 10
print (("The list is: ") + str(a))
print (("The elements that are less than 10 in list are: ") + str(
    [i for i in a if i < 10]))

# ask user for a number
num = int(input("Please enter the number: "))

# printing the elements of list thatare less tan users number
print (("The elements that are less than your number in list are: ") + str(
    [i for i in a if i < num]))

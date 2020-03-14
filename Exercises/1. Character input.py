"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells
them the year that they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous
message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing
the ENTER button)
"""
#start
import datetime

#name info
name = input("Enter your name: ")
print("Your name: " + name)

#age info
age = input("Enter your age: ")
age = int(age)
print("Your age: " + str(age))

#current year info
current_year = datetime.datetime.today().year
print("Current year: " + str(current_year))
current_year = int(current_year)

#year that user will turn to 100 years old
year100 = (int(current_year) - age +100)
year100 = int(year100)

#result printing
print(str(name) + " will be 100 years old in " + str(year100) + " year")





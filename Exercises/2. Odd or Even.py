# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?
# Extras:
# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num)
# and one number to divide by (check).
# If check divides evenly into num, tell that to the user.
# If not, print a different appropriate message.

# start
# importing modules
import sys

# numbers input
number = int(input("Please, enter any number: "))
check = int(input("Please, enter another number to divide by: "))


# checking check number
if check == 0:  # jeśli check = 0, to go usuawasz i pobierasz na nowo? :)
    check = None  # clearing variable if check == 0
    check = int(input("The division by zero is not possible. "
                      "Please, enter another number to divide by: "))

# checking type of the number
numbertype = int(number % 4)
if number % 4 == 0:
    print("The number {} is odd and divisible by 4"
          .format(number))
# używaj .format() do printowania, podpunkty #2 i #3:
# https://realpython.com/python-string-formatting/
elif number % 2 == 0:
    print("The number {} is odd and not divisible by 4"
          .format(number))
else:
    print("The number {} is eve".format(number))

# checking how number reacts with check number
if number % check == 0:
    print("The number {} is divisible by {} ".format(number, check))
else:
    print("The number {} is not divisible by {}."
          .format(number, check))
    sys.exit()  # exit from python

# checking the result of dividing number by check number
result = int(number / check)
print('The result of dividing {} by {} is {} '.
      format(number, check, result))

# exit from python
sys.exit()

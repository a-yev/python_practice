# Ask the user for a string and print out whether this string
# is a palindrome or not.

# start
# input string

a = (str(input("Input a string: ")))
arevers = a[::-1]
print(("Reverse string is: ") + str(arevers))

# check is string a palindrome
if a == arevers:
    print("Inputed string is a palindrome")
else:
    print("Inputed string is not a palindrome")

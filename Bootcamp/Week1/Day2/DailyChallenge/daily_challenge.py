#!/usr/bin/python3

#Instructions
#
# 1.   Using the input function, ask the user for a string. The string must be 10 characters long.
#        If it’s less than 10 characters, print a message which states “string not long enough”.
#        If it’s more than 10 characters, print a message which states “string too long”.
#        If it’s 10 characters, print a message which states “perfect string” and continue the exercise.
#
# 2.   Then, print the first and last characters of the given text.
#
#    The user enters "HelloWorld"
#    Then you have to print 
#    H
#    d
#
#
#
#    3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
#
#    The user enters "HelloWorld"
#    Then, you have to construct the string character by character
#    H
#    He
#    Hel
#    ... etc
#    HelloWorld
#
#
#
#    4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:
#
#    Hlrolelwod

import random

s1 = input("Type a string with 10 characters long\n")

if len(s1) == 10:
    print("perfect string")
elif len(s1) > 10:
    print("string too long")
else: # < 10
    print("string not long enough")


s2 = input("Type a string\n")

print(f"printing the first: {s2[0]}")
print(f"printing the last: {s2[-1]}")


s3 = input("Type a string\n")

temp_string = ""
for char in s3:
    temp_string += char
    print(temp_string)

s4 = input("Type a string\n")
shuffled_list = list(s4)

random.shuffle(shuffled_list)
shuffled_string = "".join(shuffled_list)  # Convert back to string
print(f"\nShuffled string: {shuffled_string}")

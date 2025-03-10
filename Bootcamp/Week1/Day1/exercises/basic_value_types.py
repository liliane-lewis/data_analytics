#!/usr/bin/python3
#
# Exercise
#
# Working with the following string:
#
# description = "strings are..."
#
#
#   make it all uper case
#   replace the word "are" to "is"
#   print just the word "strings"

descripton = "strings are..."
new_description=(descripton.upper()).replace("ARE","IS")
print(new_description.split()[0])


# Exercise
#
# In the python shell, Create a variable called my_age, use python to know how old you will be in 123879 years


my_age=99

new_age = my_age + 123879
print(f"I will be  {new_age} years old")

# Exercise
#
# Check what is the type of each value, then change it: if it is a string, make it an integer and vice-versa:
#
# bank_balance = '33000'
# phone_number = 532287514


bank_balance = '33000'
phone_number = 532287514

print(type(bank_balance))
print(type(phone_number))
bank_balance=int(bank_balance)
phone_number=str(phone_number)
print(type(bank_balance))
print(type(phone_number))

first_name="Liliane"
last_name="Lewis Zukerman"
print(f"{first_name} {last_name}")

# Exercise
#
# Given the following values:

# x = 5
# y = 10
# z = 0
# word1 = "hello"
# word2 = "world"


# 1. Check if x is less than y and y is greater than z.
# 2. Verify if word1 is not equal to word2.
# 3. Use the bool() function to check the boolean value of z and word1.

x = 5
y = 10
z = 0
word1 = "hello"
word2 = "world"

if (x < y) and (y > z):
    print("x is less than y and y is greater than z")
else:
    print("x is great than y OR y is less z, or BOTH")

print(bool(z))
print(bool(word1))
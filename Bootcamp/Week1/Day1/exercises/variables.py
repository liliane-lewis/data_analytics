#!/usr/bin/python3

# Exercise 1
#
# You have a friend named Alice, and you want to send her a message with the following details:
#
# Name: Alice
# Age: 30
# City: New York
#
#T asks:
#
# Use f-strings to print a message saying:
#
# "Hello, Alice! You are 30 years old and live in New York."

# Use str.format() to print the same message.

name="Alice"
age=30
city="New York"

print(f"Hello, {name}! You are {age} years old and live in {city}.")

print("Hello, {}! You are {} years old and live in {}.".format(name, age, city))


# Exercise 2
# Ask the user for their age using the input() function and store it in a variable age.
# Convert the inputted age into an integer and calculate the number of years until they turn 100.
# Display a message: "You will turn 100 in X years", where X is the number of years calculated.

age = int(input("Enter your age:\n"))
years_until_100 = 100 - age
print(f"You will turn 100 in {years_until_100} years")


# Exercise

#Analyze the code below and predict what the outcome will be. Check the results in your python shell.

age = input("How old are you? ")
print(f"You are {age} years old")

# the output is normal. age in this case is a string

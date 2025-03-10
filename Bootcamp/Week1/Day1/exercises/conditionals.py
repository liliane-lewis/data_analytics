#!/usr/bin/python3


# Exercise
# 1. ask the user to enter his/her name
# 2. use the len() function to check the lenght of the name. if it is less than 5 letter print('You have a short name :)')

name = input("What is your name? \n")

lenght = len(name)

if lenght < 5:
    print("You have a short name :)")

# Exercise

# Ask the user for a number between 1 and 100
# If the number is a multiple of three, print Fizz
# If the number is a multiple of five, print Buzz.
# If the number is a multiple is a multiples of both three and five, print FizzBuzz instead.

number = int(input("Type a number between 1 and 100\n"))

mod3 = number % 3
mod5 = number %5


if not mod3 and not mod5:
    print("FizzBuz")
elif not mod5:
    print("Buzz")
elif not mod3:
    print("Fizz")
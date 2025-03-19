#!/usr/bin/python3

#Exercise 4 : Random
#Instructions

#    Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
#    Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

import random

def generate_random_number():
    return random.randint(1, 100)

user_number = int(input("Enter a number (1-100): \n"))
if 1 <= user_number <= 100:
    random_num = generate_random_number()
    if user_number == random_num:
        print(f"You guessed the number! It is {user_number}.")
    else:
        print(f"The number {user_number} is wrong. The right number is {random_num}.")
else:
    print("Invalid number.")

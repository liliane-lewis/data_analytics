#Project Overview

#This project involves creating a simple Number Guessing Game using Python. The program will generate a random number between 1 
# and 100, and the player will have a limited number of attempts to guess the correct number. After each guess, the program will 
# provide feedback, indicating whether the guess is too low, too high, or correct.

import random

max_attempts = 7
ran = random.randint(1, 100)
print(ran)

def guess(ran,num):
    if num < ran:
        print("the guess is too low")
    elif num > ran:
        print("the guess is too high")
    elif num == ran:
        print("correct")
        return True
    return False
for i in range(max_attempts):
    print(f"Try #{i + 1}\n")
    num = int(input("Type a number between 1 -100\n"))
    ret = guess(ran,num)
    if ret:
        break

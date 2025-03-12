#!/usr/bin/python3

import random


#Exercise 9 : Random number
#Instructions

#    Ask the user to input a number from 1 to 9 (including).
#    Get a random number between 1 and 9. Hint: random module.
#    If the user guesses the correct number print a message that says Winner.
#    If the user guesses the wrong number print a message that says better luck next time.
#    Bonus: use a loop that allows the user to keep guessing until they want to quit.
#    Bonus 2: on exiting the loop tally up and display total games won and lost.

win_count = 0
loss_count = 0


while True:
    user_input = input("\nWrite a number from 1 to 9 (or type 'quit' to exit):\n")
    if user_input.lower() == "quit":
        break

    num = int(user_input)
    if num < 1 or num > 9:
        print("Please enter a number between 1 and 9.")
        continue

    random_num = random.randint(1, 9)

    if num == random_num:
        print(f"Winner! The correct number was {random_num}. Congratualtions!")
        win_count += 1
    else:
        print(f"Wrong guess. The correct number was {random_num}. Better luck next time!")
        loss_count += 1


print("Game Over!")
print(f"Total of Wins: {win_count}")
print(f"Total of Losses: {loss_count}")

#!/usr/bin/python3


# game.py – this will contain a Game class which will have functions to play a single game of rock-paper-scissors against the computer, determine the 
# game’s result, and return the result.

#Part I - game.py
#
#    game.py – this file/module should contain a class called Game. It should have 4 methods:
#        get_user_item(self) – Ask the user to select an item (rock/paper/scissors). Keep asking until the user has selected one of the items – use data 
# validation and looping. Return the item at the end of the function.
#
#        get_computer_item(self) – Select rock/paper/scissors at random for the computer. Return the item at the end of the function. Use python’s 
# random.choice() function (read about it online).
#
#        get_game_result(self, user_item, computer_item) – Determine the result of the game.
#            Parameters:
#                user_item – the user’s chosen item (rock/paper/scissors)
#                computer_item – the computer’s chosen (random) item (rock/paper/scissors)
#                Return either win, draw, or loss. Where win means that the user has won, draw means the user and the computer got the same item, and 
# loss means that the user has lost.
#
#        play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py). It will do 3 things:
#            Get the user’s item (rock/paper/scissors) and remember it
#
#            Get a random item for the computer (rock/paper/scissors) and remember it
#
#            Determine the results of the game by comparing the user’s item and the computer’s item
#                Print the output of the game; something like this: “You selected rock. The computer selected paper. You lose”, “You selected scissors. The computer selected scissors. You drew!”
#
#                Return the results of the game as a string: win;draw;loss;, where win means that the user has won, draw means the user and the computer got the same item, and loss means that the user has lost.


#!/usr/bin/python3

import random

class Game:

    def get_user_item(self):
        """Ask the user to select rock/paper/scissors. Keep asking until valid input is received."""
        while True:
            user_item = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
            if user_item in ['r', 'p', 's']:
                return user_item
            else:
                print("Invalid input. Please try again.")

    def get_computer_item(self):
        """Randomly choose rock/paper/scissors for the computer."""
        return random.choice(['r', 'p', 's'])

    def get_game_result(self, user_item, computer_item):
        """Determine the result of the game."""
        if user_item == computer_item:
            return "draw"
        elif (user_item == 'r' and computer_item == 's') or \
             (user_item == 'p' and computer_item == 'r') or \
             (user_item == 's' and computer_item == 'p'):
            return "win"
        else:
            return "loss"

    def play(self):
        """Play a round of rock-paper-scissors and return the result."""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
    
        #print(f"user_item: {user_item}, computer_item: {computer_item}")

        result = self.get_game_result(user_item, computer_item)

        items = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        print(f"You selected {items[user_item]}. The computer selected {items[computer_item]}. You {result}!")
        return result
    
if __name__ == "__main__":
    game = Game()
    game.play()


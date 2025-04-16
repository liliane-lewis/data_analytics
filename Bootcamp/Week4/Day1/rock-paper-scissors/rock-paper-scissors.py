#!/usr/bin/python3


from game import Game


#rock-paper-scissors.py – this will contain functions to show the main menu, handle user’s input, and show the game summary before exiting.
#
#
#get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation), and return the choice. 
#No looping should occur here.
#The possibles choices are : Play a new game or Show scores or Quit
#
#print_results(results) – this should print the results of the games played. It should have a single parameter named results; which will be a dictionary of the results of the games played. It should display these results in a user-friendly way, and thank the user for playing.

from game import Game

def get_user_menu_choice():

    print("\n=== Rock Paper Scissors ===")
    print("Choose an option:")
    print("(1) Play a new game")
    print("(2) Show scores")
    print("(x) Exit")

    choice = input("Enter your choice: ").lower()
    if choice in ['1', '2', 'x', 'q']:
        return choice
    else:
        print("Invalid choice.")
        return None


def print_results(results):
    print("\n=== Game Results ===")
    print(f"Wins:   {results.get('win', 0)}")
    print(f"Losses: {results.get('loss', 0)}")
    print(f"Draws:  {results.get('draw', 0)}")
    print("\nThank you for playing!")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()

        if choice == '1':
            game = Game()
            result = game.play()
            if result in results:
                results[result] += 1

        elif choice == '2':
            print_results(results)

        elif choice in ['x', 'q']:
            print_results(results)
            break

        else:
            print("Please select a valid option.")
if __name__ == "__main__":
    main()
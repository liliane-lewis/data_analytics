#!/usr/bin/python3

#  Mini-Project #2 - Hangman

#Instructions
#
#    The computer choose a random word and mark stars for each letter of each word.
#    Then the player will guess a letter.
#        If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
#        If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
#        The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
#        The player can’t guess the same letter twice.


import random

hangman = \
"""+--+ 
|    
|    
|\   """
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist).upper()
#print(word)

hangman_stages = {
    0: """
     +--+
     |  
     |  
     |\ 
    """,
    1: """
     +--+
     |  o
     |  
     |\ 
    """,
    2: """
     +--+
     |  o
     |  |
     |\ 
    """,
    3: """
     +--+
     |  o
     | /|
     |\ 
    """,
    4: """
     +--+
     |  o
     | /|\\
     |\ 
    """,
    5: """
     +--+
     |  o
     | /|\\
     |\/ 
    """,
    6: """
     +--+
     |  o
     | /|\\
     |\/ \\
    """
}


def display_hangman(stage):
    print(hangman_stages[stage])


def main():
    stage = 0
    letters_chosen = set()
    user_word = ['_' if char.isalpha() else char for char in word]

    while stage < 6 and '_' in user_word:
        print("\nCurrent word:", ' '.join(user_word))
        display_hangman(stage)
        c = input("Choose a letter: ").upper()
        
        if c in letters_chosen:
            print("Letter already chosen. Try again.")
            continue
        
        letters_chosen.add(c)

        if c in word:
            for i, letter in enumerate(word):
                print("ENTROU")
                if letter == c:
                    user_word[i] = c
                    print(f"USER WORD: {user_word}")
        else:
            stage += 1
    
    display_hangman(stage)
    
    if '_' not in user_word:
        print("Congratulations! You won! The word was:", word)
    else:
        print("Game over! The word was:", word)


main()

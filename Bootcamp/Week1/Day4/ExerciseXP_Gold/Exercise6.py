#!/usr/bin/python3


#Exercise 6: Words and letters
#Instructions

 #   Ask a user for 7 words, store them in a list named words.
 #   Ask the user for a single character, store it in a variable called letter.
 #   Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
 #   If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.


words = []

print("Write 7 words:\n")

for n in range(1, 8):
    new_word = input(f"Word number {n}: ")
    words.append(new_word)  # Fix: Store the word correctly

letter = input("Write a single character: ")
for word in words:
    if letter in word:
        index = word.index(letter)
        print(f"The letter {letter} is in the word {word} in the index {index}")
    else:
        print(f"The letter {letter} is not in the word {word}")



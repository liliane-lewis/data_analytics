#!/usr/bin/python3

#Instructions
#Challenge 1
#
#    Ask a user for a word
#
#    Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.
#        Make sure the letters are the keys.
#        Make sure the letters are strings.
#        Make sure the indexes are stored in a list and those lists are values.

#Examples
#
#"dodo" ➞ { "d": [0, 2], "o": [1, 3] }
#
#"froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }
#
#"grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3], 'e': [4], 's': [5]}

words = input("Write a word:\n")

words_dictionary = {}
index = 0
for c in words:
    if c not in words_dictionary:
        words_dictionary[c] = []  
    words_dictionary[c].append(index)
    index += 1

print(words_dictionary)

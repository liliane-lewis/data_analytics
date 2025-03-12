#!/usr/bin/python3

#Exercise 5: The Alphabet
#Instructions
#
#    Create a string of all the letters in the alphabet
#    Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.


alphabet = "abcdefghijklmnopqrstuvwxyz"

vowels = "aeiou"

for letter in alphabet:
    if letter in vowels:
        print(f"{letter} is a vowel")
    else:
        print(f"{letter} is a consonant")
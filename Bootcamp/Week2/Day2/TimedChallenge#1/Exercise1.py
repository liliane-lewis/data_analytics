#!/usr/bin/python3
#Count occurence

#Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.
#
#String: Programming is cool!
#Character: o
#3

#
#String: This is a great example
#Character: y
#0



def calculate_character(string,character):
    count = 0
    for c in string:
        if c == character:
            count += 1
    return count

string = input("Write a string: ")
character = input("Write a character to count: ")

print(calculate_character(string,character))
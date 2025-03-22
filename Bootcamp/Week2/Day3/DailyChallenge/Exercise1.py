#!/usr/bin/python3
#Instructions
#
#    Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after 
#    sorting them alphabetically.
#    Use List Comprehension
#
#Example:

#Suppose the following input is supplied to the program: without,hello,bag,world
#Then, the output should be: bag,hello,without,world


def sort_words(words):
    words_sorted = ",".join(sorted([word.strip() for word in words.split(",")]))
    return words_sorted

words = "without,hello,bag,world"

print(sort_words(words))
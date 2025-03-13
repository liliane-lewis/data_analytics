#!/usr/bin/python3

#Challenge 2
#
#    Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
#
#Examples
#
#user's word : "ppoeemm" ➞ "poem"
#
#user's word : "wiiiinnnnd" ➞ "wind"
#
#user's word : "ttiiitllleeee" ➞ "title"
#
#user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"

#  Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

word = input("write a word: \n")
new_word = ""
char_before = ""
for char in word:

    if char_before != char:
        new_word += (2*char)

    char_before=char

print(f"New word: {new_word}")

#!/usr/bin/python3

#Exercise 3: Check the index
#Instructions
#
#Using this variable
#
#names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
#
#Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
#
#Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

name = input("What is your name?\n")

if name in names:
    index = names.index(name)
    print(f"Index: {index}")
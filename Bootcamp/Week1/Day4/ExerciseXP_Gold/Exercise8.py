#!/usr/bin/python3

#Exercise 8 : List and Tuple
#Instructions
#
#Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
#
#Suppose the following input is supplied to the program: 34,67,55,33,12,98
#
#Then, the output should be:

#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

string_of_numbers = input("Write a list of numbers. Ex: 34,67,55,33,12,98:\n")
print(string_of_numbers)
print(type(string_of_numbers))

list_of_numbers = string_of_numbers.split(",")
print(list_of_numbers)
print(type(list_of_numbers))

new_list_of_numbers = []
for s in list_of_numbers:
    if s:
        new_list_of_numbers.append(s)

print(new_list_of_numbers)
print(type(new_list_of_numbers))




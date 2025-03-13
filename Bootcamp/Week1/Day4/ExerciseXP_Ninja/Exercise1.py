#!/usr/bin/python3

#Exercise 1: Formula
#Instructions
#
#    Write a program that calculates and prints a value according to this given formula:
#    Q = Square root of [(2 * C * D)/H]
#    Following are the fixed values of C and H:
#        C is 50.
#        H is 30.
#    Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results

#For example, if the user inputs: 100,150,180
#The output should be:
#18,22,24

import math 

C = 50
H = 30

def calculate_q(D):
    return int(math.sqrt((2 * C * D) / H))

numbers = input("Write comma-separated string of numbers. Eg: 1,4,6,7\n")
list_of_numbers = numbers.split(",")
list_of_results = []
for d in list_of_numbers:
    d = int(d.strip())
    q = calculate_q(int(d))
    list_of_results.append(q)

print(",".join(map(str, list_of_results)))

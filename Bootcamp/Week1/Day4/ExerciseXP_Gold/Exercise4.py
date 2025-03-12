#!/usr/bin/python3

#Exercise 4: Greatest Number
#Instructions

#Ask the user for 3 numbers and print the greatest number.

#Test Data
#Input the 1st number: 25
#Input the 2nd number: 78
#Input the 3rd number: 87

#The greatest number is: 87


num1 = int(input("Input the 1st number:\n"))
num2 = int(input("Input the 2nd number:\n"))
num3 = int(input("Input the 3rd number:\n"))


greatest_number = 0

if num1 > greatest_number:
    greatest_number = num1
if num2 > greatest_number:
    greatest_number = num2
if num3 > greatest_number:
    greatest_number = num3


print(f"The greatest number is: {greatest_number}")
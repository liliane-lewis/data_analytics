#!/usr/bin/python3

#Perfect number

#A perfect number is a positive integer that is equal to the sum of its divisors.
#However, the number itself is not included in the sum.

#    Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
#    Hint: Google perfect numbers

#Example

#Input -- Enter the number:6
#Output -- True

#Input -- Enter the number:10
#Output --  False

def divisors(num):
    div = [i for i in range(1, num) if num % i == 0]
    return div

x = int(input('Enter the Number:\n'))
sum_div = sum(divisors(x))

if x == sum_div:
    print("True")
else:
    print("False")

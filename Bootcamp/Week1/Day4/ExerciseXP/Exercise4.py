#!/usr/bin/python3

# Exercise 4: Floats
# Instructions
#
#    Recap – What is a float? What is the difference between an integer and a float?
#    A float represents a decimal number
#    A integer is also a number, but without a decimal part
#
#    Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
list1 = list(range(3, 11))
new_list = []
for l in list1:
    new_list.append(l/2)

print(new_list)

#or
num = [x / 2 for x in range(3, 11)]
print(num)

#    Can you think of another way to generate a sequence of floats?

numbers = []
num = 1.5
while num <= 5:
    numbers.append(num)
    num += 0.5
print(numbers)

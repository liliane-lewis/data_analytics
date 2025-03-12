#!/usr/bin/python3

#Exercise 7: Min, Max, Sum
#Instructions

# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. 
# Use the sum() function to see how quickly Python can add a million numbers.

list_of_numbers = range(1,1000001)


print(f"Minimum number: {min(list_of_numbers)}")  
print(f"Maximum number: {max(list_of_numbers)}") 


sum = sum(list_of_numbers)
print(f"Sum of numbers from 1 to 1,000,000: {sum}")
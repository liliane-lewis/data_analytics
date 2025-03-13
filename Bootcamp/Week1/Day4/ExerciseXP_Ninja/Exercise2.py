#!/usr/bin/python3
import random

#Exercise 2 : List of integers
#Instructions
#
#Given a list of 10 integers to analyze. For example:
#
#    [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#    [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#    [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#    [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

# 1. Store the list of numbers in a variable.
# 2  Print the following information:
#    a. The list of numbers – printed in a single line
#    b. The list of numbers – sorted in descending order (largest to smallest)
#    c. The sum of all the numbers
# 3. A list containing the first and the last numbers.
# 4. A list of all the numbers greater than 50.
# 5. A list of all the numbers smaller than 10.
# 6. A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.
# 7. The numbers without any duplicates – also print how many numbers are in the new list.
# 8. The average of all the numbers.
# 9. The largest number.
#10  The smallest number.
#11. Bonus: Find the sum, average, largest and smallest number without using built in functions.
#12. Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100
#  – repeat this question 10 times. Each number should be added into a variable that you created earlier.
#13. Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
#14. Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.
#15. Bonus: Will the code work when the number of random numbers is not equal to 10?


numbers = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]

#2
# a
print(f"List: {numbers}")

# b
rev_sorted_numbers = sorted(numbers, reverse=True)
print(f"Ordered and reverted list: {rev_sorted_numbers}")

# c
sum_numbers = sum(numbers)
print(f"Sum of numbers: {sum_numbers}")

# 3
new_list = []
new_list.append(numbers[0])
new_list.append(numbers[-1])
print(f"First and lats number: {new_list}")

# 4

new_list = []
for num in numbers:
    if num > 50:
        new_list.append(num)
print(f"Greater than 50: {new_list}")

#5
new_list = []
for num in numbers:
    if num < 10:
        new_list.append(num)
print(f"Last than 10 {new_list}")

#6
square = []
for num in numbers:
    square.append(num*num)
print(f"Root suqare {square}")

#7 

unique_numbers = list(set(numbers))
print(f"unique numbers: {unique_numbers}")
print(f"Number in the new list: {len(unique_numbers)}")

#8

average = sum(numbers) / len(numbers)
print(f"Average: {average}")

#9
largest = max(numbers)
print(f"The largest number is: {largest}")

# 10.

smallest = min(numbers)
print(f"The smallest number is: {smallest}")

#11.

sum = 0
count = 0
for n in numbers:
    sum += n
    count += 1
print(f"Sum of numbers: {sum_numbers}")

print(f"Average: {sum/count}")



largest = -1000
for n in numbers:
    if n > largest:
        largest = n
print(f"The largest number is: {largest}")

smallest = 10000000

for n in numbers:
    if n < smallest:
        smallest = n
print(f"The smallest number is: {smallest}")

#12. 



#for i in range(10):
#    numbers.append(int(input(f"Enter number {i+1} (between -100 and 100): ")))

#print("User list:", numbers)

#13. 
for i in range(10):
    numbers.append(random.randint(-100,100))

print("Random list added:", numbers)

#14.
num_count = random.randint(50, 100)  

for i in range(num_count):
    numbers.append(random.randint(-100,100))

print(f"Generated {num_count} random numbers:")
print(numbers)

# 15
# It is necessary to use range(num_count) insted the range(10)
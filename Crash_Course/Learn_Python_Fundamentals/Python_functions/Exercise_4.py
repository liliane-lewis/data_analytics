#Write a function sum_list that takes a list of numbers as a parameter and returns the sum of all numbers in the list.

def sum_list(list):
    sum = 0
    for num in list:
        sum += num
    return sum

print(sum_list([1, 2, 3, 4]))  # Output: 10
print(sum_list([5, 5, 5]))  # Output: 15
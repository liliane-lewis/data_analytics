# Write a function find_largest that takes a list of numbers and returns the largest number in the list.

def find_largest(list):
    
    num = 0
    for l in list:
        if l > num:
            num = l
    return num

print(find_largest([1, 2, 3, 4]))  # Output: 4
print(find_largest([10, 20, 5]))  # Output: 20

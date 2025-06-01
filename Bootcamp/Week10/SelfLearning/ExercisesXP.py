
#!/usr/bin/python3

import numpy as np

# Exercise 1 : Array Creation and Manipulation
#Instructions
#
#Create a 1D NumPy array containing numbers from 0 to 9.
#
#Expected Output:
#
#
#array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

array_1D = np.arange(10)
print(array_1D)

# Exercise 2 : Type Conversion and Array Operations
#Instructions

#Convert a list [3.14, 2.17, 0, 1, 2] into a NumPy array and convert its data type to integer.

#Expected Output:


#array([3, 2, 0, 1, 2])

list = [3.14, 2.17, 0, 1, 2]

array_list = np.array(list, dtype=int)

print(array_list)


#🌟 Exercise 3 : Working with Multi-Dimensional Arrays
#Instructions

#Create a 3x3 NumPy array with values ranging from 1 to 9.

#Expected Output:
#
#
#array([[1, 2, 3],
#       [4, 5, 6],
#       [7, 8, 9]])

array_2D = np.arange(1, 10).reshape(3, 3)

print(array_2D)

#Exercise 4 : Creating Multi-Dimensional Array with Random Numbers
#Instructions

#Create a 2D NumPy array of shape (4, 5) filled with random numbers.

#Expected Output:


array_2D_reshape = np.round(np.random.rand(4, 5), 2)

print(array_2D_reshape)


#Exercise 5 : Indexing Arrays
#Instructions

#Select the second row from a given 2D NumPy array.

#Expected Output:


#array = np.array([[21,22,23,22,22],[20, 21, 22, 23, 24],[21,22,23,22,22]])

array = np.array([[21, 22, 23, 22, 22],
                  [20, 21, 22, 23, 24],
                  [21, 22, 23, 22, 22]])


second_row = array[1]

print(second_row)

#Exercise 6 : Reversing elements
#
# Instructions
#
#Reverse the order of elements in a given 1D NumPy array (first element becomes last).
#
#Expected Output:
#
#
#array([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])

array = np.arange(10)

reversed_array = array[::-1]

print(reversed_array)

#Exercise 7 : Identity Matrix
#Instructions
#
#Create a 4x4 identity matrix using NumPy.
#
#Expected Output:
#
#
#array([[1., 0., 0., 0.],
#       [0., 1., 0., 0.],
#       [0., 0., 1., 0.],
#       [0., 0., 0., 1.]])

array_4x4 = np.identity(4)
print(array_4x4)

#Exercise 8 : Simple Aggregate Funcs
#Instructions
#
#Find the sum and average of a given 1D array.
#
#Expected Output:


#Sum: 45, Average: 4.5


array_1D = np.arange(10)
array_1D_sum = np.sum(array_1D)
array_1D_avarage = np.average(array_1D)

print(array_1D)
print(array_1D_sum)
print(array_1D_avarage)



#Exercise 9 : Create Array and Change its Structure
#Instructions
#
#Create a NumPy array with elements from 1 to 20; then reshape it into a 4x5 matrix.
#
#Expected Output:
#
#
#array([[ 1,  2,  3,  4,  5],
#       [ 6,  7,  8,  9, 10],
#      [11, 12, 13, 14, 15],
#       [16, 17, 18, 19, 20]])


array = np.arange(1, 21).reshape(4, 5)
print(array)

#Exercise 10 : Conditional Selection of Values
#Instructions
#
#Extract all odd numbers from a given NumPy array.
#
#Expected Output:
#
#
#array([1, 3, 5, 7, 9])
array = np.arange(10)

odd_numbers = array[array % 2 == 1]

print(odd_numbers)

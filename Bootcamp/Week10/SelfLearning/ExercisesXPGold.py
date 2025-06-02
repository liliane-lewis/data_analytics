
#!/usr/bin/python3

import numpy as np

#Exercise 1 : Minimum and Maximum of Random Array
#Instructions
#
#Create a 5x5 array with random values and find the minimum and maximum values.
#
#Expected Output:
#
#
#Min: 0.01, Max: 0.99

array = np.round(np.random.rand(5, 5), 2)

min_val = np.min(array)
max_val = np.max(array)

print(array)
print("Min:", min_val, ", Max:", max_val)

#Exercise 2 : Matrix Normalization
#Instructions
#
#Normalize a 3x3 random matrix (subtract the mean and divide by the standard deviation of the matrix).
#
#Expected Output:
#
#
#array([[-1.22474487,  1.22474487],
 #      [ 0.        ,  0.        ]])


array2 = np.round(np.random.rand(3, 3), 2)
mean_value =  np.mean(array2)
std_value = np.std(array2)
print("Mean:", mean_value, ", STD:", std_value)

norm_array = (array2 - mean_value) / std_value

print("Normalized array:", norm_array)

#Exercise 3 : Evenly Spaced Elements in Array
#Instructions
#
#Create a 1D array of 50 evenly spaced elements between 0 and 10, exclusive.
#
#xpected Output:
#
#
#array([0. , 0.2, 0.4, ..., 9.6, 9.8, 10.])

array = np.round(np.linspace(0, 10, 50), 1)

print(array)


#Exercise 4 : Matrix Multiplication
#Instructions
#
#Multiply a 5x3 matrix by a 3x2 matrix (real matrix product).
#
#Expected Output:
#
#
#array([[ 8.79,  6.73],
#       [12.87,  9.77],
#       [16.92, 12.83],
#       [20.98, 15.89],
#       [25.04, 18.95]])


array4_A = np.round(np.random.rand(5, 3), 2)
array4_B = np.round(np.random.rand(3, 2), 2)

mul_array = array4_A @ array4_B
print(np.round(mul_array,2))


#Exercise 5
#Instructions
#
#    Utilize your understanding of matrix multiplication to solve this exercise.
#    Create two matrices of compatible dimensions.
#    Perform matrix multiplication on these matrices and display the result.
#    Ensure the dimensions of the matrices allow for valid multiplication.

#Tip: Remember that the number of columns in the first matrix should match the number of rows in the second matrix for successful 
# multiplication.


array5_A = np.round(np.random.rand(6, 4), 2)
array5_B = np.round(np.random.rand(4, 1), 2)

mul_array5 = array5_A @ array5_B
print(np.round(mul_array5,2))
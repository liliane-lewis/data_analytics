#!/usr/bin/python3

import math


# Daily challenge: Solve the Matrix
#Instructions
#
#Given a “Matrix” string:
#
#7ii
#Tsx
#h%?
#i #
#sM 
#$a 
##t%
#^r!


matrix_string = "7iiTsxh%?i #sM $a #t%^r!"
cols = 3
rows = len(matrix_string)/cols
rows = math.ceil(rows)

matrix = [['' for _ in range(cols)] for _ in range(rows)]

print(matrix)


index = 0
for r in range(rows):
    for c in range(cols):
        if index < len(matrix_string): 
            matrix[r][c] = matrix_string[index]
        else:
            matrix[r][c] = ' '
        index += 1
print(matrix)

def decode(matrix):
    decoded_text = ""
    for c in range(cols):
        for r in range(rows):
            decoded_text += matrix[r][c]
    print(decoded_text)

decode(matrix)
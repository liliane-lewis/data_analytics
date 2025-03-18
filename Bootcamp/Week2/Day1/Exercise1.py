#!/usr/bin/python3

# 
# Write a function calculation() such that it can accept two variables and calculate the addition and 
# subtraction of it. And also it must return both addition and subtraction in a single return call
def calculation(a, b):
    var_sum = a + b
    var_sub = a - b
    return var_sum, var_sub

a = 40
b = 10
var_sum,var_sub = calculation(a, b)
print(f"{a} + {b} = {var_sum}")
print(f"{a} - {b} = {var_sub}")
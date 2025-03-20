#!/usr/bin/python3
#Exercise 2 : Sum
#Instructions
#
#    Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.
#
#Example:
#If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)
#
#Hint: treating our number as a int or a str at different points in our code may be helpful



def print_num(num):
    
    num1 = int(str(num)) 
    num2 = int(str(num) * 2)  
    num3 = int(str(num) * 3) 
    num4 = int(str(num) * 4) 
    
    total = num1 + num2 + num3 + num4

    print(f"{total} ({num1} + {num2} + {num3} + {num4})")
    return total

num = int(input("Write a number beetween 0-9: "))
print_num(num)
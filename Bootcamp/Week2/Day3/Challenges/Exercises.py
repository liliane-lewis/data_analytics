#!/usr/bin/python3

import math

#Exercise 1
#Instructions
#Write a script that inserts an item at a defined index in a list.

fruits_list = ["banana", "apple", "blueberry"]

item = "melon"
index = 2

fruits_list.insert(index, item)
   

print(fruits_list)


#Exercise 2
#Instructions

#Write a script that counts the number of spaces in a string.

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed consequat at quam sed accumsan. Sed vel ornare turpis. " \
"Etiam tincidunt sem eu lacus scelerisque ultricies. Cras sollicitudin massa ut ante sagittis, quis cursus justo porttitor. Donec " \
"varius nunc id quam vehicula mollis. Maecenas egestas erat sit amet elementum molestie. In hac habitasse platea dictumst. Maecenas " \
"egestas vulputate neque. "
count_spaces = 0

#for c in string:
#    if c == " ":
#        count_spaces += 1
count_spaces = string.count(" ")

print(f"The string: \"{string}\" has {count_spaces} spaces")


#Exercise 3
#Instructions
#
#Write a script that calculates the number of upper case letters and lower case letters in a string.

string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed consequat at quam sed accumsan. Sed vel ornare turpis. " \
"Etiam tincidunt sem eu lacus scelerisque ultricies. Cras sollicitudin massa ut ante sagittis, quis cursus justo porttitor. Donec " \
"varius nunc id quam vehicula mollis. Maecenas egestas erat sit amet elementum molestie. In hac habitasse platea dictumst. Maecenas " \
"egestas vulputate neque. "
count_upper = string.count(" ")

def count_case_letters(string):
    upper_count = sum(1 for char in string if char.isupper())
    lower_count = sum(1 for char in string if char.islower())
    return upper_count, lower_count


upper, lower = count_case_letters(string)

print(f"Uppercase letters: {upper}")
print(f"Lowercase letters: {lower}")


#Exercise 4
#Instructions

#Write a function to find the sum of an array without using the built in function:
#
#>>>my_sum([1,5,4,2])
#>>>12

def my_sum(numbers):
    s = 0
    for num in numbers:
        s += num
    return s

print(my_sum([1,5,4,2]))


#Exercise 5
#Instructions
#
#Write a function to find the max number in a list
#
#>>>find_max([0,1,3,50])
#>>>50


def find_max(numbers):
    max = 0
    for n in numbers:
        if n > max:
            max = n
    return max

print(find_max([1,5,4,90]))

#Exercise 6
#Instructions
#
#Write a function that returns factorial of a number
#
#>>>factorial(4)
#>>>24


def calculate_factorial(number):
    fac = 1
    while number > 1:
        fac *= number
        number -= 1
    return fac

print(calculate_factorial(4))  # 24
print(calculate_factorial(5))  # 120
print(calculate_factorial(0))  # 1 (by definition)


#Exercise 7
#Instructions
#
#Write a function that counts an element in a list (without using the count method):
#
#>>>list_count(['a','a','t','o'],'a')
#>>>2

def list_count(lst, element):
    count = 0
    for item in lst:
        if item == element:
            count += 1
    return count


print(list_count(['a','a','t','o'],'a'))

#Exercise 8
#Instructions
#
#Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:
#
#>>>norm([1,2,2])
#>>>3


def norm(lst):
    squares = 0

    for l in lst:
        squares += l * l

    return math.sqrt(squares)


print("Exercise 8")
print(norm([1,2,2]))


#Exercise 9
#Instructions

#Write a function to find if an array is monotonic (sorted either ascending of descending)

#>>>is_mono([7,6,5,5,2,0])
#>>>True

#>>>is_mono([2,3,3,3])
#>>>True

#>>>is_mono([1,2,0,4])
#>>>False


def is_mono2(lst):
    control = True
    ascending = False
    descending = False
    i = 0 
    while (control):
        if lst[i] > lst[i + 1]:
            ascending = True
            control = False   
        elif lst[i] < lst[i + 1]:
            descending = True            
            control = False   
        else:
            i += 1

    i = 1
    if ascending:
        for i in range(len(lst) - 1):
            if lst[i] >= lst[i + 1]:
                pass
            else:
                return False
    

    if descending:
        for i in range(len(lst) - 1):
            if lst[i] <= lst[i + 1]:
                pass
            else:
                return False

    return True

def is_mono(lst):
    return all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1)) or \
           all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

print(is_mono([7,6,5,5,2,0])) #True

print(is_mono([2,3,3,3])) #True

print(is_mono([1,2,0,4])) #False


#Exercise 10
#Instructions

#Write a function that prints the longest word in a list.


def get_longest_word(lst):
    longest = ""
    for item in lst:
        if len(item) > len(longest):
            longest = item

    return longest


print(get_longest_word(["banana", "apple", "blueberry"]))



#Exercise 11
#Instructions
#
#Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

def separate_int_str(list):
    int_list = []
    str_list = []

    for i in list:
        if isinstance(i, int):
            int_list.append(i)
        elif isinstance(i, str):
            str_list.append(i)
    
    return int_list, str_list

numbers, words = separate_int_str([1, "apple", 2, "banana", 3, "cherry"])
print("Integers:", numbers)
print("Strings:", words)


#Exercise 12
#Instructions

#Write a function to check if a string is a palindrome:

#>>>is_palindrome('radar')
#>>>True

#>>>is_palindrome('John)
#>>>False


def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome('radar'))  # True
print(is_palindrome('John'))   # False
print(is_palindrome('level'))  # True
print(is_palindrome('hannah'))  # True

#Exercise 13
#Instructions
#
#Write a function that returns the amount of words in a sentence with length > k:
#
#>>>sentence = 'Do or do not there is no try'
#>>>k=2
#>>>sum_over_k(sentence,k)
#3>>>3


def sum_over_k(sentence,k):
    count = 0
    words = sentence.split()
    for w in words:
        if len(w) > k:
            count += 1
    return count
            

sentence = 'Do or do not there is no try'
k = 3
print(sum_over_k(sentence, k))


#Exercise 14
#Instructions
#
#Write a function that returns the average value in a dictionary (assume the values are numeric):
#
#>>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#>>>3

def dict_avg(d):
    return sum(d.values()) / len(d) if d else 0

print(dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1}))  # avg: 3
print(dict_avg({'x': 10, 'y': 20, 'z': 30}))  # avg: 20
print(dict_avg({}))  # ang: 0


# Exercise 15
#Instructions
#
#Write a function that returns common divisors of 2 numbers:
#
#>>>common_div(10,20)
#>>>[2,5,10]

def common_div(num1, num2):

    div_num1 = [n for n in range(1, num1 + 1) if num1 % n == 0]
    div_num2 = [n for n in range(1, num2 + 1) if num2 % n == 0]
    both = [n for n in div_num1 if n in div_num2]
    
    return both

print(common_div(10, 20))  # [1, 2, 5, 10]


#Exercise 16
#Instructions

#Write a function that test if a number is prime:
#
#>>>is_prime(11)
#>>>True

def is_prime(num):
    
    if num < 2:  # 0 and 1 are not prime
        return False

    div_num = [n for n in range(1, num + 1) if num % n == 0]
    if 1 in div_num and num in div_num and len(div_num ) == 2:
        return True
    else:
        return False
    

print(is_prime(11)) #True
print(is_prime(4)) #False
print(is_prime(13)) #True

#Exercise 17
#Instructions
#
#Write a function that prints elements of a list if the index and the value are even:
#
#>>>weird_print([1,2,2,3,4,5])
#>>>[2,4]

def weird_print(lst):
    even = []

    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 == 0:
            even.append(i)

    #even = [lst[i] for i in range(len(lst)) if i % 2 == 0 and lst[i] % 2 == 0]

    print(even)


weird_print([1,2,2,3,4,5])
        
    
#Exercise 18
#Instructions

#Write a function that accepts an undefined number of keyworded arguments and return the count of different types:
#
#>>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#>>>int: 1, str:1 , float:1, bool:2

def type_count(**kwargs):
    type_dict = {"int": 0, "str": 0, "float": 0, "bool": 0}
    
    for value in kwargs.values():
        if isinstance(value, bool):
            type_dict["bool"] += 1
        elif isinstance(value, int):
            type_dict["int"] += 1
        elif isinstance(value, str):
            type_dict["str"] += 1
        elif isinstance(value, float):
            type_dict["float"] += 1

    return type_dict

print(type_count(a=1,b='string',c=1.0,d=True,e=False)) #int: 1, str:1 , float:1, bool:2


#Exercise 19
#Instructions
#
#Write a function that mimics the builtin .split() method for strings.
#
#By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def my_split(sentence,arg=" "):
    my_string = []
    current_word = ""

    for char in sentence:
        if char == arg:
            if current_word:
                my_string.append(current_word)
                current_word = ""
        else:
            current_word += char
    
    if current_word:
        my_string.append(current_word)

    return my_string


print(my_split("This is my sentence", " "))
print(my_split("This is my sentence"))
print(my_split("This-is-my-sentence", "-"))


#Exercise 20
#Instructions
#
#Convert a string into password format.
#
#Example:
#input : "mypassword"
#output: "***********"

def password_format(inp):
    return "*" * len(inp)

inp = input("Write a password: ")

out = password_format(inp)
print(f"output: {out}")


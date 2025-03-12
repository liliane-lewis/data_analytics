#!/usr/bin/python3

#Exercise 1: Concatenate lists
#Instructions
#
#Write code that concatenates two lists together without using the + sign.

odd_list = [1,3,5,7,9]
even_list = [2,4,6,8]

final_list = []

final_list = even_list[:]

final_list.extend(odd_list)

print(final_list)
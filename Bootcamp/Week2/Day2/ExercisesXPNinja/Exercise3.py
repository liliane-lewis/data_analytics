#!/usr/bin/python3

#Exercise 3 : Box of stars
#Instructions

#Write a function named box_printer that takes any amount of strings (not in a list) and prints them, one per line, in a rectangular frame.
#For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:

#******************
#* Hello          *
#* World          *
#* in             *
#* reallylongword *
#* a              *
#* frame          *
#******************

def box_printer(*args):
    max_length = max(len(word) for word in args)
    border = "#" + "*" * (max_length + 4)
    
    print(border)
    for word in args:
        print(f"#* {word.ljust(max_length)} *")
    print(border)
#* Hello          *
#* World          *
#* in             *
#* reallylongword *
#* a              *
#* frame          *
#******************
box_printer("Hello", "World", "in", "reallylongword", "a", "frame")
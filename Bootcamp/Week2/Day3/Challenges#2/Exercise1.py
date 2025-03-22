#!/usr/bin/python3

#Instructions
#
#    Draw the following pattern using for loops:
#
#  *
# ***
#*****
###
#
#    Draw the following pattern using for loops:
#
#    *
#   **
#  ***
# ****
#*****
#
#
#    Draw the following pattern using for loops:
#
#*
#**
#***
#****
#*****
#*****
# ****
#  ***
#   **
#    *


def draw_pattern1(rows):
    max_width = 2 * rows - 1 #last line
    for i in range(1, max_width + 1, 2):
        stars = '*' * i
        print(stars.center(max_width))

draw_pattern1(3)



def draw_pattern2(rows):
    max_width = 2 * rows - 1 #last line
    for i in range(1, max_width + 1, 1):
        stars = '*' * i
        print(stars.rjust(max_width))

draw_pattern2(3)


def draw_pattern3(rows):
    max_width = 2 * rows - 1 #last line
    for i in range(1, max_width + 1, 1):
        stars = '*' * i
        print(stars.ljust(max_width))
    max_width = 2 * rows - 1 #last line
    #print("---")
    for i in range(max_width, 0, -1):
        stars = '*' * i
        print(stars.rjust(max_width))


draw_pattern3(3)
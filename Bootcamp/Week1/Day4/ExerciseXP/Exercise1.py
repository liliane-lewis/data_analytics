#!/usr/bin/python3

#Exercise 1 : Favorite Numbers
#Instructions
#
#    Create a set called my_fav_numbers with all your favorites numbers.
#    Add two new numbers to the set.
#    Remove the last number.
#    Create a set called friend_fav_numbers with your friend’s favorites numbers.
#    Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.


my_fav_numbers = {7,17,82,42,99}
print(f"my fav nums: {my_fav_numbers}")
my_fav_numbers.add(101)
print(f"my fav nums after add 101: {my_fav_numbers}")
my_fav_numbers.add(200)
print(f"my fav nums after add 200: {my_fav_numbers}")
my_fav_numbers.remove(200)
print(f"my fav nums after remove 200: {my_fav_numbers}")
friend_fav_numbers = {19,84,11,17,51,22,33}
print(f"my frinds fav nums: {friend_fav_numbers}")

our_fav_numbers = my_fav_numbers | friend_fav_numbers
print(f"Ours fav nums: {our_fav_numbers}")

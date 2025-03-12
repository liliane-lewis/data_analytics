#!/usr/bin/python3

#Exercise 5: For Loop
#Instructions

 #   Use a for loop to print all numbers from 1 to 20, inclusive.
 #   Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for i in range(1,21):
    print(i)


for i in range(1,21):
    if (i - 1) % 2 == 0:
        print(i)

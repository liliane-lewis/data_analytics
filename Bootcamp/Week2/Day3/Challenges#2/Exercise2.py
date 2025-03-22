#!/usr/bin/python3
#Exercise 2
#Instructions
#
#    Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes,
#  and add the final output. Try to understand the purpose of this program.

#It is a Sort algoritm

my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1): # Iterates through indices (0 to len-2)
    minimum = i # set the current index as the minimum value
    for j in range( i + 1, len(my_list)): # Iterate through the rest of the list
        if(my_list[j] < my_list[minimum]): # If a smaller value is found, update the index of the smaller value
            minimum = j
            if(minimum != i): #if the index is different of the current i..
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # swap the place of the minimum with the current number tested
print(my_list)


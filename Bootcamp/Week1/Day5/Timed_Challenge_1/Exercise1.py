#!/usr/bin/python3


#Reverse the Sentence
#
#Write a program to reverse the sentence wordwise.
#
#Input:
#You have entered a wrong domain
#Output:
#domain wrong a entered have You

#string = "You have entered a wrong domain"
REverseinp= input("Write a sentence\n")
string_list = list(REverseinp.split(" "))
reversed_list = list(reversed(string_list))
reversed = str(" ".join(reversed_list))
print(reversed) 
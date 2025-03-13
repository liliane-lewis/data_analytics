#!/usr/bin/python3
import string

#Exercise 4 : Frequency Of The Words
#Instructions

#Write a program that prints the frequency of the words from the input.

#Suppose the following input is supplied to the program:
#New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

#Then, the output should be:
#
#    2:2
#    3.:1
#    3?:1
#    New:1
#    Python:5
#    Read:1
#    and:1
#    between:1
#    choosing:1
#    or:2
#    to:1

input_text = input("Write a sentence: \n")
word_counts = {}
words = input_text.split()
clean_words = [word.strip(string.punctuation) for word in words] 
for word in clean_words:
    word_counts[word] = word_counts.get(word, 0) + 1


for w in sorted(word_counts):
    print(f"{w}:{word_counts[w]}") 
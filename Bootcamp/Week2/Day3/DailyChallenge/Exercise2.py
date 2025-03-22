#!/usr/bin/python3

#Challenge 2 : Longest Word
#Instructions
#
#    Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
#    Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).
#
#Examples
#
#longest_word("Margaret's toy is a pretty doll.") ➞ "Margaret's"
#
#longest_word("A thing of beauty is a joy forever.") ➞ "forever."
#
#longest_word("Forgetfulness is by all means powerless!") ➞ "Forgetfulness"

def longest_word(words):

    words_list = ([word.strip() for word in words.split(" ")])
    longest = ""
    for w in words_list:
        if len(w) > len(longest):
           longest =  w 

    print(longest)


longest_word("Margaret's toy is a pretty doll.") #➞ "Margaret's"
longest_word("A thing of beauty is a joy forever.")# ➞ "forever."
longest_word("Forgetfulness is by all means powerless!") #➞ "Forgetfulness"
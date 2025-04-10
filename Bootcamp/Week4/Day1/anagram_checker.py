#!/usr/bin/python3

#Anagram checker
#
#We will create a program that will ask the user for a word.
#It will check if the word is a valid English word, and then find all possible anagrams for that word.


import itertools

class AnagramChecker:
    def __init__(self):
        '''should load the word list file (text file) into a variable, so that it can be searched later on in the code.'''
        with open("sowpods.txt", "r") as file:
            self.content = file.read().splitlines()
        #return contents
        #print(contents)

    def is_valid_word(self, user_word):
        ''' should check if the given word (ie. the word of the user) is a valid word.'''
        if user_word in self.content:
            return True
        else:
            return False
        
    def get_anagrams(self,word):
        anagrams = []
        word = word.upper()
        word_list =  list(set([''.join(p) for p in itertools.permutations(word)]))
        for word in word_list:
            #print(word)
            if self.is_valid_word(word):
                anagrams.append(word)
        return anagrams




a = AnagramChecker()
#user_word = input("Type a word\n")
#print(a.get_anagrams(user_word))

#anagrams.py

#a.get_anagrams(user_word)

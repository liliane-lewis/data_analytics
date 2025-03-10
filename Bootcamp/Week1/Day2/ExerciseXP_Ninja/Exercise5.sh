#!/usr/bin/python3


#Exercise 5: Longest word without a specific character
#Instructions

#    Keep asking the user to input the longest sentence they can without the character “A”.
#    Each time a user successfully sets a new longest sentence, print a congratulations message.


sentence = ""
longest_sentence = ""

while "A" not in sentence: 
    sentence = input("Write the longest sentence you can without the character 'A' or 'a':\n")
    if 'A' in sentence.upper():
        print("Oops! You used the letter 'A' or 'a'. Game over!")
        break

    if len(sentence) > len(longest_sentence):
        longest_sentence = sentence
        len_longest = len(longest_sentence)
        print(f"Congratulations! You've set a new record of {len_longest} characteres!")
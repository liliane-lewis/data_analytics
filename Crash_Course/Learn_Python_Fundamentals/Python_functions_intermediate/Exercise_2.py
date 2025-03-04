# Write a function check_letter that takes a word and a letter as parameters and checks if the letter is in the word. It should return True if the letter is found and False if not.



def check_letter(word,letter):
    if letter in word:
        return True
    else:
        return False
print(check_letter("apple", "a"))  # Output: True
print(check_letter("banana", "z"))  # Output: False
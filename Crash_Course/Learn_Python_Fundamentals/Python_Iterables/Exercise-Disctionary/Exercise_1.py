#1. Given a list: [("name", "Elie"), ("job", "Instructor")], create a dictionary that looks like this: {'job': 'Instructor', 'name': 'Elie'} (Note: The order does not matter).

list = [("name", "Elie"), ("job", "Instructor")]
dictionary = dict(list)
print(dictionary)

#2. Given two lists: ["CA", "NJ", "RI"] and ["California", "New Jersey", "Rhode Island"], return a dictionary that looks like this: {'CA': 'California', 'NJ': 'New Jersey', 'RI': 'Rhode Island'}.


keys = ["CA", "NJ", "RI"]
values =  ["California", "New Jersey", "Rhode Island"]
dictionary = dict(zip(keys, values))
print(dictionary)

#3. Create a dictionary where the keys are vowels in the alphabet and the values are 0. Your dictionary should look like this: {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}. (Do not use the fromkeys method).

keys = ["a", "b", "c", "d", "e"]
values = [0,0,0,0,0]
dictionary = dict(zip(keys, values))
print(dictionary)

#4. Create a dictionary where the key is the position of the letter in the alphabet, and the value is the letter itself. You should return something like this:
#{1: 'A',
# 2: 'B',
# 3: 'C',
# 4: 'D',
# 5: 'E',
# 6: 'F',
# 7: 'G',
# 8: 'H',
# 9: 'I',
# 10: 'J',
# 11: 'K',
# 12: 'L',
# 13: 'M',
# 14: 'N',
# 15: 'O',
# 16: 'P',
# 17: 'Q',
# 18: 'R',
# 19: 'S',
# 20: 'T',
# 21: 'U',
# 22: 'V',
# 23: 'W',
# 24: 'X',
# 25: 'Y',
# 26: 'Z'}

import string
keys = range(1, 27)
values = string.ascii_uppercase
dictionary = dict(zip(keys, values))
print(dictionary)

#Super Bonus:

#Given the string "awesome sauce", return a dictionary where the keys are vowels, and the values are the count of each vowel in the string. Your dictionary should look like this: {'a': 2, 'e': 3, 'i': 0, 'o': 1, 'u': 1}.

string = "awesome sauce"
vowels = "aeiou" 
dictionary = {v: 0 for v in vowels} 
print(dictionary)

for s in string:
    if s in dictionary:
        dictionary[s] += 1

print(dictionary)

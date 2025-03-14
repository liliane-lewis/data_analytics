#!/usr/bin/python3

#Exercise 4 : Disney characters
#Instructions

#Use this list :
#
#users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
#
#Analyse these results :
#
##1

#>>> print(disney_users_A)
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

#2/
#
#>>> print(disney_users_B)
#{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

#3/ 
#
#>>> print(disney_users_C)
#{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
#
#
#    Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
#    Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
#    Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
#4.     Only recreate the 1st result for:
#        The characters, which names contain the letter “i”.
#        The characters, which names start with the letter “m” or “p”.

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]

# 1. Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
#>>> print(disney_users_A)
#{"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

disney_users_A = {}
count = 0
for user in users:
    disney_users_A[user] = count
    count += 1
print("\n Dictionary disney_users_A:")
print(disney_users_A)


#2/
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
#>>> print(disney_users_B)
#{0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}

disney_users_B = {}
count = 0
for user in users:
    disney_users_B[count] = user
    count += 1
print("\n Dictionary disney_users_B:")
print(disney_users_B)

#3/ 
#  Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
#>>> print(disney_users_C)
#{"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

def create_dictionary(name,count,dictionary):
    dictionary[count] = user
    return dictionary

disney_users_C = {}
sorted_users = sorted(users)

for index, user in enumerate(sorted_users):
    disney_users_C = create_dictionary(user,index,disney_users_C)

print("\n Dictionary disney_users_C:")
print(disney_users_C)


#4.     Only recreate the 1st result for:
#        The characters, which names contain the letter “i”.
#        The characters, which names start with the letter “m” or “p”.

new_disney_users_A = {}
count = 0
for user in users:
    if "i" in user:
        new_disney_users_A[user] = count
        count += 1
print("\n Dictionary disney_users_A recreated (The characters, which names contain the letter \"i\"):")
print(new_disney_users_A)

new2_disney_users_A = {}
count = 0
for user in users:
    if user.startswith("M") or user.startswith("P"):
        new2_disney_users_A[user] = count
        count += 1
print("\n Dictionary disney_users_A recreated (The characters,which names start with the letter \"m\" or \"p\":")
print(new2_disney_users_A)
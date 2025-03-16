#!/usr/bin/python3

#Exercise 1: Birthday Look-up
#Instructions

#    Create a variable called birthdays. Its value should be a dictionary.
#    Initialize this variable with birthdays of 5 people of your choice. For each entry in the dictionary, the key should be the person’s name, and the value 
#    should be their birthday. Tip : Use the format “YYYY/MM/DD”.
#    Print a welcome message for the user. Then tell them: "You can look up the birthdays of the people in the list!""
#        Ask the user to give you a person’s name and store the answer in a variable.
#        Get the birthday of the name provided by the user.
#        Print out the birthday with a nicely-formatted message.


birthdays = {"Maria": "1992/12/01",
             "Jose": "1984/05/19",
             "Antonio": "2001/08/13",
             "Carlos": "2005/02/23",
             "Monica": "1983/03/17"}


print(f"Wellcome!\n")
print("You can look up the birthdays of the people in the list!")
print(", ".join(birthdays.keys()))
name = input("Write a name:\n")
if name in birthdays:
    birthday = birthdays[name]
    print(f"The birthday of {name} is {birthday}.")
else:
    print(f"Name '{name}' not found.")





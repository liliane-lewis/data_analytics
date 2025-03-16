#!/usr/bin/python3

#Exercise 2: Birthdays Advanced
#Instructions
#
#    Before asking the user to input a person’s name print out all of the names in the dictionary.
#    If the person that the user types is not found in the dictionary, print an error message 
# (“Sorry, we don’t have the birthday information for <person’s name>”)


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
    print(f"Sorry, we don’t have the birthday information for {name}")



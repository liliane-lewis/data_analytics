#!/usr/bin/python3

#Exercise 3: Add Your Own Birthday
#Instructions
#
#    Add this new code: before asking the user to input a person’s name to look up, ask the user to add a new birthday:
#        Ask the user for a person’s name – store it in a variable.
#        Ask the user for this person’s birthday (in the format “YYYY/MM/DD”) - store it in a variable.
#        Now add this new data into your dictionary.
#    Make sure that if the user types any name that exists in the dictionary – including the name that he entered himself – the corresponding birthday is
#  found and displayed.

birthdays = {"Maria": "1992/12/01",
             "Jose": "1984/05/19",
             "Antonio": "2001/08/13",
             "Carlos": "2005/02/23",
             "Monica": "1983/03/17"}


print("Wellcome to the birthdays calendar!")
print("Enter a name to add to the birthday list:")
new_name = (input("Write your name:\n")).title()
new_date = input("Write your birthday (Format: YYYY/MM/DD):\n")
birthdays[new_name] = new_date

print("You can look up the birthdays of the people in the list!")
print(", ".join(birthdays.keys()))
name = input("Write a name:\n")
if name in birthdays:
    birthday = birthdays[name]
    print(f"The birthday of {name} is {birthday}.")
else:
    print(f"Sorry, we don’t have the birthday information for {name}")



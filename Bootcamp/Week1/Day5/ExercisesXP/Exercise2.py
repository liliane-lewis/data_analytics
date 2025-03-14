#!/usr/bin/python3

#Exercise 2 : Cinemax #2
#Instructions

#    A movie theater charges different ticket prices depending on a person’s age.
#        if a person is under the age of 3, the ticket is free.
#        if they are between 3 and 12, the ticket is $10.
#        if they are over the age of 12, the ticket is $15.
#
#    Given the following object:

#    family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


#    How much does each family member have to pay ?
#    Print out the family’s total cost for the movies.
#    Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add 
# them into a family dictionary that is initially empty).


family = {}
print("Write the names and their ages. Write 'quit' to exit\n")

while True:
    name = input("Name: ")
    if name == 'quit':
        break
    age = int(input("Age: "))
    family[name] = age


#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

payment = {}
total = 0
for name, age in family.items():
    print(f"Name: {name}, Age: {age}")
    if age < 3:
        payment[name] = 0
    elif 3 <= age <= 12:
        payment[name] = 10
        total += 10
    else:
        payment[name] = 15
        total += 15

# Print individual payments 
print(payment)
print(f"Total: {total}")
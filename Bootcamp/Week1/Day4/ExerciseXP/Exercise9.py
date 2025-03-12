#!/usr/bin/python3

#Exercise 9: Cinemax
#Instructions

#    A movie theater charges different ticket prices depending on a person’s age.
#        if a person is under the age of 3, the ticket is free.
#        if they are between 3 and 12, the ticket is $10.
#        if they are over the age of 12, the ticket is $15.

#    Ask a family the age of each person who wants a ticket.

#    Store the total cost of all the family’s tickets and print it out.

#    A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#    Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
#    At the end, print the final list.

total = 0

while True:
    age = int(input("Write the person's age? Or write -1 to make the checkout: "))

    if age == -1: 
        break
    elif age < 3: 
        continue  
    elif age < 12:  
        total += 10
    else: 
        total += 15
print(f"Total ticket price for the family: ${total}\n")

print(f"Total: {total}")


teenagers = ["Carol", "Edu", "Lili", "Rick", "Monica", "Katia"]

ages = {}


for teen in teenagers[:]:
    age = int(input(f"Enter age for {teen}: "))

    ages[teen] = age

    if age > 21 or age < 16:
        print(f"{teen} is not allowed to watch this movie!")
        teenagers.remove(teen)

print("Final list of allowed people:")
print(teenagers)
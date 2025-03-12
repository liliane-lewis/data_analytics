#!/usr/bin/python3

#Exercise 8: Who ordered a pizza ?
#Instructions

#    Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#    As they enter each topping, print a message saying you’ll add that topping to their pizza.
#    Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

topping_list = []

while True:
    topping = input("Enter a pizza topping (or type 'quit' to stop):\n")

    if topping == "quit":
        break 

    topping_list.append(topping)
    print(f"Adding {topping} to your pizza!\n")


base_price = 10  
topping_price = 2.5 * len(topping_list)  
total_price = base_price + topping_price

print(f"Total Price: ${total_price}")
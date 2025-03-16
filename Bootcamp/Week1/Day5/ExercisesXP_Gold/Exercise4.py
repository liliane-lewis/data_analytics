#!/usr/bin/python3

#Exercise 4: Fruit Shop
#Instructions

#items = {
#    "banana": 4,
#    "apple": 2,
#    "orange": 1.5,
#    "pear": 3
#}

#    Using the dictionary above, each key-value pair represents an item and its price - print all the items and their prices in a sentence.
#    Using the dictionary below, each value are dictionaries containing both the price and the amount of items in stock -
#    write some code to calculate how much it would cost to buy everything in stock.

#items = {
#    "banana": {"price": 4 , "stock":10},
#    "apple": {"price": 2, "stock":5},
#    "orange": {"price": 1.5 , "stock":24},
#    "pear": {"price": 3 , "stock":1}
#}

# 1.
items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

print("Available items and their prices:")
for fruit, price in items.items():
    print(f"* {fruit.capitalize()}: ${price}")

#2.
items = {
    "banana": {"price": 4 , "stock":10},
    "apple": {"price": 2, "stock":5},
    "orange": {"price": 1.5 , "stock":24},
    "pear": {"price": 3 , "stock":1}
}

total = 0 
for fruit, stock in items.items():
    total += stock["price"] * stock["stock"]

print("Available items and their prices and stocks:")
for fruit, stock in items.items():
    print(f'* {fruit.capitalize()}: ${stock["price"]} - #{stock["stock"]}')

print(f"It would cost {total} to buy everything in stock.")

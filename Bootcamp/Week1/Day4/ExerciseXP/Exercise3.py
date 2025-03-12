#!/usr/bin/python3


#Exercise 3: List
#Instructions
#
#Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

#    Remove “Banana” from the list.
#    Remove “Blueberries” from the list.
#    Add “Kiwi” to the end of the list.
#    Add “Apples” to the beginning of the list.
#    Count how many apples are in the basket.
#    Empty the basket.
#    Print(basket)


basket = ["Banana", "Apples", "Oranges", "Blueberrie"]
print(f"Initial list: {basket}")
basket.remove("Banana")
print(f"After revoving Banana: {basket}")
basket.remove("Blueberrie")
print(f"After revoving Blueberrie: {basket}")
basket.append("Kiwi")
print(f"After adding Kiwi to the end of the list.: {basket}")
basket.insert(0,"Apples")
print(f"After adding Apples to the beginning of the list.: {basket}")
apple_count = basket.count("Apples")
print(f"Number of Apples in the basket: {apple_count}")
basket.clear()
print(f"Empty list: {basket}")


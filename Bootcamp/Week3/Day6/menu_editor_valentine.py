#!/usr/bin/python3

import re

from menu_manager_valentine import MenuManager

def load_manager():
    """this function should create a new MenuManager instance."""
    return MenuManager()

def add_item_to_menu(manager):
    try:
        name = input("Enter item name: ")
        price = float(input("Enter item price: "))
        if validation_valentine(name, price): 
            manager.add_item(name, price)
            print(f"{name} added successfully.")
    except ValueError:
        print("Invalid price. Must be a number.")

def remove_item_from_menu(manager):
    name = input("Enter the item name to remove: ")
    try:
        if manager.remove_item(name):
            print(f"{name} removed successfully.")
        else:
            print(f"{name} not found in the menu.")
    except:
        print("Error.")

def show_restaurant_menu(manager):
    items = manager.display_menu()
    if not items:
        print("The menu is empty.")
    else:
        print("\nRestaurant Menu:")
        for item in items:
            print(f"- {item['name']}: ${item['price']}")

def validation_valentine(name, price):
    
    name_pattern = re.compile(
    r"^V[a-z]*" # Starts with V
    r"(?:\s(?:[A-Z][a-z]*|of|and|the|in|on|at|to|for|with|a|an))*"  # More words, with connection words in lowercase
    r"(?=(?:.*e){2,})"  # two 'e's
    r"$", re.IGNORECASE # Case-insensitive for lookahead
    )

    price_pattern = re.compile(r"^\d{2},14$")
    name_valid = bool(name_pattern.match(name)) and not re.search(r"\d", name)
    price_valid = bool(price_pattern.match(str(price)))
    if name_valid and price_valid:
        return True
    else:
        return False
    
def show_user_menu():

    manager = load_manager()

    while True:
        print("    MENU VALENTINE    ")
        print("(a) Add an item")
        print("(d) Delete an intem")
        print("(v) View the menu")
        print("(x) Exit")

        choice = input("Choose an option: ").strip().lower()


        
        if choice == "a":
            print("    Rules to add a valentine item: ")
            print(" -  Each word in the item name should begin with an uppercase letter and because it's Valentines Day, the first word needs to begin with a "
            "capital \"V\".")
            print(" -  If the name contains connection words, they should begin in lowercase. Example: Vegetable Soup of Valentines-day")
            print(" -  The name of the meal needs to contain at least two \"e\", and no numbers.")
            print(" -  The price needs to match the following pattern: XX.14, where X are numbers.")
            add_item_to_menu(manager)
        
        elif choice == "d":
            remove_item_from_menu(manager)
        
        elif choice == "v":
            show_restaurant_menu(manager)
        
        elif choice == "s":
            manager.save_to_file()
            print("Menu saved successfully.")
        
        elif choice == "x":
            print("End of menu")
            manager.save_to_file()
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    show_user_menu()        
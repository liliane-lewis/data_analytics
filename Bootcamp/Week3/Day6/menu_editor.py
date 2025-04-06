#!/usr/bin/python3

from menu_manager import MenuManager

def load_manager():
    """this function should create a new MenuManager instance."""
    return MenuManager()

def add_item_to_menu(manager):
    name = input("Enter item name: ")
    try:
        price = float(input("Enter item price: "))
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

def show_user_menu():

    manager = load_manager()

    while True:
        print("    MENU")
        print("(a) Add an item")
        print("(d) Delete an intem")
        print("(v) View the menu")
        print("(x) Exit")

        choice = input("Choose an option: ").strip().lower()
        
        if choice == "a":
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
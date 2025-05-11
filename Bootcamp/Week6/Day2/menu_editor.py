#Part 2
#
#    Create a file called menu_editor.py , which will have the following functions:
#        show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to :
#            View an Item (V)
#            Add an Item (A)
#            Delete an Item (D)
#            Update an Item (U)
#            Show the Menu (S)
#            Call the appropriate function that matches the user’s input.
#
#        add_item_to_menu() - this function should ask the user to input the item’s name and price. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
#            If the item was added successfully print a message which states: item was added successfully.
#
#        remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
#            If the item was deleted successfully – print a message to let the user know this was completed.
#            If not – print a message which states that there was an error.
#
#        update_item_from_menu()- this function should ask the user to input the name and price of the item they want to update from the restaurant’s menu, as well as to input the name and price they want to change them with. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
#            If the item was updated successfully – print a message to let the user know this was completed.
#            If not – print a message which states that there was an error.
#
#        show_restaurant_menu() - print the restaurant’s menu.
#
#    When the user chooses to exit the program, display the restaurant menu and exit the program.


import psycopg2
from menu_item import MenuItem
from menu_manager import MenuManager

connection = psycopg2.connect(
    dbname="restaurant_db",
    user="postgres",
    password="P0st2o25",
    host="localhost",
    port="5432"
)
MenuItem.connection = connection  

def show_user_menu():
    '''
    This function should display the program menu (not the restaurant menu!), and ask the user to:
        View an Item (V)
        Add an Item (A)
        Delete an Item (D)
        Update an Item (U)
        Show the Menu (S)
        Call the appropriate function that matches the user’s input.
    '''
    while True:
        choice = input("""
        V - View an Item
        A - Add an Item
        D - Delete an Item
        U - Update an Item
        S - Show the Menu
        X - Exit
        Your choice: 
        """).strip().upper()

        if choice == 'V':
            name = input("Enter item name: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"{item.name}: ${item.price}")
            else:
                print("Item not found.")
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'X':
            print("Final Restaurant Menu:")
            show_restaurant_menu()
            break
        else:
            print("Invalid input. Try again.")

def add_item_to_menu():
    '''
    This function should ask the user to input the item’s name and price. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
    If the item was added successfully print a message which states: item was added successfully.
    '''
    name = input("Item name: ")
    try:
        price = int(input("Item price: "))
        item = MenuItem(name, price)
        item.save()
        print("Item was added successfully.")
    except Exception as e:
        print("Error adding item:", e)

def remove_item_from_menu():
    '''
    This function should ask the user to input the name of the item they want to remove from the restaurant’s menu. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
    If the item was deleted successfully – print a message to let the user know this was completed.
    If not – print a message which states that there was an error
    '''
    name = input("Enter item name to remove: ")
    item = MenuManager.get_by_name(name)
    if item:
        item.delete()
        print("Item was deleted successfully.")
    else:
        print("Error: item not found.")

def update_item_from_menu():
    '''
    This function should ask the user to input the name and price of the item they want to update from the restaurant’s menu, as well as to input the name and price they want to change them with. This function will not interact with the menu itself, but simply create a MenuItem object and call the appropriate function from the MenuItem object.
    If the item was updated successfully – print a message to let the user know this was completed.
    If not – print a message which states that there was an error
    '''
    old_name = input("Current item name: ")
    item = MenuManager.get_by_name(old_name)
    if item:
        new_name = input("New name: ")
        try:
            new_price = int(input("New price: "))
            item.update(new_name, new_price)
            print("Item was updated successfully.")
        except Exception as e:
            print("Error updating item:", e)
    else:
        print("Error: item not found.")

def show_restaurant_menu():
    '''
    print the restaurant’s menu.
    '''
    items = MenuManager.all_items()
    if items:
        print("\n--- Restaurant Menu ---")
        for item in items:
            print(f"{item.name} - ${item.price}")
    else:
        print("The menu is currently empty.")

if __name__ == '__main__':
    show_user_menu()

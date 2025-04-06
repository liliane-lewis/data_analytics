#!/usr/bin/python3

import json

class MenuManager:
    def __init__(self):
        try:
            with open('restaurant_menu.json', 'r') as file:
                data = json.load(file)
                self.menu = data.get("items", [])
        except FileNotFoundError:
            print("The file restaurant_menu.json was not found.")
            self.menu = []
        except json.JSONDecodeError:
            print("Error decoding JSON from restaurant_menu.json.")
            self.menu = []


    def add_item(self, name, price):
        '''This method adds an item to the menu (in memory only, not saved to file yet).'''
        new_item = {
            "name": name,
            "price": price
        }
        self.menu.append(new_item)

    def remove_item(self,name):
        for index, item in enumerate(self.menu):
            if item.get("name") == name:
                del self.menu[index]
                return True
        return False

    def save_to_file(self):
        try:
            with open('restaurant_menu.json', 'w') as file:
                json.dump({"items": self.menu}, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving the menu: {e}")

    def display_menu(self):
        return self.menu

#M = MenuManager()

#print(M.menu)
#
#M.add_item("Pizza", 39.9)
#print(M.menu)

#print(M.remove_item("Hamburger"))  #True
#print(M.remove_item("Pizza"))      #False
#print(M.menu)
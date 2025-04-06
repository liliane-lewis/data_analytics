#!/usr/bin/python3

#Exercise 1 : Restaurant Menu Manager
#Instructions
#
#Description: Create a restaurant menu management system for a manager. The program should allow the manager to view the menu, add an item and delete 
# an item.
#
#The menu should be saved to a local file – the program should load the file when it begins and add the updated details to the file before exiting.
#
#The program should be written in two files – one which will deal with the UI (user interface), eg. showing the user menu and getting user input, etc.
#The second file will handle all other functionality such as adding/removing items from the menu, along with loading and saving the data to a JSON file.
#Separating the files is important – the file which deals with the UI functionality should not have any details about the menu file itself (encapsulation).
#
#The following code is the basic menu for a restaurant. You can make any changes you want.
#
#{
#    "items": [
#        {
#            "name": "Vegetable soup",
#            "price": 30
#        },
#        {
#            "name": "Hamburger",
#            "price": 44.9
#        },
#       {
#            "name": "Milkshake",
#            "price": 22.5
#        },
#        {
#            "name": "Artichoke",
#            "price": 18
#        },
#        {
#            "name": "Beef stew",
#            "price": 52.5
#        }
#    ]
#}
##
#
#    Create a JSON file called restaurant_menu.json. Paste the menu provided above in the restaurant_menu.json file.
#
#    Create a file called menu_manager.py. The file should contain a class called MenuManager, with the following functions:
##        __init__() - The function should read the menu from the restaurant_menu.json file and store it in a variable called menu.
#
#        add_item(name, price) – this method should add an item to the menu, although do not save the changes to the file yet.
#
#        remove_item(name) – if the item is in the menu, this function should remove it from the menu (and again do not save the changes to the file yet) 
# and return True. If the item was not in the menu, return False. (Hint: use Python’s del operator).#
#
#        save_to_file() - When the manager is finished updating the menu this function should be called and it should save all the updates and 
#write them into the the restaurant_menu.json file (ie. the file which holds the menu).
#
#    Create a file called menu_editor.py , which will have the following functions:
#        load_manager()- this function should create a new MenuManager instance.
#
#        show_user_menu() - this function should display the program menu (not the restaurant menu!), and ask the user to choose an item. Call the appropriate function that matches the user’s input.
#
#        add_item_to_menu() - this will ask the user to input the item’s name and price. It will not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
#            If the item was added successfully print a message which states: item was added successfully.
#
#        remove_item_from_menu()- this function should ask the user to input the name of the item they want to remove from the restaurant’s menu. The function should not interact with the menu itself, but simply call the appropriate function from the MenuManager object.
#            If the item was deleted successfully – print a message to let the user know this was completed.
#            If not – print a message which states that there was an error.#
#
#        show_restaurant_menu() - print the restaurant’s menu.
#
#    When the user chooses to exit the program, first write the menu to the file and then print a message that states that the menu was saved, finally exit the program.
#
#    After exiting the program the changes should be reflected in the menu (see Part 1.1) and in the JSON file.
#
#    Here’s an example of the menu shown to the user:




#Exercise 2 : Giphy API #1
#Instruction
#Hint: For this exercise, check out the documentation of the Giphy API


#You will work with this part of the documention
#You will use this Gif URL: https://api.giphy.com/v1/gifs/search?q=hilarious&rating=g&api_key=hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
print("\nExercise 2\n")


API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"


import requests



query = "hilarious"
rating = "g"
limit = 10


url = f"https://api.giphy.com/v1/gifs/search?q={query}&rating={rating}&api_key={API_KEY}&limit={limit}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for i, gif in enumerate(data['data'], 1):
        gif_url = gif['url']
        height = gif['images']['original']['height']
        if int(height) > 100:
            print(f"{i}. URL: {gif_url} (Height: {height})")
else:
    print('Failed to fetch GIFs:', response.status_code)



#Exercise 3 : Giphy API #2

#Instructions
#
#Hint: For this exercise, You will work with this part of the documention
#You will use this API KEY : hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My
#
#    Create a small Python program which asks the user for a term or phrase and returns all the relevant gifs. (Example: all the “hilarious” gifs)
#        If the term or phrase doesn’t exist or if the user didn’t enter a correct term or phrase, return the trending gifs of the day and a message 
# stating that you couldn’t find the requested term or phrase.
#        Note from the documentation : GIPHY Trending returns a list of the most relevant and engaging content each and every day.

print("\nExercise 3\n")

import requests

API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My"
rating = "g"
limit = 10

print("GIF Search")

query_user = input("Type a term or phrase to search for GIFs (Example: hilarious): ").strip()

def search_gifs(query):

    url = f"https://api.giphy.com/v1/gifs/search?q={query}&rating={rating}&api_key={API_KEY}&limit={limit}"

    return requests.get(url)

def get_trending_gifs():
    url = "https://api.giphy.com/v1/gifs/trending/"
    params = {
        'api_key': API_KEY,
        'limit': limit,
        'rating': rating
    }
    return requests.get(url, params=params)

response = search_gifs(query_user)

if response.status_code == 200:
    data = response.json()
    #print(data)
    if not data['data']:
        print("No GIFs found for that term. Showing trending GIFs instead.\n")
        response = get_trending_gifs()
        data = response.json()
    else:
        print(f"Showing GIFs for: {query_user}\n")
else:
    print("Error in search request. Showing trending GIFs instead.\n")
    response = get_trending_gifs()
    data = response.json()

for i, gif in enumerate(data['data'], 1):
    gif_url = gif['url']
    height = gif['images']['original']['height']
    print(f"{i}. URL: {gif_url} (Height: {height})")

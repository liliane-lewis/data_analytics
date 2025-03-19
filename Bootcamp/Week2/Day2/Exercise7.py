#!/usr/bin/python3

#Exercise 7 : Temperature Advice
#Instructions

#    Create a function called get_random_temp().
#        This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
#        Test your function to make sure it generates expected results.
#
#    Create a function called main().
#        Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
#        Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
#
#    Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
#        below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
#        between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
#        between 16 and 23
#        between 24 and 32
#        between 32 and 40
#
#    Change the get_random_temp() function:
#        Add a parameter to the function, named ‘season’.
#        Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is
#        ‘winter’, temperatures should only fall between -10 and 16.
#        Now that we’ve changed get_random_temp(), let’s change the main() function:
#            Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in 
#               a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
#            Use the season as an argument when calling get_random_temp().
#
#    Bonus: Give the temperature as a floating-point number instead of an integer.
#    Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

import random

#def get_random_temp():
#    return(random.randint(-10,40))

def get_random_temp(season):
    if season == "winter":
        return round(random.uniform(-10, 16), 1)
    elif season == "spring":
        return round(random.uniform(5, 22), 1)
    elif season == "summer":
        return round(random.uniform(20, 40), 1)
    elif season == "autumn" or season == "fall":
        return round(random.uniform(5, 25), 1)
    else:
        raise ValueError("Invalid season. Please enter winter, spring, summer, or autumn.")

def get_season_by_mounth(mounth):
    if mounth in [1, 2, 12]:
        print("It is winter!")
        return "winter"
    elif mounth in [3, 4, 5]:
        print("It is winter!")
        return "spring"
    elif mounth in [6, 7, 8]:
        return "summer"
    elif mounth in [9, 10, 11]:
        return "autumn"

def main():
    #temp = get_random_temp("winter")
    #temp = get_random_temp("spring")
    #temp = get_random_temp("summer")
    #season = input("Enter a season: (winter, spring, summer, or autumn (or fall).)\n")
    #temp = get_random_temp("fall")
    mounth = int(input("Enter a mouth (1-12):\n"))
    season = get_season_by_mounth(mounth)
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= temp <= 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 < temp <= 23:
        print("It is cool!")
    elif 24 <= temp <= 32:
        print("It is perfect!!")
    elif 33 <= temp <= 40:
        print("It is too hot!!!")


main()
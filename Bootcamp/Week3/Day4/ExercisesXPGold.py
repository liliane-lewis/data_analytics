#!/usr/bin/python3

#Exercise 1 : Upcoming Holiday
#Instructions
#
#    Write a function that displays today’s date.
#    The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is. 
#    (Example: the next holiday is New Years’ Eve in 30 days).
#    Hint: Use a module to find the datetime and name of the upcoming holiday.


from datetime import datetime, date


jewish_holidays_2025 = {
    "Purim": date(2025, 3, 14),
    "Passover (1st day)": date(2025, 4, 13),
    "Shavuot": date(2025, 6, 2),
    "Rosh Hashanah": date(2025, 10, 2),
    "Yom Kippur": date(2025, 10, 11),
    "Sukkot (1st day)": date(2025, 10, 16),
    "Simchat Torah": date(2025, 10, 23),
    "Hanukkah (1st day)": date(2025, 12, 22),
}

def next_jewish_holiday():
    today = date.today()
    print(f"Today is: {today.strftime('%A, %B %d, %Y')}")

    future_holidays = {name: d for name, d in jewish_holidays_2025.items() if d > today}
    #print(future_holidays)

    if not future_holidays:
        print("No upcoming Jewish holidays found for this year.")
        return

    next_holiday_name = min(future_holidays, key=future_holidays.get)
    next_holiday_date = future_holidays[next_holiday_name]
    days_left = (next_holiday_date - today).days

    print(f"The next Jewish holiday is {next_holiday_name} in {days_left} day(s), on {next_holiday_date.strftime('%A, %B %d, %Y')}.")

next_jewish_holiday()



#Exercise 2 : How Old Are You On Jupiter?
#Instructions
#
#    Given an age in seconds, calculate how old someone would be on all those planets :
#        Earth: orbital period 365.25 Earth days, or 31557600 seconds
#            Example : if someone is 1,000,000,000 seconds old, the function should output that they are 31.69 Earth-years old.
#        Mercury: orbital period 0.2408467 Earth years
#        Venus: orbital period 0.61519726 Earth years
#        Mars: orbital period 1.8808158 Earth years
#        Jupiter: orbital period 11.862615 Earth years
#        Saturn: orbital period 29.447498 Earth years
#        Uranus: orbital period 84.016846 Earth years
#        Neptune: orbital period 164.79132 Earth years






from datetime import datetime, timedelta

orbital_period = {
    "Mercury": 0.2408467,
    "Venus": 0.61519726,
    "Earth": 1,
    "Mars": 1.8808158,
    "Jupiter": 11.862615,
    "Saturn": 29.447498,
    "Uranus": 84.016846,
    "Neptune": 164.79132,
}

EARTH_DAYS = 365.25
EARTH_YEAR_SECONDS = 31557600  # seconds in one Earth year

def age_in_seconds(age):

    now = datetime.now()
    birthdate = now - timedelta(days=age * EARTH_DAYS)
    age_seconds = int((now - birthdate).total_seconds())
    return age_seconds


def age_plannet(age, planet):
    age_s = age_in_seconds(age)
    orbit = orbital_period[planet]
    age_on_planet = age_s / (EARTH_YEAR_SECONDS * orbit)
    print(f"At age {age} in Earth, you are {age_on_planet:.2f} {planet}-years old.")


age_plannet(42,"Earth")
age_plannet(42,"Mercury")
age_plannet(42,"Venus")
age_plannet(42,"Mars")
age_plannet(42,"Jupiter")
age_plannet(42,"Saturn")
age_plannet(42,"Uranus")
age_plannet(42,"Neptune")


#Exercise 3 : Regular Expression #1
#Instructions

#Hint: Use the RegEx (module)
#
#    Use the regular expression module to extract numbers from a string.
#
#    Example
#
#    return_numbers('k5k3q2g5z6x9bn') 
#   // Excepted output : 532569

import re

def return_numbers(st):
    numbers = re.findall(r'\d', st)
    print("".join(numbers))

return_numbers('k5k3q2g5z6x9bn') 


#Exercise 4 : Regular Expression #2
#Instructions
#
#Hint: Use the RegEx (module)
#
#    Ask the user for their full name (example: “John Doe”), and check the validity of their answer:
#        The name should contain only letters.
#        The name should contain only one space.
#        The first letter of each name should be upper cased.

def check_nane(name):
    #numbers = re.findall(r'\d', name)
    #spaces = re.findall(r'\s', name)
    #first_letter_name = re.findall(r'[A-Z]', name[0])
    #first_letter_surnamename = re.findall(r'[A-Z]', (name.split(" "))[1])
    #if not numbers and len(spaces) == 1 and first_letter_name and first_letter_surnamename:
    #    return True
    #else:
    #    return False
    pattern = r'^[A-Z][a-z]+ [A-Z][a-z]+$'
    return bool(re.fullmatch(pattern, name))

user_name = input("Write your full name. \nRules: "
"\nThe name should contain only letters."
"\nThe name should contain only one space."
"\nThe first letter of each name should be upper cased\n")
if check_nane(user_name):
    print("Full name OK")
else:
    print("Full name not OK")


#Exercise 5: Python Password Generator
#Instructions
#
#Create a Python program that will generate a good password for you.#
#
#Program flow:
#
#    Ask the user to type in the number of characters that the password should have (password length) – between 6 and 30 characters.
#        Validate the input. Make sure the user is inputing a number between 6 to 30. Create a loop which will continue to ask the user for an input until
#  they enter a valid one.
#
#    Generate a password with the required length.
#
#    Print the password with a user-friendly message which reminds the user to keep the password in a safe place!
#
#Rules for the validity of the password
#
#    Each password should contain:
#        At least 1 digit (0-9)
#        At least 1 lower-case character (a-z)
#        At least 1 upper-case character (A-Z)
#        At least 1 special character (eg. !, @, #, $, %, ^, _, …)
#        Once there is at least 1 of each, the rest of the password should be composed of more characters from the options presented above.
#
#    Create a test function first!
#
#    Do the following steps 100 times, with different password lengths:
#        Generate a password.
#        Test the password to ensure that:
#            it fulfills all the requirements above (eg. it has at least one digit, etc.)
#            it has the specified length.

import random
import string
import re

def test(password):
    digit = re.search(r'\d', password)
    lower_case = re.search(r'[a-z]', password)
    upper_case = re.search(r'[A-Z]', password)
    special = re.search(r'[!@#$%^&*()_+\-=\[\]{};:"\\|,.<>\/?]', password)
    return bool(digit and lower_case and upper_case and special)

def generate_password(password_length):

    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{};:,.<>/?"
    while True:
        password = ''.join(random.choice(chars) for _ in range(password_length))
        if test(password):
            return password
        
password_length = 0
def main():
    while True:
        password_length = int(input("Enter the password length\n"))
        if password_length >= 6 and password_length <= 30:
            break 
        else:
            print("Please enter a number between 6 and 30.")

#main()
for _ in range(100):
    length = random.randint(6, 30)
    pwd = generate_password(length)
    if test(pwd):
        print(pwd)
        continue
    else:
        break
print("All 100 passwords passed the tests.")


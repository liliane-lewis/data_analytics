#!/usr/bin/python3


#Exercise 1: Currencies
#Instructions
#
#class Currency:
#    def __init__(self, currency, amount):
#        self.currency = currency
#        self.amount = amount

    #Your code starts HERE


#   1. Using the code above, implement the relevant methods and dunder methods which will output the results below.
#    Hint : When adding 2 currencies which don’t share the same label you should raise an error.
#>>> c1 = Currency('dollar', 5)
#>>> c2 = Currency('dollar', 10)
#>>> c3 = Currency('shekel', 1)
#>>> c4 = Currency('shekel', 10)

#>>> str(c1)
#'5 dollars'

#>>> int(c1)
#5

#>>> repr(c1)
#'5 dollars'

#>>> c1 + 5
#10

#>>> c1 + c2
#15

#>>> c1 
#5 dollars

#>>> c1 += 5
#>>> c1
#10 dollars

#>>> c1 += c2
#>>> c1
#20 dollars

#>>> c1 + c3
#TypeError: Cannot add between Currency type <dollar> and <shekel>


class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        if self.amount == 1:
            return f"{self.amount} {self.currency}"
        else:
            return f"{self.amount} {self.currency}s"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        elif isinstance(other, int):
            return self.amount + other
        else:
            return 1

    def __iadd__(self, other):
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        elif isinstance(other, int):
            self.amount += other
        else:
            return NotImplemented
        return self
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

try:

    print(str(c1))      # '5 dollars'
    print(int(c1))      # 5
    print(repr(c1))     # '5 dollars'

    print(c1 + 5)       # 10
    print(c1 + c2)      # 15

    print(c1)           # 5 dollars

    c1 += 5
    print(c1)           # 10 dollars

    c1 += c2
    print(c1)           # 20 dollars

    print(c1 + c3)      # TypeError

except TypeError as e:
    print(e)


#Exercise 3: String module
#Instructions

#    Generate random String of length 5
#    Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
#    Hint: use the string module


import random
import string

letters = string.ascii_letters
#letters = "ABCDEFGHIJKLMNOPRSTUVXWYZabcdefghijklmnopqrstuvxyz"
# Generate a random string of length 5
string_5 = ''.join(random.choice(letters) for _ in range(5))
print(string_5)


#Exercise 4 : Current Date
#Instructions

#    Create a function that displays the current date.
#    Hint : Use the datetime module.


import datetime

def current_data():
    today = datetime.date.today()
    print("Day:", today.day)
    print("Month:", today.month)
    print("Year:", today.year)


current_data()

#Exercise 5 : Amount of time left until January 1st
#Instructions

#    Create a function that displays the amount of time left from now until January 1st.
#    (Example: the 1st of January is in 10 days and 10:34:01hours).

from datetime import datetime

def time_until_january_first():
    now = datetime.now()
    jan_first = datetime(year=now.year + 1, month=1, day=1)
    time_left = jan_first - now
    print(f"Time left until January 1st: {time_left}")


time_until_january_first()


#Exercise 6 : Birthday and minutes
#Instructions
#
#    Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes 
# the user lived in his life.'


def minutes_of_life(day, month, year):
    now = datetime.now()
    birthday = datetime(year=year, month=month, day=day)
    lived = now - birthday
    minutes = int(lived.total_seconds() // 60)
    print(f"You have lived approximately {minutes:,} minutes so far.")

day, month, year = input("Enter your birth date (DD/MM/AAAA): ").strip().split("/")
minutes_of_life(int(day), int(month), int(year))



#Exercise 7 : Faker Module
#Instructions

#    Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
#    Create an empty list called users. Tip: It should be a list of dictionaries.
#    Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to 
# populate them with fake data.


# documentation:
#from faker import Faker
#fake = Faker()
#
#fake.name()
# 'Lucy Cechtelar'
#
#fake.address()

import faker
fake = faker.Faker()
users = []

name_list = [{'name': "", 
              'address': "", 
              'language_code': ""
              }]

def add_fake_users():
    for _ in range(10):
        user = {
            'name': fake.name(),
            'address': fake.address(),
            'language_code': fake.language_code()
        }
        users.append(user)


add_fake_users()

for user in users:
    print(user)
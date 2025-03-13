#!/usr/bin/python3

#Instructions
#
#    Ask the user for their data (specify the format, for example: DD/MM/YYYY).
#    Display a little cake as seen below:
#
#       ___iiiii___
#      |:H:a:p:p:y:|
#    __|___________|__
#   |^^^^^^^^^^^^^^^^^|
#   |:B:i:r:t:h:d:a:y:|
#   |                 |
#   ~~~~~~~~~~~~~~~~~~~

#The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.
#
#Bonus : If they were born on a leap year, display two cakes !


data = input("Write your birthday: DD/MM/YYYY\n")
day, mount, year = data.split("/")
year = int(year)
age = 2025 - year
candles = age % 10

# https://www.programiz.com/python-programming/examples/leap-year
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

candles_str = "i" * candles
cake = f"""
       ___{candles_str}___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

if is_leap:
    print("You were born in a leap year! Here's two cakes!\n")
    print(cake * 2)
else:
    print("Happy Birthday! Here is you cake. Enjoy!\n")
    print(cake)


#!/usr/bin/python3
#Exercise 1 : When will I retire ?
#Instructions

#The point of the exercise is to check if a person can retire depending on their age and their gender.
#Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).
#
#    Create a function get_age(year, month, day)
#    Hard-code the current year and month in your code (there are better ways of doing this, but for now it will be enough.)
#    After calculating the age of a person, the function should return the age (the age is an integer).
#    Create a function can_retire(gender, date_of_birth).
#    It should call the get_age function (with what arguments?) in order to receive an age.
#    Now it has all the information it needs in order to determine if the person with the given gender and date of birth is able to retire or not.
#    Calculate. You may need to do a little more hard-coding here.
#    Return True if the person can retire, and False if he/she can’t.
#
#Some Hints
#
#    Ask for the user’s gender as “m” or “f”.
#    Ask for the user’s date of birth in the form of “yyyy/mm/dd”, eg. “1993/09/21”.
#    Call can_retire to get a definite value for whether the person can or can’t retire.
#    Display a message informing the user whether they can retire or not.
#    As always, test your code to ensure it works.

current_year = 2025 
current_month = 3
#Note : Let’s say retirement age is 67 for men, and 62 for women (born after April, 1947).
RETIREMENT_MAN = 67
RETIREMENT_WOMAN = 63

def get_age(year, month, day):
    current_year = 2025 
    current_month = 3
    current_day = 20
    age =  current_year - year
    if month == current_month:
        if day > current_day:
            age -= 1
    if month > current_month:
            age -= 1
    return age

def can_retire(gender, date_of_birth):
    year, month, day = map(int, date_of_birth.split("/"))
    age = get_age(year, month, day)
    print(f"Your age is: {age}")
    if gender == "M" and age >= RETIREMENT_MAN or gender == "W" and age >= RETIREMENT_WOMAN:
        print("You can retire. Enjoy!")
        return True
    else:
        print("Sorry, you cannot retire yet!")
        return False



sex = input("Enter your sex: M or W\n")
date = input("Enter your birthday: YYYY/MM/DD\n")
can_retire(sex,date)
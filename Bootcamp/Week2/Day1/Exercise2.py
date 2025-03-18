#!/usr/bin/python3

#Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters'

def say_hello(name):
    return(print(f"Hello, {name}!"))
people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]


filtered_names = filter(lambda s: len(s) <= 4, people)


greetings = map(say_hello, filtered_names)

print(list(greetings))


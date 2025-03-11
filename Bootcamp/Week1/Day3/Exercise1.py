#!/usr/bin/python3


# Accept a number from the user and print its multiplication table


number = int(input("Type a number\n"))

for mul in range(1,11):
    print(f"{number} * {mul} = {mul * number}\n")

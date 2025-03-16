#!/usr/bin/python3
#Exercise 1 : Cars
#Instructions
#
#    Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
#    Convert it into a list using Python (don’t do it by hand!).
#    Print out a message saying how many manufacturers/companies are in the list.
#    Print the list of manufacturers in reverse/descending order (Z-A).
#    Using loops or list comprehension:
#        Find out how many manufacturers’ names have the letter ‘o’ in them.
#        Find out how many manufacturers’ names do not have the letter ‘i’ in them.
#
#    Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
#        Remove these programmatically. (Hint: you can use set to help you).
#        Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), 
# also print out a message saying how many companies are now in the list.#
#
#    Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

string_manufacturers = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet, Toyota"
manufacturers = list(set([m.strip() for m in string_manufacturers.split(",")]))

print(type(manufacturers))
print(f"List of manufacturers: {manufacturers}\n")
print(f"There are {len(manufacturers)} in the list.")

manufacturers_sorted = sorted(manufacturers, reverse=True)
print(f"The manufacturers sorted in reverse: {manufacturers_sorted}")

count_o = 0
count_not_i = 0
for manufacturer in manufacturers:
    if "o" in manufacturer:
        count_o += 1
    if not "i" in manufacturer:
        count_not_i += 1
print(f'There are {count_o} names have the letter "o" in them.')
print(f'There are {count_not_i} names do not have the letter "i" in them.')

manufacturers_string = ", ".join(manufacturers)
print(f'Manufacturers: {manufacturers_string} ')
print(f'There are {len(manufacturers)} in the list')

manufacturers_sorted = sorted(manufacturers, reverse=True)
manufacturers_reversed = sorted([m[::-1] for m in manufacturers])
print(f'List sorted reversed: {manufacturers_reversed}')
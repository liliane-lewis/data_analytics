#!/usr/bin/python3

#Exercise 3: Zara
#Instructions

# 1.   Here is some information about a brand.

#    name: Zara 
#    creation_date: 1975 
#    creator_name: Amancio Ortega Gaona 
#    type_of_clothes: men, women, children, home 
#    international_competitors: Gap, H&M, Benetton 
#    number_stores: 7000 
#    major_color: 
#        France: blue, 
#        Spain: red, 
#        US: pink, green



#    2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
#    The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
#    3. Change the number of stores to 2.
#    4. Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.
#    5. Add a key called country_creation with a value of Spain.
#    6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
#    7. Delete the information about the date of creation.
#    8. Print the last international competitor.
#    9. Print the major clothes colors in the US.
#    10. Print the amount of key value pairs (ie. length of the dictionary).
#    11. Print the keys of the dictionary.
#    12. Create another dictionary called more_on_zara with the following details:

#    creation_date: 1975 
#    number_stores: 10 000



 #   13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
 #   14. Print the value of the key number_stores. What just happened ?


#2 Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
#    The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.
brand = {"name": "Zara",
         "creation_date": 1975,
        "creator_name": "Amancio Ortega Gaona",
        "type_of_clothes": ["men", "women", "children", "home"], 
        "international_competitors": ["Gap", "H&M", "Benetton"],
        "number_stores": 7000, 
        "major_color": { "France": ["blue"],
                          "Spain": ["red"], 
                          "US": ["pink", "green"]
                        }
        }

print("\ninitial Dictionary:")
for key, value in brand.items():
    print(key, ":", value)
#3  Change the number of stores to 2.

brand["number_stores"] = 2
print(f"\nAfter change the store number:")
for key, value in brand.items():
    print(key, ":", value)
   

#4  Use the key [type_of_clothes] to print a sentence that explains who Zaras clients are.
print("\nThe Zaras clients are:")
print(", ".join(brand["type_of_clothes"]))

#5 Add a key called country_creation with a value of Spain.
brand["country_creation"] = "Spain"
print("\nAfter adding country_creation:")
for key, value in brand.items():
    print(key, ":", value)

#6  Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

if "international_competitors" in brand.keys():
    brand["international_competitors"].append("Desigual")

print("\nAfter adding Desigual:")
for key, value in brand.items():
    print(key, ":", value) 


#7. Delete the information about the date of creation.

del brand["creation_date"]

print("\nAfter deleting creation_date:")
for key, value in brand.items():
    print(key, ":", value)

# 8. Print the last international competitor.
brand["international_competitors"].pop()
print("\nAfter deleting the last international competitor:")
for key, value in brand.items():
    print(key, ":", value)

#9. Print the major clothes colors in the US.
for country, colors in brand["major_color"].items():
    if country == "US":
        print(f"US Colors: ",", ".join(colors))

#10.  Print the amount of key value pairs (ie. length of the dictionary).

print(f"\nThe dictionary has {len(brand)} pairs")

#11.  Print the keys of the dictionary.

print("\nKeys of the dictionary:")
for key in brand.keys():
    print(key)
#or print(brand.keys())

#12 Create another dictionary called more_on_zara with the following details:

more_on_zara = {"creation_date" : 1975,
                "number_stores": 10000
}

#13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.

def add_to_dictionary(dictionary,item):
    dictionary.update(item)

add_to_dictionary(brand,more_on_zara)
print("\nAfter adding new information:")
for key, value in brand.items():
    print(key, ":", value)

#14. Print the value of the key number_stores. What just happened ?
print(brand["number_stores"])

#the original value (2) was replaced by the new one (10000).
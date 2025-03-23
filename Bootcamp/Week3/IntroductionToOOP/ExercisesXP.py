#!/usr/bin/python3
#Exercise 1: Cats
#Instructions
#
#Using this class
#
#class Cat:
#    def __init__(self, cat_name, cat_age):
#        self.name = cat_name
#        self.age = cat_age
#
#    Instantiate three Cat objects using the code provided above.
#    Outside of the class, create a function that finds the oldest cat and returns the cat.
#    Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest(cat_lst):
    oldest = None
    age = -1 
    for c in cat_lst:
        if c.age > age:
           oldest = c
           age = c.age 

    return oldest

cat1 = Cat("Mingal",7)
cat2 = Cat("Mimi",3)
cat3 = Cat("Spock",2)

cats = [cat1,cat2,cat3]
c = find_oldest([cat1,cat2,cat3])

print("\n**********************\nExercise 1\n**********************\n")
print(f"The oldest cat is {c.name} and is {c.age} years old.")


#Exercise 2 : Dogs
#Instructions
#
#    Create a class called Dog.
#    In this class, create an __init__ method that takes two parameters : name and height. This function instantiates 
#    two attributes, which values are the parameters.
#    Create a method called bark that prints the following string “<dog_name> goes woof!”.
#    Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
#    Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
#    Print the details of his dog (ie. name and height) and call the methods bark and jump.
#    Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
#    Print the details of her dog (ie. name and height) and call the methods bark and jump.
#    Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

class Dog:
    def __init__(self, dog_name, dog_height):
        self.name = dog_name
        self.height = dog_height
    def bark(self):
        print(f"{self.name} goes woof!")
    def jump(self):
        print(f"{self.name} jumps {2 * self.height} cm high!")

davids_dog = Dog("Rex",50)
print(f"Davids dog is {davids_dog.name} and he is {davids_dog.height} high")
davids_dog.bark()
davids_dog.jump()
sarahs_dog = Dog("Teacup",20)
print(f"Sarahs dog is {sarahs_dog.name} and he is {sarahs_dog.height} high")
sarahs_dog.bark()
sarahs_dog.jump()

dogs_list = [davids_dog,sarahs_dog]
def find_bigger(dogs_list):
    bigger = ""
    height = -1 
    for d in dogs_list  :
        if d.height > height:
           height = d.height
           bigger = d.name

    return bigger

d = find_bigger(dogs_list)

print("\n**********************\nExercise 2\n**********************\n")
print(f"The bigger dog is {d}")



#Exercise 3 : Who’s the song producer?
#Instructions

#1. Define a class called Song, it will show the lyrics of a song.
#Its __init__() method should have two arguments: self and lyrics (a list).
#2. Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
#3. Create an object, for example:
#
#stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])#
#
#
#4. Then, call the sing_me_a_song method. The output should be:
#
#There’s a lady who's sure
#
#all that glitters is gold
#
#and she’s buying a stairway to heaven


class Song:
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for l in self.lyrics:
            print(l)


stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])

print("\n**********************\nExercise 3\n**********************\n")
stairway.sing_me_a_song()



#Exercise 4 : Afternoon at the Zoo
#Instructions
#
#    Create a class called Zoo.
#    In this class create a method __init__ that takes one parameter: zoo_name.
#    It instantiates two attributes: animals (an empty list) and name (name of the zoo).
#    Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to 
# the animals list as long as it isn’t already in the list.
#    Create a method called get_animals that prints all the animals of the zoo.
#    Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal 
# from the list and of course the animal needs to exist in the list.#

#    Create a method called sort_animals that sorts the animals alphabetically and groups them together based on 
# their first letter.
#    Example

#    { 
#        A: "Ape",
#        B: ["Baboon", "Bear"],
#       C: ['Cat', 'Cougar'],
#        E: ['Eel', 'Emu']
#    }
#
#
#    Create a method called get_groups that prints the animal/animals inside each group.
#    Create an object called new_york_zoo and call all the methods.
#    Tip: The zookeeper is the one who will use this class.
#    Example
#
#    Which animal should we add to the zoo --> Giraffe
#    x.add_animal(Giraffe)
class Zoo:
    def __init__(self, zoo_name):
        self.name = zoo_name
        self.animals = []

    def add_animal(self,new_animal):
        if new_animal not in self.animals:
            self.animals.append(new_animal)

    def get_animals(self):
        print("Animals in the zoo:")
        for animal in self.animals:
            print(animal)

    def sell_animal(self,animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)

    def sort_animals(self):

        self.animals.sort()
        sorted_animals = {}

        for animal in self.animals:
            first_letter = animal[0].upper()
            if first_letter in sorted_animals:
                sorted_animals[first_letter].append(animal)
            else:
                sorted_animals[first_letter] = [animal]

        return sorted_animals
    
    def get_groups(self):
        
        sorted_groups = self.sort_animals()
        print("Grouped animals:")
        for letter, animals in sorted_groups.items():
            print(f"{letter}: {animals}")
    
animals = ["zebra","lion","elephant"]

#    Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to 


new_york_zoo = Zoo("NY Zoo")

new_york_zoo.add_animal("Zebra")
new_york_zoo.add_animal("Lion")
new_york_zoo.add_animal("Elephant")
new_york_zoo.add_animal("Bear")
new_york_zoo.add_animal("Baboon")
new_york_zoo.add_animal("Cougar")
new_york_zoo.add_animal("Emu")
new_york_zoo.add_animal("Eel")


print("\n**********************\nExercise 4\n**********************\n")


new_york_zoo.get_groups()
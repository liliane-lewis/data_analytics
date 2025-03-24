#!/usr/bin/python3
# #Exercise 3 : Dogs Domesticated
#Instructions

#    Create a new python file and import your Dog class from the previous exercise.
#    In the new python file, create a class named PetDog that inherits from Dog.
#    Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False
#    by default.
#    Add the following methods:
#        train: prints the output of bark and switches the trained boolean to True
#
#        play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print
#    the following string: “dog_names all play together”.
#
#        do_a_trick: If the dog is trained the method should print one of the following sentences at random:
#            “dog_name does a barrel roll”.
#            “dog_name stands on his back legs”.
#            “dog_name shakes your hand”.
#            “dog_name plays dead”.

from ExercisesXP import Dog
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)  
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True
    
    def play(self,*args):
        dog_names = ", ".join(args)
        print(f"{dog_names} all play together.")     

    def do_a_trick(self):

        trick = ["does a barrel roll.", "stands on his back legs.", "dog_name shakes your hand.", "dog_name plays dead."]

        if (self.trained):
            random_trick = random.choice(trick)
            print(f"{self.name} {random_trick}")
        else:
            print(f"{self.name} is not trained yet and doesn't do a trick.")

dog1 = PetDog("Arnaldo", 1, 5)
dog2 = PetDog("Doguinho", 3, 20)

dog1.train()

dog1.do_a_trick()
dog2.do_a_trick()

dog1.play("Doguinho", "Rex", "Luna")


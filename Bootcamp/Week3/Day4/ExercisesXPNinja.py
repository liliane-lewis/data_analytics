#!/usr/bin/python3

#Exercise 1 : Temperature
#Instructions
#
#    Write a base class called Temperature.
#        Implement the following subclasses: Celsius, Kelvin, Fahrenheit.
#        Each of the subclasses should have a method which can convert the temperture to another type.
#        You must consider different designs and pick the best one according to the SOLID Principle.

class Temperature:
    def __init__(self, value):
        self.value = value

    def to_celsius(self):
        raise NotImplementedError

    def to_fahrenheit(self):
        raise NotImplementedError

    def to_kelvin(self):
        raise NotImplementedError


class Celsius(Temperature):
    def to_fahrenheit(self):
        return (self.value * 9/5) + 32

    def to_kelvin(self):
        return self.value + 273.15

    def to_celsius(self):
        return self.value


class Fahrenheit(Temperature):
    def to_celsius(self):
        return (self.value - 32) * 5/9

    def to_kelvin(self):
        return (self.value - 32) * 5/9 + 273.15

    def to_fahrenheit(self):
        return self.value


class Kelvin(Temperature):
    def to_celsius(self):
        return self.value - 273.15

    def to_fahrenheit(self):
        return (self.value - 273.15) * 9/5 + 32

    def to_kelvin(self):
        return self.value

temp = Fahrenheit(-40)
print(f"-40F in Celsius: {temp.to_celsius()}°C")
print(f"-40F in Kelvin: {temp.to_kelvin()}K")


#Exercise 2: In the Quantum Realm
#Instructions
#
#    Write a class called QuantumParticle and implement the following:
#        The attributes - The particle has an initial position (x), momentum (y) and spin (p)
#
#        The method position() - Position measurement: generate a random position (integer between 1 and 10,000)
#
#        The method momentum() - Momentum measurement: generate a random momentum (float - a number between 0 and 1)
#
#        The method spin() - Spin measurement: can randomly be 1/2 or -1/2
#
#        Create a method that implements a disturbance. A disturbance occurs each time a measurement is made (e.g. one of the measurements method 
# is called). Disturbance changes the position and the momentum of the particle (randomly generated) and then prints ‘Quantum Interferences!!’
#
#        Implement a meaningful representation of the particle (repr)
#
#    Quantum Entanglement: two particle can be entangled, meaning that if I measure the spin of one of them the second one is automatically set to 
# the opposite value. A quantum particle can only be entangled to another quantum particle (check that when you run the method !!)
#        Modify as you see fit the attributes and methods of your class to fit the previous definition
#        When two particles are entangled print: ‘Spooky Action at a Distance !!’
#
#>>>p1 = QuantumParticle(x=1,p=5.0)
#>>>p2 = QuantumParticle(x=2,p=5.0)
#>>>p1.entangle(p2)
#>>>'Particle p1 is now in quantum entanglement with Particle p2'
#
#>>>p1 = QuantumParticle()
#>>>p2 = QuantumParticle()
#>>>p1.entangle(p2)
#>>>'Spooky Action at a Distance'

import random

class QuantumParticle:
    def __init__(self, x=None, y=None, s=None):
        self.x = x if x is not None else random.randint(1, 10000)
        self.y = y if y is not None else random.uniform(0, 1)
        self.s = s if s is not None else random.choice([0.5, -0.5])
        self.entangled_particle = None

    def __repr__(self):
        return f"QuantumParticle(position={self.x}, momentum={self.y:.4f}, spin={self.s})"

    def position(self):
        self.disturbance()
        return self.x

    def momentum(self):
        self.disturbance()
        return self.y

    def spin(self):
        self.disturbance()
        return self.s

    def disturbance(self):
        self.x = random.randint(1, 10000)
        self.y = random.uniform(0, 1)
        print("Quantum Interferences!!")

    def entangle(self, other):
        if not isinstance(other, QuantumParticle):
            raise ValueError("Can only entangle with another QuantumParticle")

        self.entangled_particle = other
        other.entangled_particle = self

        other.s = -self.s

        print("Spooky Action at a Distance !!")
        print(f"Particle {id(self)} is now in quantum entanglement with Particle {id(other)}")


p1 = QuantumParticle(x=1, y=0.5, s=0.5)
p2 = QuantumParticle(x=2, y=0.5, s=-0.5)

p1.entangle(p2)
print(p1)
print(p2)

print(p1.position())
print(p1.momentum())
print(p1.spin())
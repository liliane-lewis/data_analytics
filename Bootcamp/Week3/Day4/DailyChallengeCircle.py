#!/usr/bin/python3

#Instructions :
#
#The goal is to create a class that represents a simple circle.
#A Circle can be defined by either specifying the radius or the diameter.
#The user can query the circle for either its radius or diameter.
#
#Other abilities of a Circle instance:
#
#    Compute the circle’s area
#    Print the attributes of the circle - use a dunder method
#    Be able to add two circles together, and return a new circle with the new radius - use a dunder method
#    Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
#    Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
#    Be able to put them in a list and sort them
#    Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

PI = 3.14

class Circle:
    def __init__(self, radius=None, diameter=None):
        if radius is not None:
            self.radius = radius
        elif diameter is not None:
            self.radius = diameter / 2
        else:
            raise ValueError("Must enter the radius or the diameter")
        
    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return PI * self.radius ** 2

    def __repr__(self):
        return f"Circle(radius={self.radius})"
    
    def __add__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return Circle(radius=self.radius + other.radius)

    def __gt__(self, other):
        if not isinstance(other, Circle):
            return NotImplemented
        return self.radius > other.radius

    def __eq__(self, other):
        if not isinstance(other, Circle):
            return False
        return self.radius == other.radius
    
    def add_list(self,other_circle):
        circle_list = []
        return list(set(circle_list.append(other_circle)))

        
c1 = Circle(radius=3)
c2 = Circle(diameter=10)

print(c1)                      # Circle(radius=3)
print(c2.diameter)             # 10.0
print(c1.area())               # 28.26
print(c1 > c2)                 # False
print(c1 == c2)                # False

c3 = c1 + c2
print(c3)                      # Circle(radius=8.0)


circles = [c1, c2, c3]
circles.sort()
print(circles)     

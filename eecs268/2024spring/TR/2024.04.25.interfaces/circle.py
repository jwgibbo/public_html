#circle.py

from shape import Shape
from math import pi

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi*self.radius**2

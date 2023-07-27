#circle.py

from shape import Shape
import math

class Circle(Shape):
    def __init__(self):
        self.radius = 0

    def area(self):
        return math.pi*self.radius**2

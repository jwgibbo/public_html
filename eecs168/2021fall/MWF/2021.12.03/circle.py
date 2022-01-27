#circle.py
from math import pi

class Circle:
    def __init__(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            self._radius = 0

    def __lt__(self, other):
        return self._radius < other._radius

    def __str__(self):
        output = "Circle info:\n"
        output += f'Radius: {self._radius}\n'
        output += f'Area: {self.area()}\n'
        return output

    def __repr__(self):
        output = f'Circle({self._radius})'
        return output
        
    def area(self):
        return pi*self._radius**2

    def set_radius(self, radius):
        if radius > 0:
            self._radius = radius
            return True
        else:
            return False

    def get_radius(self):
        return self._radius



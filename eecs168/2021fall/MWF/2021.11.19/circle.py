#circle.py
from math import pi

class Circle:
    def __init__(self):
        self._radius = 0

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



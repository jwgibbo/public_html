#circle.py
import math

class Circle:
    def __init__(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            self._radius = 0
        #Notice no return statement

    def area(self):
        ans = math.pi*self._radius**2
        return ans

    def set_radius(self, r):
        if r > 0:
            self._radius = r
        else:
            self._radius = 0

    def get_radius(self):
        return self._radius

    def __lt__(self, other):
        if self._radius < other._radius:
            return True
        else:
            return False

    def __eq__(self, other):
        if self._radius == other._radius:
            return True
        else:
            return False

    def __le__(self, other):
        if self < other or self == other:
            return True
        else:
            return False
        
    def __ge__(self, other):
        return not(self < other)

    def __str__(self):
        output = f'Circle<radius={self._radius}>'
        return output

    def __repr__(self):
        output = f'Circle({self._radius})'
        return output

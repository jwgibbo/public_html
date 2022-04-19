#circle.py
import math

class Circle:
    def __init__(self):
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

    def __gt__(self, other):
        if self._radius > other._radius:
            return True
        else:
            return False

    def __str__(self):
        #Build and return a string
        output = f'radius: {self._radius}, area: {self.area()}'
        return output
        

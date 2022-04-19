#circle.py
import math

class Circle:
    def __init__(self):
        self._radius = 0
        #we don't normally print here
        #but for lecture we will
        print('Hey, you made a Circle!')

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

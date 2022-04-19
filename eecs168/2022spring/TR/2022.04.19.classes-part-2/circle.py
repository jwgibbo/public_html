#circle.py

class Circle:
    def __init__(self, radius=0):
        if radius > 0:
            self._radius = radius
        else:
            self._radius = 0
        #we don't normally do this
        print('You made a Circle')

    def area(self):
        ans = 3.14*self._radius**2
        return ans

    def circumference(self):
        ans = 2*3.14*self._radius
        return ans

    def set_radius(self, radius):
        if radius > 0:
            self._radius = radius
        else:
            self._radius = 0

    def get_radius(self):
        return self._radius

    def __lt__(self, other):
        if self._radius < other._radius:
            return True
        else:
            return False

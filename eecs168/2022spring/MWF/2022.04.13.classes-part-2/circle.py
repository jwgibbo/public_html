#circle.py
import math

class Circle:
    def __init__(self, r):
        self.radius = r
        #we don't normally print here
        #but for lecture we will
        print('Hey, you made a Circle!')

    def area(self):
        ans = math.pi*self.radius**2
        return ans

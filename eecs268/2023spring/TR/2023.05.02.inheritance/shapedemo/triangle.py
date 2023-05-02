#triangle.py
from shape import Shape

class Triangle(Shape):
    def __init__(self):
        self.base = 0
        self.height = 0

    def area(self):
        return (1/2)*self.base*self.height

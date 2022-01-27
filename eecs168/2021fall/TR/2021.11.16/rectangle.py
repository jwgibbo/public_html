#rectangle.py
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2*self.length + 2*self.width

    def is_larger(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

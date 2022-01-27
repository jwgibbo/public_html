#rectangle.py

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimiter(self):
        return 2*self.width + 2*self.height

    #Call this by doing: rec1.is_larger(rec2)
    def is_larger(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ge__(self, other):
        return self > other or self == other

    #Define overload of <
    def __lt__(self, other):
        return not self >= other

    #Define overload of <=
    def __le__(self, other):
        return not self > other
    
    

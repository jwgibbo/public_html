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
        
    #rec1 > rec2
    #rec1 ==> self, rec2 ==> other    
    def __gt__(self, other):
        return self.area() > other.area()
    
    def __eq__(self, other):
        return self.area() == other.area()
        
    def __le__(self, other):
        return not self > other

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return not self >= other

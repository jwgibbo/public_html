#triangle.py

class Triangle:
    def __init__(self, new_base, new_height):
        print('__init__ called')
        #member variables
        self.base = new_base
        self.height = new_height

    def __eq__(self, other):
        if self.base == other.base and self.height == other.height:
            return True
        else:
            return False
    
    def __gt__(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

    #Goal: Define an area method
    def area(self):
        ans = (1/2)*self.base*self.height
        return ans

    def is_larger(self, other):
        if self.area() > other.area():
            return True
        else:
            return False
        

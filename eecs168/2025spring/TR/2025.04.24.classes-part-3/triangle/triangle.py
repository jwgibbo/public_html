#triangle.py

class Triangle:
    def __init__(self, base, height):
        print('init called')
        self.base = base
        self.height = height

    def area(self):
        ans = (1/2)*self.base*self.height
        return ans
        
    def __gt__(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

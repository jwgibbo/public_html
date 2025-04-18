#triangle.py
class Triangle:
    def __init__(self, base, height):
        print("Triangle's init called")
        #member variables
        self.base = base
        self.height = height

    def area(self):
        ans = 0.5*self.base*self.height
        return ans

    def is_larger(self, other_tri):
        if self.area() > other_tri.area():
            return True
        else:
            return False
        

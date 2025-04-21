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

    def __gt__(self, other):
        print('__gt__ called')
        if self.area() > other.area():
            return True
        else:
            return False

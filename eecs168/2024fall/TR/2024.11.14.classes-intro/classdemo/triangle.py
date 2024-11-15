#triangle.py

class Triangle:
    def __init__(self):
        print('Triangle init called')
        self.base = 0
        self.height = 0

    def area(self):
        ans = (1/2)*self.base*self.height
        return ans

    def is_larger(self, other_tri):
        return self.area() > other_tri.area()


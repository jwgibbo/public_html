#triangle.py

class Triangle:
    def __init__(self, base, height):
        #class members = parameter
        self.base = base
        self.height = height

    def area(self):
        ans = (1/2)*self.base*self.height
        return ans

    def set_base(self, base):
        self.base = base

    def set_height(self, height):
        self.height = height

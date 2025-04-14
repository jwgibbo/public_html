#triangle.py
class Triangle:
    def __init__(self):
        #member variables
        self.base = 0
        self.height = 0

    def area(self):
        ans = 0.5*self.base*self.height
        return ans

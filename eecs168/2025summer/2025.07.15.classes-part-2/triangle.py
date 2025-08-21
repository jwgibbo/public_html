#triangle.py

class Triangle:
    def __init__(self):
        print('__init__ called')
        #member variables
        self.base = -1
        self.height = -1

    #Goal: Define an area method
    def area(self):
        ans = (1/2)*self.base*self.height
        return ans

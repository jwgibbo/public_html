#triangle.py

class Triangle:
    def __init__(self):
        print('init called')
        self.base = 0.0
        self.height = 0.0

    def area(self):
        ans = (1/2)*self.base*self.height
        return ans
        
    def is_larger(self, other):
        #define this to see see if
        #self's area is larger than other's
        #area (return True/False)

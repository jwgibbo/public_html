#triangle.py

class Triangle:
    def __init__(self):
        print('__init__ called')
        self.base = 0
        self.height = 0

    def area(self):
        return (1/2)*self.base*self.height

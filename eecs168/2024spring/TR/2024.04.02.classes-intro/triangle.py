#triangle.py

class Triangle:
    def __init__(self):
        print('init called')
        self.base = 0
        self.height = 0

    def area(self):
        print('area called')
        return (1/2)*self.base*self.height

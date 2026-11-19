#triangle.py

class Triangle:
    def __init__(self, base, height):
        print('init called')
        self.base = base
        self.height = height

    def area(self):
        result = (1/2)*self.base*self.height
        return result

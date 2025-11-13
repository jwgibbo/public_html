#triangle.py

class Triangle:
    def __init__(self, base, height):
        print('init called')
        self.base = base
        self.height = height

    def area(self):
        result = self.base*self.height*0.5
        return result

    

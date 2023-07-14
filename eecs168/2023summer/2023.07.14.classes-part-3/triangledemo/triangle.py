#triangle.py

class Triangle:
    def __init__(self, base=0, height=0):
        self.base = base
        self.height = height

    def area(self):
        answer = (1/2)*self.base*self.height
        return answer

    

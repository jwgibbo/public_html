#triangle.py
class Triangle:
    def __init__(self):
        self.base = 0
        self.height = 0

    def area(self):
        answer = self.base*self.height*(1/2)
        return answer

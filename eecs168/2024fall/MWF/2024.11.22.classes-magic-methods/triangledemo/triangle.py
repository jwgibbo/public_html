#triangle.py

class Triangle:
    def __init__(self, base=0, height=0):
        print('Call to Triangle init made')
        self.base = base
        self.height = height

    def area(self):
        ans = (1/2)*self.base*self.height
        return ans

    def is_larger(self, other_tri):
        return self.area() > other_tri.area()

    def __gt__(self, other):
        #the left-hand argument is self
        #the right-hand argument is other
        return self.area() > other.area()

    def __eq__(self, other):
        return self.base == other.base and self.height == other.height

    def __str__(self):
        output = 'Triangle with base of '
        output += f'{self.base} and height '
        output += f'of {self.height}'
        return output

    def __repr__(self):
        output = f'Triangle({self.base}, {self.height})'
        return output

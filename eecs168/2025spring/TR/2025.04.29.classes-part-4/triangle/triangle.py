#triangle.py

class Triangle:
    def __init__(self, base, height):
        print('init called')
        self.base = base
        self.height = height

    def area(self):
        ans = (1/2)*self.base*self.height
        return ans
        
    def __gt__(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.area() == other.area():
            return True
        else:
            return False

    def __str__(self):
        output_str = 'Awesome Triangle with'
        output_str += ' a base of '
        output_str += str(self.base)
        output_str += ' and a height of '
        output_str += str(self.height)
        return output_str

    def __repr__(self):
        output_str = f'Triangle({self.base}, {self.height})'
        return output_str

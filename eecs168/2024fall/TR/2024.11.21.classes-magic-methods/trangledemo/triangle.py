#triangle.py

class Triangle:
    def __init__(self, base, height):
        print('Triangle init called')
        self.base = base
        self.height = height

    def area(self):
        ans = (1/2)*self.base*self.height
        return ans
    #           lhs   rhs
    def __gt__(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

    def __eq__(self, other):
        if self.base == other.base and self.height == other.height:
            return True
        else:
            return False

    def __str__(self):
        output_str = 'Triangle with base of '
        output_str += f'{self.base} and '
        output_str += f'height of {self.height}'
        return output_str

    def __repr__(self):
        output_str = f'Triangle({self.base}, {self.height})'
        return output_str

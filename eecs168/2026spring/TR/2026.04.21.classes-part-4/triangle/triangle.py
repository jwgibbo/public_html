#triangle.py

class Triangle:
    def __init__(self, base, height):
        print('Triangle init called')
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

    def __str__(self):
        output_str = f'Triangle with a base of '
        output_str += f'{self.base} and a height'
        output_str += f' of {self.height}'
        return output_str

    def __repr__(self):
        output_str = f'Triangle({self.base}, '
        output_str += f'{self.height})'
        return output_str

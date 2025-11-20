#triangle.py
class Triangle:
    def __init__(self, base, height):
        print('init called')
        self.base = base
        self.height = height

    def area(self):
        answer = self.base*self.height*(1/2)
        return answer

    def __gt__(self, other):
        if self.area() > other.area():
            return True
        else:
            return False

    def __str__(self):
        output_str = 'Triangle with base = '
        output_str += f'{self.base} and height = '
        output_str += f'{self.height}'
        return output_str

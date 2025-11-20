#triangle.py

class Triangle:
    def __init__(self, base, height):
        print('init called')
        self.base = base
        self.height = height

    def area(self):
        result = self.base*self.height*0.5
        return result

    def __str__(self):
        output_str = 'Triangle with base = '
        output_str += f'{self.base} height = '
        output_str += f'{self.height}'
        return output_str

    def __repr__(self):
        output_str = f'Triangle({self.base}, {self.height})'
        return output_str

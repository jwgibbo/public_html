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
        print('Triangle definition for > called')
        if self.area() > other.area():
            return True
        else:
            return False

    def __eq__(self, other):
        print('Triangle definition for == called')
        if self.base == other.base and self.height == other.height:
            return True
        else:
            return False

    def __str__(self):
        output_str = f'Triangle with base = {self.base}'
        output_str += f' and height = {self.height}'
        return output_str

    def __repr__(self):
        return f'Triangle({self.base}, {self.height})'
        

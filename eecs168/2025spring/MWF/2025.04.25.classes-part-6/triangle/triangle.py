#triangle.py
class Triangle:
    def __init__(self, base, height):
        print("Triangle's init called")
        #member variables
        self.base = base
        self.height = height

    def area(self):
        ans = 0.5*self.base*self.height
        return ans

    def __gt__(self, other):
        print('__gt__ called')
        if self.area() > other.area():
            return True
        else:
            return False

    def __str__(self):
        output_str = 'Triangle with base = '
        output_str += str(self.base)
        output_str += ' and height = '
        output_str += str(self.height)
        return output_str

    def __repr__(self):
        output_str = f'Triangle({self.base}, {self.height})'
        return output_str

#triangle.py

class Triangle:
    def __init__(self, base=0, height=0):
        self.base = base
        self.height = height

    def area(self):
        answer = (1/2)*self.base*self.height
        return answer
    
    def __repr__(self):
        return f"Triangle({self.base}, {self.height})"
    
    def __str__(self):
        output = f"Triangle: base={self.base} height={self.height}"
        return output
    
    def __lt__(self, rhs):
        return self.area() < rhs.area()

    def __eq__(self, rhs):
        return self.base == rhs.base and self.height == rhs.height

    def __ne__(self, rhs):
        return not(self == rhs)

    def __gt__(self, rhs):
        is_equal = (self == rhs)
        is_less_than = (self < rhs)
        return (not is_equal) and (not is_less_than)

    def __le__(self, rhs):
        return not (self > rhs)

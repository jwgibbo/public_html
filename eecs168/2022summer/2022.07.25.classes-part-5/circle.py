#circle.py

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        ans = 3.14*self.radius**2
        return ans

    def __lt__(self, other):
        if self.radius < other.radius:
            return True
        else:
            return False

    def __str__(self):
        output_string = f'Circle with radius:{self.radius}'
        return output_string    


    def __repr__(self):
        string = f'Circle({self.radius})'
        return string

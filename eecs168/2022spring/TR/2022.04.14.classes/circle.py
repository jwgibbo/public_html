#circle.py

class Circle:
    def __init__(self):
        self.radius = 0
        #we don't normally do this
        print('You made a Circle')

    def area(self):
        ans = 3.14*self.radius**2
        return ans

    def circumference(self):
        ans = 2*3.14*self.radius
        return ans
        

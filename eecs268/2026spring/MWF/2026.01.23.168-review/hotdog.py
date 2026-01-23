import math
class Hotdog:
    def __init__(self, radius, length):
        self.radius = radius
        self.length = length

    def volume(self):
        return (math.pi*self.radius**2)*self.length

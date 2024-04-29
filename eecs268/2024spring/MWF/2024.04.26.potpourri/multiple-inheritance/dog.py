from animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('Dog created')
        
        
    def eat(self):
        print('Dog eating')

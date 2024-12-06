from animal import Animal
class Cat(Animal):
    def __init__(self):
        super().__init__()
        print('Cat created')
        
        
    def eat(self):
        print('Cat eating')

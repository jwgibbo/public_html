#dog.py
from animal import Animal

class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__(age) #Animal's
        print('Dog init called')
        self.breed = breed
        
    def sleep(self):
        print('Hrp, hrp, hrp, hrp HRP, hrp')

    def do_trick(self):
        print('Dog is doing an amazing trick')

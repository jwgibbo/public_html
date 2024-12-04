#dog.py
from animal import Animal

class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__(age)
        print('Dog created')
        self.breed = breed

    def sleep(self):
        print('Hrp, hrp, hrp-hrp, HRRP')
        
    def do_trick(self):
        print('Dog doing amazing trick!')

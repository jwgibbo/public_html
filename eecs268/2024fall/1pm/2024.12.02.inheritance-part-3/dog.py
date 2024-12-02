#dog.py
from animal import Animal
class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__(age)
        print('Dog created')
        self.breed = breed
        
    def do_trick(self):
        print('Amazing Dog trick happening')

    def sleep(self):
        print('Hrph, hrp-hrp-hrp, HRRRP')

#dog.py

from animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('Dog created')
        self.breed = 'UNDEFINED'
    
    def do_trick(self):
        print('Dog doing an amazing trick')

    def sleep(self):
        print('Dog sleeping. Hrp hrp hrp HRP')

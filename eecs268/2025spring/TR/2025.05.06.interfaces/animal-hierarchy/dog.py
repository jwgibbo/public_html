#dog.py

from animal import Animal

class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__(age)
        print('Dog created')
        self.breed = breed
        
    def do_trick(self):
        print('Dog doing amazing trick!')

    def sleep(self):
        print('Dog sleeping...')
        print('Hrp. Hrp HRP. Hrp hrrp.')

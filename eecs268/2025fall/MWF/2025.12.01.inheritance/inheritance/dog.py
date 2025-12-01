#dog.py

from animal import Animal

class Dog(Animal):
    def __init__(self, age, tail_length):
        super().__init__(age)
        print('Dog created')
        self.tail_length = tail_length
        
    def do_trick(self):
        print('This', self.age, 'year old dog')
        print('Dog doing an amazing trick!')

    def sleep(self):
        self.do_trick()
        print('Hrp. Hrp. Hrp HRP.')

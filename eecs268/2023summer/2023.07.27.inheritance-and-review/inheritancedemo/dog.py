#dog.py

from animal import Animal

class Dog(Animal):
    def __init__(self, temperment):
        super().__init__()
        self.temperment = temperment
        print('Dog created')

    def sleep(self):
        self.do_trick()
        self.temperment = 'sleepy'
        print('Hrp, hrp, hrp, HRPH!')

    def do_trick(self):
        print('Dog doing an amazing trick!')

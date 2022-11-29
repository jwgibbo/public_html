#dog.py

from animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.floppy_ears = True
        print('Dog created...')

    def do_trick(self):
        print('Oloie (dog trick happening)')

    def sleep(self):
        print('Hrph. Hrph, hrph. HRPH!')

#dog.py

from animal import Animal

class Dog(Animal):
    def __init__(self, age):
        super().__init__(age)
        self.age = self.age * 7
        prisnt('Dog Created')
        self.ear_type = ''

    def do_trick(self):
        print('Dog doing amazing trick')

    def sleep(self):
        self.do_trick()
        print('Dog goes hrp, hrp-hrp, HRP, hrph')

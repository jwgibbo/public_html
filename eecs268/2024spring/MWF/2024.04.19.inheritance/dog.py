#dog.py

from animal import Animal

class Dog(Animal):
    def do_trick(self):
        print('Dog doing amazing trick')

    def sleep(self):
        self.do_trick()
        print('Dog goes hrp, hrp-hrp, HRP, hrph')

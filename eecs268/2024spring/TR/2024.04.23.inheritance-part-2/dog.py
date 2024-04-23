#dog.py
from animal import Animal

class Dog(Animal):
    def __init__(self, age):
        super().__init__(age) #Animal's init
        print('Dog created')
        self.floppy_ear_level = 0
        
    def zoomies(self):
        print('freeeeeeeeeeeeedom!')

    def sleep(self):
        self.zoomies()
        print('Scratching & Circling')
        print('hrp, hrp, hrp HRP!')

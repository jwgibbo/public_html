#dog.py
from animal import Animal

class Dog(Animal):
    def __init__(self, age, ear_type):
        super().__init__(age) #Animal's init
        print('Dog created')
        self.ear_type = ear_type
        
    def do_trick(self):
        print('Dog doing amazing trick!')

    #override the Animal definition
    def sleep(self):
        print('One trick then bedtime')
        self.do_trick()
        print('Hrp, hrp, rhpr hrp HRRP! hrp')

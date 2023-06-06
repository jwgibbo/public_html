#dog.py

from animal import Animal

#The Dog class inherits from the Animal class
class Dog(Animal):
    def __init__(self):
        super().__init__() #Animal's 
        print('Dog created')

    def do_trick(self):
        print('Dog doing amazing trick')

    def sleep(self):
        print('Hrp. Hrph, hrp hrph!!!')
        

#dog.py

from animal import Animal

#     Subclass(Superclass)
class Dog(Animal):
    def __init__(self, age, fur_type):
        #call Animal's init
        super().__init__(age)
        print('Dog init called')
        self.fur_type = fur_type
        
    def do_trick(self):
        print('Dog doing an amazing trick!')

    def sleep(self):
        print('Hrp, hrp, hrp. HRP. Hrp. Hrp. HRP!')

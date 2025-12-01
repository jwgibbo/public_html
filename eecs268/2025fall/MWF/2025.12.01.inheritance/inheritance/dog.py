#dog.py

from animal import Animal

#     Derived(Base)
class Dog(Animal):
    def __init__(self, age, breed):
        #Call Animal's init
        super().__init__(age)
        print('Dog created')
        self.breed = breed
    
    def do_trick(self):
        print('Dog is doing an amazing trick')

    def sleep(self):
        print('Dog is sleeping')
            

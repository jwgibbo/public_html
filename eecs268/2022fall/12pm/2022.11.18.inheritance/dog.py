#dog.py

from animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.breed = 'no breed assigned'
    
    def do_trick(self):
        print('Whoa! Look at that trick!')

    

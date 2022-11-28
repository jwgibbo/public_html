#dog.py

from animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.breed = 'no breed assigned'
        self.type = 'Dog'
        print('Dog created')
    
    def do_trick(self):
        print('Whoa! Look at that trick!')

    def sleep(self):
        print('Hrph. Hrph-hrph. HRPH!')

    def __eq__(self, other):
        '''This is an example of
        polymorphism!'''
        

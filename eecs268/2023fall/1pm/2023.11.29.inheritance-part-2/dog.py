#dog.py
from animal import Animal

#     SubClass(SuperClass)
class Dog(Animal):
    def __init__(self, age, breed):
        super().__init__(age)
        print('Dog init called')
        self.breed = breed
    
    def sleep(self):
        self.do_trick()
        print(f'Your {self.breed} is Hrp,hrp,hrping')
        

    def do_trick(self):
        print('Amazing trick happening!')

from dog import Dog
from cat import Cat
from animal import Animal

class CatDog(Dog, Cat):
    def __init__(self):
        super().__init__()
        print('CatDog created')

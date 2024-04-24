from dog import Dog

from cat import Cat

class CatDog(Cat, Dog):
    def __init__(self):
        super().__init__()
        print('CatDog created')

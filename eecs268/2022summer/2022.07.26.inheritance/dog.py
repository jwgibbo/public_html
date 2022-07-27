#dog.py
from animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('Dog created')

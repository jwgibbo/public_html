#animal.py

class Animal:
    def __init__(self, age):
        print('Animal created')
        self.age = age

    def eat(self):
        print('Animal eating...')

    def sleep(self):
        print('Animal sleeping...')

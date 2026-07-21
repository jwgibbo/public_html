#animal.py
#DISCLAIMER: This class is for educational purposes

class Animal:
    def __init__(self, age):
        print('Animal init called')
        self.age = age

    def eat(self):
        print('Animal is eating')

    def sleep(self):
        print('Animal is sleeping')

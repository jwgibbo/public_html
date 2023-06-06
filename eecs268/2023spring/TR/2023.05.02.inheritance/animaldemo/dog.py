#dog.py
from animal import Animal
class Dog(Animal):
    def __init__(self, ear_type):
        super().__init__()
        self.ear_type = ear_type
        print('Dog created')

    def sleep(self):
        self.do_trick()
        print(self.ear_type, 'ears are tuckered out')
        print('Hrph. Hrp. Hrp, hrp! HRPH!')

    def do_trick(self):
        print('Amazing trick occurs!')

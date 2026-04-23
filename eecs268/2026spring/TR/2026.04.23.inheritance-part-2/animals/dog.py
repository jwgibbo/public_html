#dog.py

from animal import Animal

class Dog(Animal):
    def __init__(self):
        super().__init__() #Animal's init
        print('Dog created')
        self.owner = 'UNKNOWN'
        
    def do_trick(self):
        print('Dog doing amazing trick! Wow!')

    def sleep(self):
        print(self.owner, 'put a bed out')
        print(self.owner, 'asks for a trick before bed')
        self.do_trick()
        print('Hrp. Hrp, hrph HRPH.')

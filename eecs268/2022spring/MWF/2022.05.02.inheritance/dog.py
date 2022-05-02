#dog.py

from animal import Animal


class Dog(Animal):
    def __init__(self):

        #Call Animal's init
        Animal.__init__(self)

        self.breed = 'NOT SET'
        
        print('You made a Dog')
        
    def do_trick(self):
        print('Dog doing amazing trick!')

    def sleep(self):
        super().sleep()
        print('Ruf. roof. roooof. rof')
        print('*kick* *kick*')
        print('Ruf. roof. roooof. rof')
        print('SUDDENLY STARTLED')

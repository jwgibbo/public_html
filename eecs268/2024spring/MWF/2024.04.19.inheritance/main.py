#main.py

from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    print('------Play time------')
    some_animal.eat()
    some_animal.sleep()
    print('---------------------')

def main():
    my_animal = Animal()
    my_dog = Dog()
    
    play_with_animal(my_animal)
    #my_animal.do_trick() ERROR
    play_with_animal(my_dog)
    my_dog.do_trick()

main()

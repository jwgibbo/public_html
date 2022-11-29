#main.py

from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    print('Playing with some animal')
    some_animal.eat()
    some_animal.sleep()

def main():
    my_animal = Animal()
    my_dog = Dog()

    play_with_animal(my_animal)
    play_with_animal(my_dog)

    
    #my_animal.do_trick() ERROR
    print('=======')

    my_dog.do_trick()
    print(my_dog.floppy_ears)
    print(my_dog.type)

main()

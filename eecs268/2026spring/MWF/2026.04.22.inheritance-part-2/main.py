#main.py

from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    print('Play time!')
    some_animal.eat()
    print('Nap time!')
    some_animal.sleep()

def main():
    my_animal = Animal()
    my_dog = Dog()

    #my_animal.do_trick() ERROR

    play_with_animal(my_animal)
    play_with_animal(my_dog)

main()

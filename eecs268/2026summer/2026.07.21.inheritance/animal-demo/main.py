#main.py

from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    print('animal age =', some_animal.age)
    some_animal.eat()
    some_animal.sleep()

def main():
    my_animal = Animal(5)
    print(type(my_animal))
    play_with_animal(my_animal)

    #my_animal.do_trick() ERROR

    my_dog = Dog(13, 'fluffy')
    print(type(my_dog))
    play_with_animal(my_dog)
    print('my_dog fur type =', my_dog.fur_type)
    my_dog.do_trick()

main()

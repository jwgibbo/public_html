#main.py

from animal import Animal
from dog import Dog

def main():
    my_animal = Animal()
    my_dog = Dog()

    my_animal.eat()
    my_animal.sleep()

    print('=======')

    my_dog.do_trick()
    my_dog.eat()
    my_dog.sleep()
    print(my_dog.floppy_ears)
    print(my_dog.type)

main()

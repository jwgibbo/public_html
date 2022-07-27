#main.py

from animal import Animal
from dog import Dog

def main():
    my_animal = Animal()
    my_animal.eat()
    my_animal.sleep()

    print(type(my_animal))
    my_dog = Dog()
    print(type(my_dog))
    my_dog.eat()
    my_dog.sleep()

main()

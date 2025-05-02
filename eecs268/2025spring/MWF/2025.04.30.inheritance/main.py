#main.py

from animal import Animal
from dog import Dog

def main():
    my_animal = Animal()
    my_animal.eat()
    my_animal.sleep()

    my_dog = Dog()
    my_dog.age = 16
    my_dog.eat()
    my_dog.sleep()
    print(my_dog.age)
main()

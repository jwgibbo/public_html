from animal import Animal
from cat import Cat
from dog import Dog
from catdog import CatDog

def main():
    my_animal = Animal()
    print('-----------')
    my_cat = Cat()
    print('-----------')
    my_dog = Dog()
    print('-----------')
    my_catdog = CatDog()
    print('-----------')

    my_animal.eat()
    print('-----------')
    my_cat.eat()
    print('-----------')
    my_dog.eat()
    print('-----------')
    my_catdog.eat()
    print(CatDog.__mro__)


main()

     



#main.py

from animal import Animal
from dog import Dog

def main():
    my_animal = Animal()
    my_dog = Dog()
    print(my_dog.age)

    my_animal.eat()
    my_animal.sleep()

    my_dog.eat()
    my_dog.sleep()
    my_dog.do_trick()
    #my_animal.do_trick() ERROR

main()

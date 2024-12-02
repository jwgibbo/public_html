#main.py

from animal import Animal
from dog import Dog

def main():
    my_animal = Animal(5)
    my_dog = Dog(16, 'fluff bucket')

    my_animal.eat()
    my_animal.sleep()
    #my_animal.do_trick() ERROR

    print('age =', my_dog.age)
    print('breed =', my_dog.breed)
    my_dog.eat()
    my_dog.sleep()
    my_dog.do_trick()

main()

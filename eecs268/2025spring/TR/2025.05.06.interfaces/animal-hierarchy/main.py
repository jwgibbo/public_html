#main.py

from animal import Animal
from dog import Dog

def main():
    my_animal = Animal(10)
    my_animal.eat()
    my_animal.sleep()
    print('Animal age =', my_animal.age)
    # my_animal.do_trick() ERROR

    my_dog = Dog(5, 'shih tzu')
    my_dog.eat()
    my_dog.sleep()
    my_dog.do_trick()
    print(my_dog.breed)
    print('Dog age =', my_dog.age)

main()

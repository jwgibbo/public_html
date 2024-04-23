#main.py
from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    print('------Play time!--------')
    some_animal.eat()
    some_animal.sleep()
    print('------------------------')

def main():
    my_animal = Animal(5)
    my_dog = Dog(4)

    play_with_animal(my_animal)

    play_with_animal(my_dog)

    print('animal age:', my_animal.age)
    print('dog age:', my_dog.age)

    my_dog.zoomies()
    #my_animal.zoomies() ERROR
main()

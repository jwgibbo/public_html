#main.py

from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    some_animal.eat()
    some_animal.sleep()

def main():
    my_animal = Animal()
    my_dog = Dog()

    play_with_animal(my_animal)

    #This will run the dog's version
    #of sleep. This is called
    # POLYMORPHISM
    play_with_animal(my_dog)
    print(my_animal.age)
    print(my_dog.age)


    print('Bye!')

main()

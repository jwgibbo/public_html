#main.py
from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    some_animal.eat()
    some_animal.sleep()

def main():
    my_animal = Animal()
    my_dog = Dog('floppy')

    play_with_animal(my_animal)

    play_with_animal(my_dog)
    """
    my_dog.do_trick()
    print(my_dog.age)
    print(my_dog.ear_type)
    """
main()

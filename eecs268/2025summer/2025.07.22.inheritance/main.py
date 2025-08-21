#main.py
from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    print('playtime started!')
    some_animal.eat()
    some_animal.sleep()
    print('playtime over!')

def main():
    my_animal = Animal(5)
    my_dog = Dog(16, 'floppy')

    play_with_animal(my_animal)
    #my_animal.do_trick() ERROR Animals can't do tricks

    play_with_animal(my_dog)
    my_dog.do_trick()

    print('Animal age:', my_animal.age)
    print('Dog age:', my_dog.age)
    print('Dog ear type:', my_dog.ear_type)

main()

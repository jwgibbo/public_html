#main.py

from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    print('treat time!')
    some_animal.eat()
    print('nap time!')
    some_animal.sleep()

def main():
    my_animal = Animal()
    play_with_animal(my_animal)
    #my_animal.do_trick() ERROR
    my_dog = Dog() #Animal and Dog init called
    my_dog.owner = 'John'
    play_with_animal(my_dog)



main()

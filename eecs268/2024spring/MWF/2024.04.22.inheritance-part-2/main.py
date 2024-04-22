#main.py

from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    print('------Play time------')
    some_animal.eat()
    some_animal.sleep()
    print(f'This animal is {some_animal.age} years old')
    print('---------------------')

def main():
    my_animal = Animal(5)
    my_dog = Dog(4)
       
    play_with_animal(my_animal)
    #my_animal.do_trick() ERROR
    play_with_animal(my_dog)
    my_dog.do_trick()

main()

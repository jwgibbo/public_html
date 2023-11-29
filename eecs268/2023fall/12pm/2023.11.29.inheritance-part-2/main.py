#main.py
from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    some_animal.eat()
    some_animal.sleep()

def main():
    my_animal = Animal(5) #Animal's init
    play_with_animal(my_animal)
    print(my_animal.age)
    #my_animal.do_trick()

    my_dog = Dog(15, 'fluff bucket') #Animal's init?

    play_with_animal(my_dog)
    
    my_dog.do_trick()
    print(my_dog.age)
    print(my_dog.breed)

main()

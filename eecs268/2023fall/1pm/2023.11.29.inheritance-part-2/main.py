#main.py
from animal import Animal
from dog import Dog

def play_with_animal(some_animal):
    some_animal.eat()
    some_animal.sleep()

def main():
    my_animal = Animal(5)
    play_with_animal(my_animal)
    #my_animal.do_trick() ERROR
    print(my_animal.age)

    my_dog = Dog(15, 'fluff bucket')  #Animal's init
    play_with_animal(my_dog)
    my_dog.do_trick()   #Dog's do_trick
    print(my_dog.age)
    print(my_dog.breed)

main()
    

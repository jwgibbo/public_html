#main.py

from animal import Animal
from dog import Dog

def main():
    my_animal = Animal(5)
    my_animal.eat()
    my_animal.sleep()
    #my_animal.do_trick()
    print(my_animal.age)

    my_dog = Dog(17, 'corgi')
    my_dog.eat()
    my_dog.sleep()
    my_dog.do_trick()
    print(my_dog.age)
    print(my_dog.breed)
    

    

    
main()

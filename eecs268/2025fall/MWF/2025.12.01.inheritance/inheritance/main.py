#main.py

from animal import Animal
from dog import Dog

def main():
    my_animal = Animal(5)
    my_animal.eat()
    my_animal.sleep()
    print('Animal age =', my_animal.age)
    # my_animal.do_trick() ERROR
    
    my_dog = Dog(16, .333)
    my_dog.eat()
    my_dog.sleep()
    my_dog.do_trick()
    print('Dog age = ', my_dog.age)
    print('Dog tail length =', my_dog.tail_length)
    

    
main()

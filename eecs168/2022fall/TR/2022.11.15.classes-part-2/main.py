#main.py

#import the Triangle class
from triangle import Triangle

def main():
    #my_set is an instance of the set class
    #my_set is an object of type set
    my_set = set()

    my_tri = Triangle()
    my_tri2 = Triangle()

    my_tri.base = 5
    my_tri.height = 10

    my_tri2.base = 20
    my_tri2.height = 50

    print(my_tri.area())
    print(my_tri2.area())

    print(count('a'))


main()

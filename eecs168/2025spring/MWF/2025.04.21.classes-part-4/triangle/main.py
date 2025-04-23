#main.py
from triangle import Triangle

def main():
    my_tri = Triangle(20, 50)
    print(my_tri.area())

    your_tri = Triangle(20, 50)
    print(your_tri.area())

    #  self     other
    if my_tri > your_tri:
        print('my_tri is larger')
    else:
        print('your_tri is larger (or equal)')

    #my_tri = your_tri
    if my_tri == your_tri:
        print('they are equal')
    else:
        print('they are not equal')

main()

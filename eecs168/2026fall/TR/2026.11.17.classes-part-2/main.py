#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(10, 20) #calls init
    your_tri = Triangle(7, 13)#calls init


    print(my_tri.area())
    print(your_tri.area())


main()

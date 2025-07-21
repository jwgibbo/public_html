#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(20, 30) #instance
    your_tri = Triangle(20, 30) #instance

    #Print member variables
    print(my_tri.base)
    print(my_tri.height)
    print(your_tri.base)
    print(your_tri.height)

    #  self     other
    #calls __gt__
    if my_tri > your_tri:
        print('I have a bigger triangle')
    else:
        print('Something is wrong with my Triangle')

    if my_tri == your_tri:
        print('equivalent')
    else:
        print('different')

main()

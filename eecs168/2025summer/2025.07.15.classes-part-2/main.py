#main.py

from triangle import Triangle

def main():
    my_tri = Triangle() #instance
    your_tri = Triangle() #instance

    my_tri.base = 5
    my_tri.height = 10

    your_tri.base = 20
    your_tri.height = 30

    #Print member variables
    print(my_tri.base)
    print(my_tri.height)
    print(your_tri.base)
    print(your_tri.height)

    #Print the areas
    print(my_tri.area()) #self refers to my_tri's Triangle
    print(your_tri.area())#self refers to your_tri's Triangle


main()

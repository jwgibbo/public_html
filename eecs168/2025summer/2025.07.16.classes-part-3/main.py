#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(50, 100) #instance
    your_tri = Triangle(20, 30) #instance

    #Print member variables
    print(my_tri.base)
    print(my_tri.height)
    print(your_tri.base)
    print(your_tri.height)

    #Print the areas
    print(my_tri.area()) #self refers to my_tri's Triangle
    print(your_tri.area())#self refers to your_tri's Triangle

    if my_tri.is_larger(your_tri):
        print('I have a bigger triangle')
    else:
        print('Something is wrong with my Triangle')

    if your_tri.is_larger(my_tri):
        print('You have a larger triangle')
    else:
        print('You do NOT have a larger triangle')

main()

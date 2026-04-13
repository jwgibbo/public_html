#main.py

from triangle import Triangle
def main():
    my_tri = Triangle(10, 20) #implitcly calls init
    your_tri = Triangle(30, 40) #implitcly calls init

    print('base =', my_tri.base)
    print('height =', my_tri.height)



    print(my_tri.area())
    print(your_tri.area())

    #   self               other
    if my_tri.is_larger(your_tri):
        print('My triangle is larger')
    else:
        print('My triangle is not larger')

    #    self              other
    if your_tri.is_larger(my_tri):
        print('Your triangle is larger')
    else:
        print('Your triangle is not larger')
    
main()

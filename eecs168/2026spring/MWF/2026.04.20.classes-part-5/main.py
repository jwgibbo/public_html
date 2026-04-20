#main.py

from triangle import Triangle
def main():
    my_tri = Triangle(10, 20) #implitcly calls init
    your_tri = Triangle(10, 20) #implitcly calls init
    their_tri =  Triangle(10, 20)

    print('base =', my_tri.base)
    print('height =', my_tri.height)

    print(my_tri.area())
    print(your_tri.area())

    #   self     other
    if my_tri > your_tri:
        print('My triangle is larger')
    else:
        print('My triangle is not larger')

    #    self     other
    if your_tri == my_tri:
        print('They are equal')
    else:
        print('They are not equal')

    print(my_tri)   #implicit call to __str__
    print(your_tri) #implicit call to __str__

    tri_list = [my_tri, your_tri]
    print(tri_list) 
main()

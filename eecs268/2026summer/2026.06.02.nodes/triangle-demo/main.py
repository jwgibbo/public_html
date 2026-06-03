#main.py

from triangle import Triangle
def main():
    my_tri = Triangle(10, 20) #implitcly calls init
    your_tri = Triangle(30, 40) #implitcly calls init
    their_tri = your_tri
    their_tri.base = 0
    
    type(my_tri)
    type(your_tri)
    print(your_tri.area())
    print(their_tri.area())

    
main()

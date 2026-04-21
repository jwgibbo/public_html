#main.py

from triangle import Triangle

def main():

    my_tri = Triangle(10, 20) #calls init
    your_tri = Triangle(20, 32) #calls init
    their_tri = Triangle(10, 20)
    
    print(my_tri)
    print(your_tri)

    tri_list = [my_tri, your_tri]
    print(tri_list)
    
main()

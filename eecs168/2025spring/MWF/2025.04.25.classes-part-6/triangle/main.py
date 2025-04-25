#main.py
from triangle import Triangle

def main():
    my_tri = Triangle(20, 50)
    print(my_tri)

    your_tri = Triangle(20, 50)
    print(your_tri)

    triangles = []
    triangles.append(my_tri)
    triangles.append(your_tri)
    print(triangles)

main()

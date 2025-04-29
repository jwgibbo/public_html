#main.py

from triangle import Triangle

def main():
    my_tri = Triangle(5, 10)
    your_tri = Triangle(20, 30)

    print(my_tri)
    print(your_tri)

    triangles = []
    triangles.append(my_tri)
    triangles.append(your_tri)

    print(triangles)

main()

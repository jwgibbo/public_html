from triangle import Triangle

def main():
    my_tri = Triangle(20, 100)
    your_tri = Triangle(25, 35)

    print(my_tri.area())
    print(your_tri.area())

    #    self      other
    if your_tri > my_tri:
        print('your triangle is larger')
    else:
        print('my triangle is larger')

    if your_tri == my_tri:
        print('they are equal')
    else:
        print('they are not equal')

    print(my_tri)
    print(your_tri)

    triangles = []
    triangles.append(my_tri)
    triangles.append(your_tri)
    print(type(triangles))

    for tri in triangles:
        print(type(tri))
    
main()

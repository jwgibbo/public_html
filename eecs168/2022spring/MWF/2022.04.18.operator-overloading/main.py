#main.py

from circle import Circle

def main():
    circ1 = Circle()
    print(circ1)
    circ2 = Circle()

    circ1.set_radius(5)
    circ2.set_radius(10)

    #print the area of the larger
    #circle

    #circ1 is the calling object (i.e. self)
    #circ2 is the parameter (i.e. other)
    #Kind of like circ1.__gt__(circ2)
    if circ1 < circ2:
        print(circ1)
    else:
        print(circ2)

main()

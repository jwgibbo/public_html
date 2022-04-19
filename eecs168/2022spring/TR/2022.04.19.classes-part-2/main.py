#main.py

from circle import Circle

def main():
    circ1 = Circle()
    circ2 = Circle()

    circ1.set_radius(5)
    circ2.set_radius(10)

    #print the area of the smaller
    #circle

    if circ1 < circ2:
        print(circ1.area())
    else:
        print(circ2.area())
        

main()

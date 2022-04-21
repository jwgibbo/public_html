#main.py

from circle import Circle

def main():
    circ1 = Circle()
    circ1.set_radius(99)
    
    circ2 = Circle(99)



    print(circ1 is circ2)
    print(circ1 == circ2)
    print(circ1 < circ2)
    print(circ1 > circ2)
    print(circ1)
    print(circ2)

    my_circs = [circ1, circ2]
    print(my_circs)

main()

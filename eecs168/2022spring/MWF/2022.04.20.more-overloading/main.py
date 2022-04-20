#main.py

from circle import Circle

def main():
    circ1 = Circle(10)
    circ2 = Circle(5)
    
    print(circ1)
    print(circ2)

    #print the area of the larger
    #circle

    print(circ1 == circ2)
    print(circ1 is circ2)
    print(circ1 < circ2)
    print(circ1 > circ2)

    list_of_circs = [circ1, circ2]
    print(list_of_circs)

main()

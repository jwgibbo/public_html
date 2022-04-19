#main.py
from circle import Circle

def main():
    #implicit call to __init__
    circ1 = Circle()

    print(circ1.area())
    
    circ1.set_radius(10)
    print(circ1.area())

    circ1.set_radius(-99)
    print(circ1.area())

    circ1.set_radius(0)
    print(circ1.area())

    circ1.set_radius(415)
    #Goal: print the radius
    print(circ1.get_radius())

main()

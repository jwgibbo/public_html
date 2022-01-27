#driver.py
from circle import Circle

def main():
    circ1 = Circle()

    #unchecked assignment
    #circ1._radius = -5

    #check assignment
    circ1.set_radius(27)
    print(circ1.get_radius())
    print(circ1.area())

main()

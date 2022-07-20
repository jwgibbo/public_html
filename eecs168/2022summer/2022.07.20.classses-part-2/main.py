#main.py
#import the Circle class
from circle import Circle

def main():

    #implicit call to __init__
    circ1 = Circle()
    circ2 = Circle()

    circ1.radius = 5.5
    circ2.radius = 4.0

    print("radius =", circ1.radius)
    print("area =", circ1.area())

    print("radius =", circ2.radius)
    print("radius =", circ2.area())

main()

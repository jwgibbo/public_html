#main.py
from circle import Circle

def main():
    #implicit call to __init__
    circ1 = Circle(5.5)
    circ2 = Circle(10.5)
    
    #circ1.radius = 5.5
    #circ2.radius = 10.5

    print(circ1.radius)
    print(circ2.radius)

    print(circ1.area())
    print(circ2.area())


main()

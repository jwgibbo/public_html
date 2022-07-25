#main.py
#import the Circle class
from circle import Circle

def main():

    #implicit call to __init__
    circ1 = Circle(10)
    circ2 = Circle(20)


    print(circ1)

    my_circs = [circ1, circ2]
    print(type(my_circs))
    print(my_circs)

    my_other_circs = [Circle(10), Circle(20)]

    circ_as_string = str(circ1)

    print(circ_as_string)
    
main()

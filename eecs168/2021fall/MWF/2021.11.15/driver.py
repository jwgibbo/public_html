#driver.py
from rectangle import Rectangle

def main():
    rec1 = Rectangle(5, 10)
    rec2 = Rectangle(5, 10)

    print(rec1.is_larger(rec2))
    print(rec2.is_larger(rec1))
    print(rec1.is_larger(rec1))

    #makes implicity call to
    #our __gt__
    #rec1 is self
    #rec2 is other
    print(rec1 > rec2)
    print(rec1 == rec2)
    print(rec1 >= rec2)
main()

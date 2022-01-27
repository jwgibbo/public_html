#driver.py
from rectangle import Rectangle
def main():
    rec1 = Rectangle(10,20)
    rec2 = Rectangle(2,3)

    print(rec1.is_larger(rec2))
    print(rec2.is_larger(rec1))
    print(rec1.is_larger(rec1))

    print(rec1 > rec2)


main()

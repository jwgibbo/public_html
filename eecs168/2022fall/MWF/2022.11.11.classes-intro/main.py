#main.py
from triangle import Triangle

def main():
    my_set = set()

    tri_one = Triangle()
    tri_two = Triangle()

    tri_one.base = 10
    tri_one.height = 5
    print(tri_one.base)
    print(tri_one.height)

    tri_two.base = 20
    tri_two.height = 30
    print(tri_two.base)
    print(tri_two.height)

    print("tri_one's area:", tri_one.area())
    print("tri_two's area:", tri_two.area())
    

main()

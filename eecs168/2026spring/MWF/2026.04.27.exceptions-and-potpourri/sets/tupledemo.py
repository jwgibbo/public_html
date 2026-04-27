#tupledemo.py

def main():
    my_tup = (5, 10, 15, 20)
    print(my_tup)
    print(my_tup[2])
    # my_tup[2] = 99 ERROR

    print('-----')
    for num in my_tup:
        print(num)

    #unpacking my_tup
    a, b, c, d = my_tup
    print(a, b, c, d)
main()

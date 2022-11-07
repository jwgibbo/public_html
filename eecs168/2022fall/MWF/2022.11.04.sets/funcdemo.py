def param_test(pos1, pos2, /, flx1, flx2, *, key1, key2):
    print(f'pos1={pos1}')
    print(f'pos2={pos2}')
    print(f'flx1={flx1}')
    print(f'flx2={flx2}')
    print(f'key1={key1}')
    print(f'key2={key2}')


def main():
    # param_test(1,2,3,4,5,6) ERROR for 5 and 6
    param_test(1, 2, 3, 4, key1=5, key2=6)
    # param_test(pos1=1, pos2=2, 3, 4, key1=5, key2=6) ERROR
    word = 'Frienday'
    print(len(word))
    # print(len(obj=word)) ERROR for using keyword on positional
    param_test(1, 2, 3, flx2=4, key1=5, key2=6)

    # param_test(1, 2, flx1=3, 4, key1=5, key2=6)
    # ERROR: Again, you can't have positional after keyword arguments
    
main()

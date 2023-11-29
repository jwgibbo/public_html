def funky_town(a=-1, b=-2, c=-3):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')

def downtown(pos1, pos2, /, mix1, mix2,*, kw1, kw2):
    print(f'{pos1=}')
    print(f'{pos2=}')
    print(f'{mix1=}')
    print(f'{mix2=}')
    print(f'{kw1=}')
    print(f'{kw2=}')
          

def main():
    downtown(1, 2, 3, 4, kw2=6, kw1=5)
    print('-------')
    downtown(1, 2, 3, mix2=4, kw1=5, kw2=6)
    print('-------')
    downtown(1, 2, mix2=4, mix1=3, kw1=5, kw2=6)
    print('-------')
    downtown(2, 1, mix2=4, mix1=3, kw1=5, kw2=6)
    


    '''
    funky_town(1,2,3)
    print('-------')
    funky_town(3,2,1) #position changed
    print('-------')
    funky_town(a=1, b=2, c=3) #keyword assignment
    print('-------')
    funky_town(c=3, a=1, b=2)
    print('-------')
    funky_town(1, 2, c=3)
    print('-------')
    funky_town(1, c=3, b=2)
    print('-------')
    #funky_town(a=1, 2, 3) ERROR
    print('-------')
    funky_town()
    print('-------')
    funky_town(1)
    print('-------')
    funky_town(c=3)
    '''
main()

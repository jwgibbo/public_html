def funky_town(a, b, c):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')
    
def func(pos1, pos2, /, mix1, mix2, *, kw1, kw2):
    print(f'{pos1=}')
    print(f'{pos2=}')
    print(f'{mix1=}')
    print(f'{mix2=}')
    print(f'{kw1=}')
    print(f'{kw2=}')

def main():
    func(1, 2, 3, 4, kw1=5, kw2=6)
    print('----------')
    func(1, 2, 3, 4, kw2=55, kw1=66)
    print('----------')
    func(1, 2, mix2=4, mix1=3, kw1=5, kw2=6)
    print('----------')
    func(1, 2, 3, mix2=4, kw1=5, kw2=6)
    '''
    funky_town(1, 2, 3)
    print('----------')
    funky_town(3, 1, 2)
    print('----------')
    funky_town(a=1, b=2, c=3)
    print('----------')
    funky_town(c=3, b=2, a=1)
    print('----------')
    funky_town(1, 2, c=3)
    print('----------')
    #funky_town(1, 3, b=2)
    '''
main()

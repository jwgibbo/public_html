def funkycity(a, b, c):
    print(f'a={a}')
    print(f'b={b}')
    print(f'{c=}')

def test(pos1, pos2, /, mix1, mix2, *, kw1, kw2):
    print(f'pos1={pos1}')
    print(f'pos2={pos2}')
    print(f'mix1={mix1}')
    print(f'mix2={mix2}')
    print(f'kw1={kw1}')
    print(f'kw2={kw2}')
    
def main():
    test(1, 2, 3, 4, kw1=5, kw2=6)
    print('-------------')
    test(1, 2, 3, 4, kw2=6, kw1=5)
    print('-------------')
    test(1, 2, mix1=3, mix2=4, kw1=5, kw2=6)
    print('-------------')
    #test(pos1=1, pos2=2, mix1=3, mix2=4, kw1=5, kw2=6)
    '''
    funkycity(1, 2, 3)
    print('------------')
    funkycity(3, 1, 2)
    print('------------')
    funkycity(1, c=2, b=3)
    print('------------')
    funkycity(c=5, a=10, b=20)
    '''

main()

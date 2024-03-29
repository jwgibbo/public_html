def func(pos1, pos2, /, mix1, mix2, *, kwA, kwB):
    print(f'pos1={pos1}')
    print(f'pos2={pos2}')
    print(f'mix1={mix1}')
    print(f'mix2={mix2}')
    print(f'kw1={kw1}')
    print(f'kw2={kw2}')

def main():
    func(1, 2, 3, 4, kw2=5, kw1=6)
    print('-------')
    func(1, 2, 3, mix2=4, kw1=5, kw2=6)
    print('-------')
    #
    #func(pos1=1, pos2=2, mix1=3, mix2=4, kw1=5, kw2=6)
    
    

main()

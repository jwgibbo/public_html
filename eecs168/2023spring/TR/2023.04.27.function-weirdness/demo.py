def funkytown(a, b):
    print(f'a={a}')
    print(f'b={b}')

def weird(pos1, pos2, /, mix1, mix2, *, key1, key2):
    print(f'pos1={pos1}')
    print(f'pos2={pos2}')
    print(f'mix1={mix1}')
    print(f'mix2={mix2}')
    print(f'key1={key1}')
    print(f'key2={key2}')

def main():
    choice = 'a'
    weird('A', 'B', 'C', 'D', key1='E', key2='F')
    print('-----------')
    weird('A', 'B', 'C', 'D', key2='E', key1='F')
    print('-----------')
    funkytown(5, 10)
    funkytown(a=5, b=10)
    funkytown(b=10, a=5)
    funkytown(10, b=5)


main()

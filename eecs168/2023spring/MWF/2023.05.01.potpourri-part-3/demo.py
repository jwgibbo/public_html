#demo.py
def func(a=-1, b=-2):
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
    weird('A', 'B', 'C', 'D', key1='E', key2='F')
    print('===========')
    weird('A', 'B', 'C', 'D', key2='E', key1='F')
    print('===========')
    weird('A', 'B', mix2='C', mix1='D', key2='E', key1='F')
    print('===========')
    weird('A', 'B', 'C', mix2='D', key2='E', key1='F')
    print('===========')
    weird('A', 'B', key1='C', key2='D', mix2='E', mix1='F')
    print('===========')

    
    func(10, 5)
    print('===========')
    func(5, 10)
    print('===========')
    func(a=10, b=5)
    print('===========')
    func(b=5, a=10)
    print('===========')
    func(88, 99)
    print('===========')
    func(88)
    print('===========')
    func()

main()

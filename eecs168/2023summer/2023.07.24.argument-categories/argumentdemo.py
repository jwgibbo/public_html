def default_func(param1, param2):
    print(f'param1 = {param1}', end='!!!\n')
    print(f'param2 = {param2}', end='!!!!!!!\n')

def demo(pos1, pos2, /, mix1, mix2, *, kw1, kw2):
    print(f'{pos1=}')
    print(f'{pos2=}')
    print(f'{mix1=}')
    print(f'{mix2=}')
    print(f'{kw1=}')
    print(f'{kw2=}')
    

def main():
    default_func(5, 10)
    default_func(10, 5)
    default_func(param1=5, param2=10)
    default_func(param2=10, param1=5)
    print('------')
    demo(1, 2, 3, 4, kw1=5, kw2=6)
    print('------')
    demo(1, 2, 3, kw2=6, kw1=5, mix2=4)
    print('------')
    # ERROR
    #demo(kw2=6, kw1=5, mix2=4, 1, 2, 3)

    # ERROR
    #demo(pos1=1, pos2=2, mix1=3, mix2=4, kw1=5, kw2=6)
    
main()

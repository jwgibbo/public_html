def default_func(a=0, b=0, c=0):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')

def arg_demo(a, b, c):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')

def main():
    arg_demo(5, 10, 15)
    arg_demo(a=5, b=10, c=15)
    arg_demo(c=15, a=5, b=10)
    arg_demo(5, c=15, b=10)
    '''
    default_func(5, 10, 15)
    default_func(5, 10)
    default_func(5)
    default_func()
    '''

main()
    

def default_func(a=0, b=0, c=0):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')

def main():
    default_func(5, 10, 15)
    default_func(5, 10)
    default_func(5)
    default_func()

main()

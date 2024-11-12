def arg_func(a, b, c):
    print(f'a={a}')
    print(f'b={b}')
    print(f'c={c}')
    
def main():
    arg_func(5, 10, 15)
    arg_func(a=5, b=10, c=15)
    arg_func(c=15, a=5, b=10)
    arg_func(5, 10, c=15)
    #arg_func(c=15, 5, 10) ERROR


main()

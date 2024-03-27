def add(num1, num2=0):
    return num1 + num2

def funkytown(a, b, c):
    print(f'a={a}')
    print(f'{b=}')
    print(f'{c=}')

def main():
    funkytown(1, 2, 3)
    print('-------')
    funkytown(3, b=2, c=1)
    print('-------')
    funkytown(c=1, a=3, b=2)
    

main()

def repeat_print(word, amount=1):
    for num in range(amount):
        print(word)

def takes_a_b(a, b):
    print(f'a={a}')
    print(f'b={b}')

def param_test(pos, /, flx, *, key):
    print(f'pos={pos}')
    print(f'flx={flx}')
    print(f'key={key}')    

def main():
    param_test(5, 10, key=15)
    param_test(5, flx=10, key=15)
    param_test(pos=5, flx=10, key=15)
    

    repeat_print('Thursday', 3)
    repeat_print('Sunday')

    takes_a_b(10, 5)
    takes_a_b(a=10, b=5)
    takes_a_b(b=5, a=10)

    

main()

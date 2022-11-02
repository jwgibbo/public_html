def repeat_print(word, amount=1):
    for num in range(amount):
        print(word)

def takes_a_b(a, b):
    print(f'a = {a}')
    print(f'b = {b}')

def main():
    repeat_print('meatloaf', 3)
    repeat_print('catfood')
    takes_a_b(10, 5)
    takes_a_b(a=10, b=5)
    takes_a_b(b=99, a=-1)
    takes_a_b(z=5, t=2)

main()

def rec_fact(num):
    if num <= 1:
        return 1
    else:
        return num*rec_fact(num-1)

def main():
    print('1! =', rec_fact(1))
    print('2! =', rec_fact(2))
    print('3! =', rec_fact(3))
    print('4! =', rec_fact(4))

main()

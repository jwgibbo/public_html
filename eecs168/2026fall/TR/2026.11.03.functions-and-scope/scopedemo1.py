def num_changer(num):
    print('num_changer num =', num)
    num = -1
    print('num_changer num =', num)

def main():
    num = 5
    print('main num =', num)
    num = num_changer(num)
    print('main num =', num)

main()
